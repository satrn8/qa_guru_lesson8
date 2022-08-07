import xlrd

book = xlrd.open_workbook(".\\resources\\file_example_XLS_10.xls")
print(book.nsheets)
print(book.sheet_names())
sheet = book.sheet_by_index(0)
print(f"Количество столбцов {sheet.ncols}")
print(f"Количетсво строк {sheet.nrows}")
print(f"Ячейка 0:3 = {sheet.cell_value(rowx=9, colx=3)}")
for i in range(sheet.nrows):
    print(sheet.row(i))
