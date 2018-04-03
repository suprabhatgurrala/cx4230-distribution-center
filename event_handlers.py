from random import expovariate, random
from package import Package


class Event:
    """
    Object to handle events.
    """
    def __init__(self, timestamp, fel, warehouse, name=""):
        """
        Initializes event object
        :param event_data: data specific to the event instance
        :param event_handler: a method to handle the event, takes event_data as a paramter
        """
        self.timestamp = timestamp
        self.fel = fel
        self.warehouse = warehouse
        # self.handler = event_handler
        # self.type = event_type
        self.name = name

    def handle(self):
        """
        calls the provided event handler with event_data as a parameter
        """
        pass

    def to_string(self):
        return "Event at time: " + str(self.timestamp)

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()


class Arrival(Event):
    def __init__(self, timestamp, fel, warehouse):
        super().__init__(timestamp, fel, warehouse)
        self.warehouse = warehouse

    # schedules a process event
    def handle(self):
        package = Package()
        package.arrival_date = self.timestamp
        self.warehouse.num_packages += 1
        self.fel.schedule(Process(self.timestamp + 1, self.fel, self.warehouse, package))

        # if there are more packages, schedule the next package arrival
        if self.warehouse.num_packages < self.warehouse.max_packages:
            self.fel.schedule(Arrival(self.timestamp + int(expovariate(1.0 / 7)), self.fel, self.warehouse))


class Process(Event):
    def __init__(self, timestamp, fel, warehouse, package, worker=None):
        super().__init__(timestamp, fel, warehouse)
        self.package = package
        self.warehouse = warehouse
        self.worker = worker

    # Assign a worker if there is a free one
    # schedules either another process event or a pack event depending on
    # whether the worker made a mistake. Marks worker as free
    def handle(self):
        free_workers = self.warehouse.get_free_workers()

        if len(free_workers) == 0:
            # No free workers, schedule another process event delayed by some time
            self.fel.schedule(Process(self.timestamp + 1, self.fel, self.warehouse, self.package))

        else:
            if self.worker is None:
                worker = free_workers[0]
                worker.idle_time += self.timestamp - worker.last_job_timestamp
                worker.last_job_timestamp = self.timestamp + worker.efficiency
                worker.is_free = False
            else:
                worker = self.worker

            if random() < worker.reliability:
                # Successfully processed package
                self.fel.schedule(Pack(self.timestamp + worker.efficiency, self.fel, self.warehouse, self.package, worker))
            else:
                # Did not successfully process package, reassign process to same worker
                self.fel.schedule(Process(self.timestamp + worker.efficiency, self.fel, self.warehouse, self.package, worker=worker))


class Pack(Event):
    def __init__(self, timestamp, fel, warehouse, package, worker):
        super().__init__(timestamp, fel, warehouse)
        self.warehouse = warehouse
        self.package = package
        self.worker = worker

    def handle(self):
        self.worker.is_free = True
        free_vehicles = self.warehouse.get_free_vehicles()

        # Find a free vehicle, if no vehicle is available, wait and try again
        if len(free_vehicles) == 0:
            # No free vehicles, wait an hour and try again
            # TODO: Find a better way to do this
            self.fel.schedule(Pack(self.timestamp + 60, self.fel, self.warehouse, self.package))
        else:
            vehicle = free_vehicles[0]
            # Add package to the vehicle
            vehicle.add_package(self.package)
            if vehicle.is_full():
                # Vehicle is full, Schedule a departure event and mark as not free
                vehicle.is_free = False
                self.fel.schedule(Departure(self.timestamp, self.fel, self.warehouse, vehicle))


class Departure(Event):
    def __init__(self, timestamp, fel, warehouse, vehicle):
        super().__init__(timestamp, fel, warehouse)
        self.vehicle = vehicle

    # Schedules the first delivery event after 20 min travel time
    def handle(self):
        self.fel.schedule(Delivery(self.timestamp + 20, self.fel, self.warehouse, self.vehicle))


class Delivery(Event):

    def __init__(self, timestamp, fel, warehouse, vehicle):
        super().__init__(timestamp, fel, warehouse)
        self.vehicle = vehicle

    #stats
    def handle(self):
        # Remove the first package off the package list
        package = self.vehicle.package_list.pop()
        package.delivery_date = self.timestamp

        # If there are more packages, schedule next delivery
        if len(self.vehicle.package_list) > 0:
            self.fel.schedule(Delivery(self.timestamp + 2, self.fel, self.warehouse, self.vehicle))
        else:
            # Truck is empty, send it back to warehouse
            self.fel.schedule(VehicleReturn(self.timestamp + 20, self.fel, self.warehouse, self.vehicle))


class VehicleReturn(Event):
    def __init__(self, timestamp, fel, warehouse, vehicle):
        super().__init__(timestamp, fel, warehouse)
        self.vehicle = vehicle

    def handle(self):
        self.vehicle.is_free = True