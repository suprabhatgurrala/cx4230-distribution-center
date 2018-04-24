import size as package_size

class Package:
    """
    Object to represent a package
    """

    def __init__(self, priority=None, size=None, address=None):
        # Initialization function
        self.priority = priority
        self.size = package_size.numericSize(package_size.get_size())
        self.address = address
        self.arrival_date = None
        self.delivery_date = None
        self.ready_for_departure = False
