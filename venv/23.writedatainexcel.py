import openpyxl

path = "C:/Users/marut/Downloads/empty.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active
#workbook.get_sheet_names#to give by sheet name

for r in range(1,6):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="Welcome"

workbook.save(path)