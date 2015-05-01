from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
import cm.forms as f
import cm.models as m
import django.contrib.auth as au
import cm.importer as im

# Create your views here.



def add_program(request):
    if request.method == 'GET':
        form = f.ProgramForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = f.ProgramForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            p_id = form.cleaned_data['program_id']
            name = form.cleaned_data['name']
            level = form.cleaned_data['level']
            type = form.cleaned_data['type']
            desc = form.cleaned_data['description']
            program = m.Program.objects.create(program_id=p_id, name=name, level=level, type=type, description=desc)
            return HttpResponseRedirect(reverse('program_detail', kwargs={'program_id': program.program_id}))

    return render(request, 'add_program.html', {
        'form': form,
    })

@staff_member_required
def import_subject(request, program_id):
    if request.method == 'GET':
        form = f.UploadFileForm()
    else:
        form = f.UploadFileForm(request.POST, request.FILES)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            program = m.Program.objects.get(program_id=program_id)
            im.importXlsData(request.FILES['file'].read(), program)

    return render(request, 'import_subject.html', {
        'form': form,
    })


def view_programs(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    program_list = m.Program.objects.all()
    context = {'program_list': program_list}
    return render(request, 'view_program.html', context)

def program_detail(request, program_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    program = m.Program.objects.get(program_id=program_id)
    general_bok_list = m.BlockOfKnowledge.objects.filter(program_id=program_id, majors=None)
    general_bok_subjects = []
    for i in range (len(general_bok_list)):
        general_bok_subjects.append(general_bok_list[i].subjects.all())

    major_list = m.Major.objects.filter(program_id=program_id)
    major_bok_list = []
    major_bok_subject = []
    for i in range (len(major_list)):
        bok_list = major_list[i].blockofknowledge_set.all()
        major_bok_list.append(bok_list)
        temp = []
        for j in range(len(bok_list)):
            temp.append(bok_list[j].subjects.all())
        major_bok_subject.append(temp)
    print(major_bok_subject)
    context = {'program': program, 'major_list': major_list, 'general_bok_list': general_bok_list, 'general_bok_subjects': general_bok_subjects, 'major_bok_list': major_bok_list, 'major_bok_subject': major_bok_subject}
    return render(request, 'program_detail.html', context)

def major_detail(request, program_id, major_id):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    major = m.Major.objects.get(id=major_id)
    bok_list = major.blockofknowledge_set.all()
    context = {'major': major, 'bok_list': bok_list}
    return render(request, 'major_detail.html', context)

def bok_detail(request, bok_id):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    bok = m.BlockOfKnowledge.objects.get(id=bok_id)
    subject_list = bok.subjects.all()
    context = {'bok': bok, 'subject_list': subject_list}
    return render(request, 'bok_detail.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = au.authenticate(username=username, password=password)
        if user:
            print(user)
            if user.is_active:
                au.login(request, user)
                return HttpResponseRedirect(reverse('cm.views.view_programs'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

def subject_detail(request, subject_id):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    subject = m.Subject.objects.get(subject_id=subject_id)
    assessmentmethods = subject.assessmentmethod_set.all()
    prerequisites = subject.prerequisites.all()
    resources = subject.resource_set.all()
    schedules = subject.teachingschedule_set.all()
    goals = subject.subjectgoal_set.all()
    context = {'subject': subject,
    'assessmentmethods':assessmentmethods,
    'prerequisites':prerequisites,
    'resources':resources,
    'goals':goals,
    'schedules':schedules}
    return render(request, 'subject_detail.html', context)