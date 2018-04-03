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
        self.capacity = capacity # 200 measure of storage space in truck
        # self.average_speed = average_speed
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


    # def arrive_at_warehouse_handler(self):
    #     """
    #     Method to handle an arrive at warehouse event
    #     Need to: signal that vehicle is ready to be loaded
    #     global variable numDVehiclesAvailable: number of del. vehicles at warehouse
    #     :param params:
    #     """
    #     numDVehiclesAvailable++; "should probably be a function call"
    #
    #     pass
    #
    # def depart_from_warehouse_handler(self):
    #     """
    #     Method to handle a depart from warehouse event
    #     Scheduled elsewhere
    #     Need to: schedule first delivery (time to get there)
    #     :param params:
    #     """
    #     numDVehiclesAvailable--; "should probably be a function call"
    #     schedule(self.arrive_at_destination_handler(), currentTime()+2.5);
    #
    #     pass
    #
    # def arrive_at_destination_handler(self):
    #     """
    #     Method to handle an arrive at destination event
    #     Need to: schedule depart_from_dest event after constant delivery time
    #     :param params:
    #     """
    #     schedule(self.depart_from_destination(), currentTime()+.2);
    #     self.numPackages--;
    #
    #     pass
    #
    #
    # def depart_from_destination_handler(self):
    #     """
    #     Method to handle a depart from destination event
    #     Need to: schedule next delivery event if numPackages != 0, else schedule return to warehouse event
    #     :param params:
    #     """
    #     if numPackages != 0:
    #         schedule(self.arrive_at_destination(), currentTime()+2.5);
    #     else:
    #         schedule(self.return_to_warehouse(), currentTime());
    #
    #     pass
    #
    # def return_to_warehouse_handler(self):
    #     """
    #     Method to handle a return to warehouse event
    #     Need to: schedule arrive_at_warehouse event after time to make return drive
    #     :param params:
    #     """
    #     schedule(self.arrive_at_warehouse(), currentTime()+15);
    #
    #     pass


