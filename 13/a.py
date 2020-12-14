def calculateDepartureDelta(curr_time, bus):
    return (((curr_time // bus) + 1) * bus) - curr_time

def a(input):
    curr_time = int(input[0])
    buses = [ int(bus) for bus in input[1].split(',') if bus != 'x' ]
    min_bus = None
    for bus in buses:
        t = calculateDepartureDelta(curr_time, bus)
        if not min_bus or t < calculateDepartureDelta(curr_time, min_bus):
            min_bus = bus
    return min_bus * calculateDepartureDelta(curr_time, min_bus)
