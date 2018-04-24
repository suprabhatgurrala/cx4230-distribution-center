import sys
from random import expovariate

import engine
from delivery_vehicle import DeliveryVehicle
from event_handlers import Arrival
from transportvehicle import TransportVehicle
from warehouse import Warehouse
from worker import Worker

num_workers = 10
num_vehicles = 3
max_packages = 500


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


args = getopts(sys.argv)
if '-w' in args:
    try:
        num_workers = int(args['-w'])
    except ValueError:
        print("Parameter value must be an integer. Using default value.")
if '-v' in args:
    try:
        num_vehicles = int(args['-v'])
    except ValueError:
        print("Parameter value must be an integer. Using default value.")
if '-p' in args:
    try:
        max_packages = int(args['-p'])
    except ValueError:
        print("Parameter value must be an integer. Using default value.")

print("Running simulation with {} packages, {} workers, {} vehicles.".format(max_packages, num_workers, num_vehicles))

worker_error_rate = 0.1
worker_efficiency = 10 # min

delivery_vehicle_capacity = 1000
transport_vehicle_capacity = 3000

package_arrival_interval = 7 # min

workers = [Worker(mean_mistake_prob=worker_error_rate, mean_efficiency=worker_efficiency) for i in range(num_workers)]
delivery_vehicles = []
transport_vehicles = []
for i in range(num_vehicles):
    # Assuming a fleet of vehicles has 3 delivery vehicles for every transport vehicle.
    if i % 4 == 3:
        transport_vehicles.append(TransportVehicle(transport_vehicle_capacity))
    else:
        delivery_vehicles.append(DeliveryVehicle(delivery_vehicle_capacity))

fel = engine.FEL()
warehouse = Warehouse(workers, delivery_vehicles, transport_vehicles, max_packages)
arrival_time = int(expovariate(1.0 / package_arrival_interval))
fel.schedule(Arrival(arrival_time, fel, warehouse))
engine.run_sim(fel)

# print stats about simulation here
warehouse.print_stats()
print("Simulation ran for", fel.now, "minutes")