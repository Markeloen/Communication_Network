import simplekml
from polycircles import polycircles
import xlrd
import sys

def make_kml(tupple_lists,conditions_tupple_list, rng, header):
    kml = simplekml.Kml()

    for tupple_list in tupple_lists:
        for condition in conditions_tupple_list:
            if tupple_list[3] > condition[0] and tupple_list[3] <= condition[1]:
                polycircle = polycircles.Polycircle(latitude=tupple_list[1],
                                        longitude=tupple_list[2],
                                        radius=rng * 1000,
                                        number_of_vertices=36)
                pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
                pnt = kml.newpoint()
                pnt.name = tupple_list[0]
                pnt.description = f"{header} is {tupple_list[3]}"
                pnt.coords = [(tupple_list[2],tupple_list[1])]
                if condition[2] == 'yellow':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff02e7ff")
                elif condition[2] == 'orange':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff026df7")
                elif condition[2] == 'dark_orange':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff0151b8")
                elif condition[2] == 'green':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff18bd1e")
                elif condition[2] == 'light_green':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff40f686")
                elif condition[2] == 'dark_green':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff038e5c")
                elif condition[2] == 'blue':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ffbd2b18")
                elif condition[2] == 'light_blue':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ffd77903")
                elif condition[2] == 'dark_blue':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff5c0b0a")
                elif condition[2] == 'light_purple':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "fffb58a8")
                elif condition[2] == 'purple':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "fff7278d")
                elif condition[2] == 'pink':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ffd400ff")
                elif condition[2] == 'dark_red':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff480595")
                elif condition[2] == 'red':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff0c0cff")
                elif condition[2] == 'black':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff000000")
                elif condition[2] == 'gray':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff7a7a7d")
                elif condition[2] == 'white':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ffffffff")
                    
                elif condition[2] == 'brown':
                    pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200, "ff214365")
        # if(tupple_list[3] <= 30000000 and tupple_list[3] > 20000000):
        #     polycircle = polycircles.Polycircle(latitude=tupple_list[1],
        #                                 longitude=tupple_list[2],
        #                                 radius=range * 10000,
        #                                 number_of_vertices=36)
        #     pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
        #     pol.style.polystyle.color = \
        #             simplekml.Color.changealphaint(200, simplekml.Color.red)
            
        # elif(tupple_list[3] <= 20000000 and tupple_list[3] > 10000000):
            
        #     print(counter)
        #     polycircle = polycircles.Polycircle(latitude=tupple_list[1],
        #                                 longitude=tupple_list[2],
        #                                 radius=range * 10000,
        #                                 number_of_vertices=36)
        #     pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
        #     pol.style.polystyle.color = \
        #             simplekml.Color.changealphaint(200, simplekml.Color.yellow)
        # elif(tupple_list[3] <= 10000000 and tupple_list[3] > 1000000):
        #     polycircle = polycircles.Polycircle(latitude=tupple_list[1],
        #                                 longitude=tupple_list[2],
        #                                 radius=range * 10000,
        #                                 number_of_vertices=36)
        #     pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
        #     pol.style.polystyle.color = \
        #             simplekml.Color.changealphaint(200, simplekml.Color.orange)
        # elif(tupple_list[3] <= 1000000):
        #     polycircle = polycircles.Polycircle(latitude=tupple_list[1],
        #                                 longitude=tupple_list[2],
        #                                 radius=range * 10000,
        #                                 number_of_vertices=36)
        #     pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
        #     pol.style.polystyle.color = \
        #             simplekml.Color.changealphaint(200, simplekml.Color.green)
        # else:
        #     polycircle = polycircles.Polycircle(latitude=tupple_list[1],
        #                                 longitude=tupple_list[2],
        #                                 radius=range * 1000,
        #                                 number_of_vertices=36)
        #     pol = kml.newpolygon(name=tupple_list[0], outerboundaryis=polycircle.to_kml())
        #     pol.style.polystyle.color = \
        #             simplekml.Color.changealphaint(200, simplekml.Color.black)
    kml.save(f"{header}.kml")




