
import xlrd


workbook = xlrd.open_workbook("first_file.xlsx")

worksheet=workbook.sheet_by_index(0)

rows=worksheet.nrows

for row in range(rows):
    first_col,second_col = worksheet.row_values(row)
    print(first_col,"  ",int(second_col))