import warehouse
import main


class Package:
    """
    Object to represent a package
    """

    def __init__(self, priority, size, address):
        # Initialization function
        self.priority = priority
        self.size = size
        self.address = address
        self.arrival_date = None
        self.delivery_date = None
        self.ready_for_departure = False


def sort_package_handler(params):
    """
    Method to handle a sort package event
    :param params: list
    """
    p = params[0]  # type: Package
    w = params[1]  # type: warehouse.Warehouse
    p.arrival_date = params[2]
    if p.priority == 1:
        p.delivery_date = p.arrival_date + 86400
    elif p.priority == 2:
        p.delivery_date = p.arrival_date + 172800
    elif p.priority == 7:
        p.delivery_date = p.arrival_date +  604800

    if w.inJurisdiction(p.address):
        w.addDeliveryPackage(p)
    else:
        for war in main.warehouses:
            if war.inJurisdiction(p.address):
                w.addTransferPackage(p, war)
                break

#
# def sort_package_next_day_handler(params):
#     """
#     Method to handle a sort next day package event
#     :param params:
#     """
#     pass
#
#
# def sort_package_two_day_handler(params):
#     """
#     Method to handle a sort two day package event
#     :param params:
#     """
#     pass
#
#
# def sort_package_seven_day_handler(params):
#     """
#     Method to handle a sort seven day package event
#     :param params:
#     """
#     pass

#
# def ready_for_departure_handler(params):
#     """
#     Method to handle a ready for departure event
#     :param params:
#     """
#     package = params[0]
#     package.ready_for_departure = True
#
#
# def depart_for_warehouse(params):
#     """
#     Method to handle a depart for warehouse event
#     :param params:
#     """
#
#
# def depart_for_delivery(params):
#     """
#     Method to handle a depart for warehouse event
#     :param params:
#     """
