import xlrd
import sys
import simplekml
from polycircles import polycircles
from kml import make_kml

# file_path = (r"C:\Users\Administrator\Desktop\Communication_Network\worldcities.xlsx")

# wb = xlrd.open_workbook(file_path)
# sheet = wb.sheet_by_index(0)


# number_of_values = 2

# x1 = (10000000,20000000,'yellow')
# x2 = (5000000,10000000,'red')
# x3 = (1000000,500000,'green')
# my_list = [x1, x2, x3]

# for j in range(number_of_values):
#     locations = []
#     for i in range(sheet.nrows):
#         locations.append(sheet.cell_value(i , 0))
#     lats = []
#     for i in range(sheet.nrows):
#         lats.append(sheet.cell_value(i, 1))
#     lngs = []
#     for i in range(sheet.nrows):
#         lngs.append(sheet.cell_value(i, 2))
#     values = []
#     for i in range(sheet.nrows):
#         values.append(sheet.cell_value(i, 3+j))
#     loc_tupples = list(zip(locations,lats, lngs, values))
#     headers = loc_tupples[0]
#     del loc_tupples[0]
#     make_kml(loc_tupples,my_list,7,headers[3])


def fetch_headers(file_path):
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    headers = sheet.row_values(0)
    return headers[3:]



def calculate(rng, file_path, condition_list, header):
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    # number_of_values = sheet.ncols - 3
    # print(f"This is {number_of_values} values!")
    locations = []
    values = []
    lats = []
    lngs = []
    value_list = []
    for i in sheet.row(0):
        value_list.append(i.value)
    for i in range(sheet.nrows):
        locations.append(sheet.cell_value(i , 0))
    
    for i in range(sheet.nrows):
        lats.append(sheet.cell_value(i, 1))
    
    for i in range(sheet.nrows):
        lngs.append(sheet.cell_value(i, 2))
    
    for i in range(sheet.nrows):
        values.append(sheet.cell_value(i, value_list.index(header)))
    loc_tupples = list(zip(locations,lats, lngs, values))
    del loc_tupples[0]
    make_kml(loc_tupples, condition_list, rng, header)




