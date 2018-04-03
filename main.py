from random import expovariate

import engine
from delivery_vehicle import DeliveryVehicle
from event_handlers import Arrival
from warehouse import Warehouse
from worker import Worker

num_workers = 10
num_vehicles = 3
max_packages = 500

worker_error_rate = 0.1
worker_efficiency = 10 # min

vehicle_capacity = 200

package_arrival_interval = 7 # min

workers = [Worker(mean_mistake_prob=worker_error_rate, mean_efficiency=worker_efficiency) for i in range(num_workers)]
vehicles = [DeliveryVehicle(vehicle_capacity) for i in range(num_vehicles)]
# package_arrivals = [Package() for i in range(num_packages)]

fel = engine.FEL()
warehouse = Warehouse(workers, vehicles, max_packages)
arrival_time = int(expovariate(1.0 / package_arrival_interval))
fel.schedule(Arrival(arrival_time, fel, warehouse))
engine.run_sim(fel)

# print stats about simulation here
warehouse.print_stats()