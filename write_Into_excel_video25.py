import openpyxl

path = "C:/Users/Titan Tech-2/PycharmProjects/SeleniumWithPython/New folder/write_into_excel.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active  # workbook.get_sheet_by_name("Sheet1") //
# if excel file has more than one sheet then we have to specify the sheet name Code will be
# """workbook.get_sheet_by_name("Sheet1")""" instead of """workbook.active"""

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)