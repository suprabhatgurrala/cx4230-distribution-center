class DeliveryVehicle:
    """
    Object to represent a delivery vehicle
    """

    def __init__(self, capacity):
        """
        Initialization function
        :param type: the type of vehicle Delivery or Transport
        :param capacity: total size value this vehicle can transport
        """
        self.capacity = capacity

        # Represents the packages currently stored in this vehicle, awaiting delivery
        self.package_list = []

        # Indicates whether this vehicle can accept more packages
        self.is_free = True

    def is_full(self):
        """
        returns whether or not this vehicle has reached capacity
        """
        return not self.is_free

    def add_package(self, package):
        """
        param x: number of packages to add
        """

        amount_loaded = sum(item.size for item in self.package_list)

        if amount_loaded + package.size >= self.capacity:
            is_free = False

        self.package_list.append(package)
