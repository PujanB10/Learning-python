import math

def get_station_data(filename: str):
    dic={}
    with open(filename) as new_file:
        for lines in new_file:
            lines=lines.replace("\n","")
            lines=lines.split(";")
            if lines[0]=="Longitude":
                continue
            dic[lines[3]]=(float(lines[0]),float(lines[1]))
    return dic
            

def distance(stations: dict, station1: str, station2: str):
    x_km=(stations[station1][0]-stations[station2][0]) * 55.26
    y_km=(stations[station1][1]-stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
  

def greatest_distance(stations: dict):
    station1=""
    station2=""
    greatest=0
    for items in stations:
        for items1 in stations:
            dist=distance(stations,items,items1)
            if dist>greatest:
                greatest=dist
                station1=items
                station2=items1
    return (station1,station2,greatest)


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    print(stations)
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
