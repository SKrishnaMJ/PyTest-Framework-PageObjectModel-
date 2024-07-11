import openpyxl

book = openpyxl.load_workbook("/Users/saikrishnamj/Desktop/Udemy/pythonDemo.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)

for i in range(1, sheet.max_row+1):
    if sheet.cell(row=i, column=1).value == "Test3":
        for j in range(1,sheet.max_column+1):
            print(sheet.cell(row=i, column=j).value)

