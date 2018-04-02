class DeliveryVehicle:
    """                                                                                                        
    Object to represent a delivery vehicle                                                                     
    """

    def __init__(self, capacity, numPackages, average_speed):
        """                                                                                                    
        Initialization function                                                                                
        :param type: the type of vehicle Delivery or Transport                                                 
        :param capacity: number of packages this vehicle can transport                                         
        :param average_speed: average speed while transporting                                                 
        """
        self.capacity = capacity; "200 measure of storage space in truck"
        self.numPackages = numPackages; "number of packages in the truck"
        self.average_speed = average_speed;
        pass

    def addPackage(x):
        """                                                                                                    
        param x: number of packages to add                                                                     
        """
        self.numPackages += x;
        pass

    def arrive_at_warehouse_handler():
        """                                                                                                    
        Method to handle an arrive at warehouse event                                                          
        Need to: signal that vehicle is ready to be loaded                                                     
        global variable numDVehiclesAvailable: number of del. vehicles at warehouse                            
        :param params:                                                                                         
        """
        numDVehiclesAvailable++; "should probably be a function call"

        pass

    def depart_from_warehouse_handler():
        """                                                                                                    
        Method to handle a depart from warehouse event                                                         
        Scheduled elsewhere                                                                                    
        Need to: schedule first delivery (time to get there)                                                   
        :param params:                                                                                         
        """
        numDVehiclesAvailable--; "should probably be a function call"
        schedule(self.arrive_at_destination_handler(), currentTime()+2.5);

        pass
    
    def arrive_at_destination_handler():
        """                                                                                                    
        Method to handle an arrive at destination event                                                        
        Need to: schedule depart_from_dest event after constant delivery time                                  
        :param params:                                                                                         
        """
        schedule(self.depart_from_destination(), currentTime()+.2);
        self.numPackages--;

        pass


    def depart_from_destination_handler():
        """                                                                                                    
        Method to handle a depart from destination event                                                       
        Need to: schedule next delivery event if numPackages != 0, else schedule return to warehouse event     
        :param params:                                                                                         
        """
        if numPackages != 0:
            schedule(self.arrive_at_destination(), currentTime()+2.5);
        else:
            schedule(self.return_to_warehouse(), currentTime());

        pass

    def return_to_warehouse_handler():
        """                                                                                                    
        Method to handle a return to warehouse event                                                           
        Need to: schedule arrive_at_warehouse event after time to make return drive                            
        :param params:                                                                                         
        """
        schedule(self.arrive_at_warehouse(), currentTime()+15);

        pass



