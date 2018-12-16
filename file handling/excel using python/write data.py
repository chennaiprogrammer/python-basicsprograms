
"""
To install XlsxWriter for writing to Excel files:
pip install XlsxWriter

To install xlrd for reading Excel files:
pip install xlrd
"""

from xlsxwriter import Workbook

workbook = Workbook('first_file.xlsx')
worksheet=workbook.add_worksheet()
for i in range(0,100):
    worksheet.write(i,0,'Roll no')
    worksheet.write(i,1,i)


workbook.close()