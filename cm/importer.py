import xlrd
import cm.models as m

def importXlsData(f, p):
    workbook = xlrd.open_workbook(file_contents=f)
    worksheet = workbook.sheet_by_index(0)
    num_rows = worksheet.nrows
    curr_row = 4
    while curr_row < num_rows:
        sid = worksheet.cell_value(curr_row, 0)
        print(sid)
        name_en = worksheet.cell_value(curr_row, 1)
        name_vi = worksheet.cell_value(curr_row, 2)
        credit = worksheet.cell_value(curr_row, 3)
        theory_hour = worksheet.cell_value(curr_row, 4)
        practice_hour = worksheet.cell_value(curr_row, 5)
        desc = worksheet.cell_value(curr_row, 6)
        m.Subject.objects.create(subject_id=sid, name_en=name_en, name_vi=name_vi, num_of_credit=credit, theory_hr=theory_hour,
                                           practice_hr=practice_hour, program_id=p, description=desc)
        curr_row+=1
        print(curr_row)

