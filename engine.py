class FEL:
    def schedule(self, event, timestamp):
        """
        Schedules an event into the FEL.
        :param event: the event to schedule
        :param timestamp: the timestamp of the event to schedule
        """
        self.priority_queue.append((event, timestamp))
        self.priority_queue.sort(key=lambda pair: pair[1])

    def remove(self):
        """
        Removes and returns the item at the front of the FEL
        :return: the item at the front of the FEL
        """
        return self.priority_queue.pop(0)

    def peek(self):
        """
        Returns the item at the front of the FEL without removing it.
        :return: the item at the front of the FEL
        """
        if not self.is_empty():
            return self.priority_queue[0]

    def delete(self, event):
        """
        Removes and returns a specified Event object from the FEL
        :param event: the Event object to remove
        :return: the removed Event object
        """
        return self.priority_queue.remove(event)

    def is_empty(self):
        """
        :return: True if the FEL is empty, False otherwise
        """
        return len(self.priority_queue) == 0

    def __init__(self):
        self.priority_queue = []
        self.now = 0

    def to_string(self):
        string = "["

        for event, timestamp in self.priority_queue:
            string += "{" + str(event) + ", " + str(timestamp) + "},"

        string += "]"

        return string

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()


def run_sim(fel):
    """
    Executes the simulation
    :param fel: the FEL to execute
    """
    while not fel.is_empty():
        event, timestamp = fel.remove()
        fel.now = timestamp
        event.handle()