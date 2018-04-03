from random import expovariate

import engine
from delivery_vehicle import DeliveryVehicle
from event_handlers import Arrival
from warehouse import Warehouse
from worker import Worker

num_workers = 10
num_vehicles = 3
max_packages = 500

workers = [Worker() for i in range(num_workers)]
vehicles = [DeliveryVehicle(200) for i in range(num_vehicles)]
# package_arrivals = [Package() for i in range(num_packages)]

fel = engine.FEL()
warehouse = Warehouse(workers, vehicles, max_packages)
arrival_time = int(expovariate(1.0 / 7))
fel.schedule(Arrival(arrival_time, fel, warehouse))
engine.run_sim(fel)

# print stats about simulation here
warehouse.print_stats()