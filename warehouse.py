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

    def get_free_workers(self):
        return [w for w in self.workers if w.is_free]

    def get_free_vehicles(self):
        return [w for w in self.vehicles if w.is_free]

    def print_stats(self):
        print("Done.")