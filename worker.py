import random

class Worker:
    """
        Object to represent a warehouse worker
        """

    def __init__(self):
        """
        Initialization function
        :param reliability: how often a warehouse worker makes a mistake that results in a package requiring rerouting
        :param efficiency: how long in minutes a worker spends routing a package on average
        :param idle_time: records how long the worker spends awaiting a package to be routed
        """

        self.reliability = random.expovariate(1.0 / .1) # .1 is the desired mean mistake probability
        if self.reliability > .95:
            self.reliability = .95
        self.efficiency = random.expovariate(1.0 / 10) # 10 minutes is the desired mean routing time

        self.idle_time = 0
        self.is_free = True
        self.last_job_timestamp = 0
