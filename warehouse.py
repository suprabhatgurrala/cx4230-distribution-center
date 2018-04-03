import statistics


class Warehouse:
    """
    Object to represent a warehouse
    """
    def __init__(self, workers, vehicles, max_packages):
        # Initialization function
        self.workers = workers
        self.vehicles = vehicles
        self.num_packages = 0
        self.max_packages = max_packages
        self.processed_packages = []

    def get_free_workers(self):
        return [w for w in self.workers if w.is_free]

    def get_free_vehicles(self):
        return [w for w in self.vehicles if w.is_free]

    def print_stats(self):
        print("Processed {} packages:".format(self.num_packages))
        avg_package_delivery_time = statistics.mean([p.delivery_date - p.arrival_date for p in self.processed_packages])
        print("Average package delivery time: {:.2f} minutes.".format(avg_package_delivery_time))
        avg_worker_idle = statistics.mean([w.idle_time for w in self.workers])
        print("{} workers were idle for an average of {:.2f} minutes.".format(len(self.workers), avg_worker_idle))

