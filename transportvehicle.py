class TransportVehicle:
    """                                                                                    
        Object to represent a transport vehicle                                            
        """

    def __init__(self, capacity, numPackages, average_speed):
        """                                                                                
        Initialization function                                                            
        :param type: the type of vehicle Delivery or Transport                             
        :param capacity: number of packages this vehicle can transport                     
        :param average_speed: average speed while transporting                             
        """
        self.capacity = capacity; "measure of storage space in truck"
        self.numPackages = numPackages; "number of packages in the truck"
        self.average_speed = average_speed;
        pass

    def addPackage(x):
        """                                                                                
        param x: number of packages to add                                                 
        """
        self.numPackages += x;
        pass


    def depart_from_warehouse_handler():
        """                                                                               \
        Method to handle a depart from warehouse event                                    \
                                                                                           
        Scheduled elsewhere                                                                
        :param params:                                                                    \
        """
        numTVehiclesAvailable--; "should be function call"
        schedule(self.arrive_at_other_warehouse_handler(), currentTime()+270);
        pass

    def arrive_at_other_warehouse_handler():
        """                                                                                
        Method to handle an arrive at warehouse event                                      
        :param params:                                                                     
        """
        self.numPackages = 0;
        schedule(self.depart_from_other_warehouse_handler(), currentTime()+45);
        pass

    def depart_from_other_warehouse_handler():
        """                                                                                
        Method to handle an depart from warehouse event                                    
        :param params:                                                                     
        """
        schedule(self.arrive_at_warehouse_handler(), currentTime()+270);
        pass

    def arrive_at_warehouse_handler():
        """                                                                                
        Method to handle an arrive at warehouse event                                     \
        Need to: signal that vehicle is ready to be loaded                                \
        global variable numTVehiclesAvailable: number of transport vehicles at warehouse  \
                                                                                           
        :param params:                                                                    \
                                                                                           
        """
        numTVehiclesAvailable++; "function call"

        pass



