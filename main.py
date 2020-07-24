import xlrd
import sys
import simplekml
from polycircles import polycircles
from kml import make_kml

file_path = (r"C:\Users\Administrator\Desktop\Communication_Network\worldcities.xlsx")

wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)


number_of_values = 2



for j in range(number_of_values):
    locations = []
    for i in range(sheet.nrows):
        locations.append(sheet.cell_value(i , 0))
    lats = []
    for i in range(sheet.nrows):
        lats.append(sheet.cell_value(i, 1))
    lngs = []
    for i in range(sheet.nrows):
        lngs.append(sheet.cell_value(i, 2))
    values = []
    for i in range(sheet.nrows):
        values.append(sheet.cell_value(i, 3+j))
    loc_tupples = list(zip(locations,lats, lngs, values))
    headers = loc_tupples[0]
    del loc_tupples[0]
    make_kml(loc_tupples,7,headers[3])

# for loc_tupple in loc_tupples:
#     if(loc_tupple[3] <= 10 and loc_tupple[3] > 7.5):
#         polycircle = polycircles.Polycircle(latitude=loc_tupple[1],
#                                     longitude=loc_tupple[2],
#                                     radius=70000,
#                                     number_of_vertices=36)
#         pol = kml.newpolygon(name=loc_tupple[0], outerboundaryis=polycircle.to_kml())
#         pol.style.polystyle.color = \
#                 simplekml.Color.changealphaint(200, simplekml.Color.green)
#     if(loc_tupple[3] <= 7.5 and loc_tupple[3] > 5):
#         polycircle = polycircles.Polycircle(latitude=loc_tupple[1],
#                                     longitude=loc_tupple[2],
#                                     radius=70000,
#                                     number_of_vertices=36)
#         pol = kml.newpolygon(name=loc_tupple[0], outerboundaryis=polycircle.to_kml())
#         pol.style.polystyle.color = \
#                 simplekml.Color.changealphaint(200, simplekml.Color.yellow)
#     if(loc_tupple[3] <= 5 and loc_tupple[3] > 2.5):
#         polycircle = polycircles.Polycircle(latitude=loc_tupple[1],
#                                     longitude=loc_tupple[2],
#                                     radius=70000,
#                                     number_of_vertices=36)
#         pol = kml.newpolygon(name=loc_tupple[0], outerboundaryis=polycircle.to_kml())
#         pol.style.polystyle.color = \
#                 simplekml.Color.changealphaint(200, simplekml.Color.orange)
#     if(loc_tupple[3] <= 2.5 and loc_tupple[3] > 0):
#         polycircle = polycircles.Polycircle(latitude=loc_tupple[1],
#                                     longitude=loc_tupple[2],
#                                     radius=70000,
#                                     number_of_vertices=36)
#         pol = kml.newpolygon(name=loc_tupple[0], outerboundaryis=polycircle.to_kml())
#         pol.style.polystyle.color = \
#                 simplekml.Color.changealphaint(200, simplekml.Color.red)

# kml.save("world.kml")




