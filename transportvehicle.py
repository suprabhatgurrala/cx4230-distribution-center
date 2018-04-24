class TransportVehicle:
    """                                                                                                                          
    Object to represent a transport vehicle                                                                                      
    """

    def __init__(self, capacity):
        """                                                                                                                      
        Initialization function                                                                                                  
        :param capacity: number of packages this vehicle can transport                                                           
        """
        self.capacity = capacity
        self.package_list = []
        self.is_free = True

    def is_full(self):
        if len(self.package_list) == self.capacity:
            return True
        else:
            return False

    def add_package(self, package):
        """                                                                                                                      
        param x: number of packages to add                                                                                       
        """
        self.package_list.append(package)



