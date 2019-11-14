import csv

def get_bus_stops(bus_line):
    stop_ids = set()
    with open('stop_times.txt') as trips:
        trips_reader = csv.reader(trips, delimiter=',')
        i = 0
        for row in trips_reader:
            if row[3] == 'stop_id':
                continue
            if i == 43:
                break
            stop_ids.add(row[3])
            i += 1

    stop_ls = []
    with open('stops.txt') as shapes:
        shapes_reader = csv.reader(shapes, delimiter=',')
        for row in shapes_reader:
            if row[0] in stop_ids:
                stop_ls.append(row)


    return stop_ls

def writeStops(stops, bus_line):
    with open(bus_line + '_stops.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['id','lat','lng','seq'])
        writer.writerows(stops)

stops = get_bus_stops("M8")
writeStops(stops, "M8")
