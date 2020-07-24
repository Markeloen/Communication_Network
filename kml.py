import simplekml
from polycircles import polycircles
import xlrd
import sys

def make_kml(tupple_lists, range, header):
    kml = simplekml.Kml()
    counter = 0
    for tupple_list in tupple_lists:
        counter+=1
        if(tupple_list[3] <= 30000000 and tupple_list[3] > 20000000):
            polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=range * 10000,
                                        number_of_vertices=36)
            pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
            pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, simplekml.Color.red)
            
        elif(tupple_list[3] <= 20000000 and tupple_list[3] > 10000000):
            
            print(counter)
            polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=range * 10000,
                                        number_of_vertices=36)
            pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
            pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, simplekml.Color.yellow)
        elif(tupple_list[3] <= 10000000 and tupple_list[3] > 1000000):
            polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=range * 10000,
                                        number_of_vertices=36)
            pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
            pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, simplekml.Color.orange)
        elif(tupple_list[3] <= 1000000):
            polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=range * 10000,
                                        number_of_vertices=36)
            pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
            pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, simplekml.Color.green)
        else:
            polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=range * 1000,
                                        number_of_vertices=36)
            pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
            pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, simplekml.Color.black)
    kml.save(f"{header}.kml")




