import statistics


class Warehouse:
    """
    Object to represent a warehouse
    """
    def __init__(self, workers, delivery_vehicles, transport_vehicles, max_packages):
        # Initialization function
        self.workers = workers
        self.delivery_vehicles = delivery_vehicles
        self.transport_vehicles = transport_vehicles
        self.num_packages = 0
        self.max_packages = max_packages
        self.processed_packages = []

    def get_free_workers(self):
        return [w for w in self.workers if w.is_free]

    def get_free_delivery_vehicle(self):
        return [w for w in self.delivery_vehicles if w.is_free]

    def get_free_transport_vehicle(self):
        return [w for w in self.transport_vehicles if w.is_free]

    def print_stats(self):
        print("Processed {} packages:".format(self.num_packages))
        delivery_times = []
        for p in self.processed_packages:
            if p.delivery_date is not None:
                delivery_times.append(p.delivery_date - p.arrival_date)
        avg_package_delivery_time = statistics.mean(delivery_times)
        print("Average package delivery time: {:.2f} minutes.".format(avg_package_delivery_time))
        avg_worker_idle = statistics.mean([w.idle_time for w in self.workers])
        print("{} workers were idle for an average of {:.2f} minutes.".format(len(self.workers), avg_worker_idle))

