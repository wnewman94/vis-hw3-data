import csv

def get_bus_stops(bus_line):
    shape_ids = set()
    with open('trips.txt') as trips:
        trips_reader = csv.reader(trips, delimiter=',')
        for row in trips_reader:
            if row[0] == bus_line:
                shape_ids.add(row[5])
    
    shape_ls = list(shape_ids)
    stop_ls = []
    with open('shapes.txt') as shapes:
        shapes_reader = csv.reader(shapes, delimiter=',')
        for row in shapes_reader:
            if row[0] in shape_ids:
                stop_ls.append(row)


    stop_ls.sort()

    return stop_ls

def writeStops(stops, bus_line):
    with open(bus_line + '.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['id','lat','lng','seq'])
        writer.writerows(stops)


stops = get_bus_stops("M8")
writeStops(stops, "M8")
