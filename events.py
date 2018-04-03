class Event:
    """
    Object to handle events.
    """
    def __init__(self, timestamp, name=""):
        """
        Initializes event object
        :param event_data: data specific to the event instance
        :param event_handler: a method to handle the event, takes event_data as a paramter
        """
        self.timestamp = timestamp
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

    def __init__(self, timestamp, package):
        super().__init__(timestamp)
        self.package = package

    # schedules a process event
    def handle(self):
        pass

class Process(Event):

    def __init__(self, timestamp, worker, package):
        super().__init__(timestamp)
        self.worker = worker
        self.package = package

    # schedules either another process event or a pack event depending on
    # whether the worker made a mistake. Marks worker as free
    def handle(self):
        pass

class Pack(Event):

    def __init__(self, timestamp, vehicle, package):
        super().__init__(timestamp)
        self.vehicle = vehicle
        self.package = package

    # schedules a departure event if the vehicle is full
    def handle(self):
        pass

class Departure(Event):

    def __init__(self, timestamp, vehicle):
        super().__init__(timestamp)
        self.vehicle = vehicle

    # adds appropriate amount of time to current time, and marks vehicle as free
    def handle(self):
        pass

class Delivery(Event):

    def __init__(self, timestamp, package):
        super().__init__(timestamp)
        self.package = package

    #stats
    def handle(self):
        pass