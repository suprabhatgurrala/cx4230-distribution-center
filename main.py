import engine, warehouse, package, vehicle, worker

def initialize_package_arrivals():
    """
    Method to generate package arrivals
    :return: a list of packages and their arrival times
    """
    pass

def main():
    fel = engine.FEL()
    # packages_arrivals = initialize_package_arrivals()
    # for package_arrival in package_arrivals:
    #     package, arrival_time = package_arrival
    #     event_data = (fel, package)
    #     fel.schedule(engine.Event(event_data, package), arrival_time)
    engine.run_sim(fel)

    # print stats about simulation here

main()