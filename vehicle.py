class Vehicle:
    """
        Object to represent a vehicle
        """

    def __init__(self, type, capacity, average_speed):
        """
        Initialization function
        :param type: the type of vehicle Delivery or Transport
        :param capacity: number of packages this vehicle can transport
        :param average_speed: average speed while transporting
        """

        # If it makes more sense to make seperate classes for Delivery and Transport vehicles, feel free to split them
        pass


def arrive_at_warehouse_handler(params):
    """
    Method to handle an arrive at warehouse event
    :param params:
    """
    pass


def depart_from_warehouse_handler(params):
    """
    Method to handle an depart from warehouse event
    :param params:
    """
    pass


def arrive_at_destination_handler(params):
    """
    Method to handle an arrive at destination event
    :param params:
    """
    pass


def depart_from_destination_handler(params):
    """
    Method to handle a depart from destination event
    :param params:
    """
    pass

def return_to_warehouse_handler(params):
    """
    Method to handle a return to warehouse event
    :param params:
    """
    pass