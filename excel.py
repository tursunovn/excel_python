import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="sales_managers.xlsx", data_only=True)
wb.active = 3
sheet = wb.active
rus = (sheet['C4'].value)
izza = (sheet['C5'].value)
alish = (sheet['C6'].value)


