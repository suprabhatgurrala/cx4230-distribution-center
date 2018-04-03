from random import random

import engine
from worker import Worker
from delivery_vehicle import DeliveryVehicle
from package import Package
from events import Arrival

def initialize_package_arrivals():
    """
    Method to generate package arrivals
    :return: a list of packages and their arrival times
    """
    pass

def main():
    num_workers = 10
    num_vehicles = 3
    num_packages = 500

    workers = [Worker() for i in range(num_workers)]
    vehicles = [DeliveryVehicle(200) for i in range(num_vehicles)]
    # package_arrivals = [Package() for i in range(num_packages)]

    fel = engine.FEL()
    packages_arrivals = initialize_package_arrivals()

    arrival_time = int(random.expovariate(1.0 / 7))
    # fel.schedule()
    engine.run_sim(fel)

    # print stats about simulation here

main()