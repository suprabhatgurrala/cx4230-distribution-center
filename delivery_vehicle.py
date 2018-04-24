class DeliveryVehicle:
    """
    Object to represent a delivery vehicle
    """

    def __init__(self, capacity):
        """
        Initialization function
        :param type: the type of vehicle Delivery or Transport
        :param capacity: number of packages this vehicle can transport
        """
        self.capacity = capacity
        self.package_list = []
        self.is_free = True

    def is_full(self):
        return not self.is_free

    def add_package(self, package):
        """
        param x: number of packages to add
        """

        amount_loaded = sum(item.size for item in self.package_list)

        if amount_loaded + package.size >= self.capacity:
            is_free = False

        self.package_list.append(package)
