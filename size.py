from enum import Enum
import random

class Size(Class):
    cls.mapping = {
        "ENVELOPE" : 1,
        "SMALL" : 3,
        "MEDIUM" : 6,
        "LARGE" : 10,
        "OVERSIZE" : 15
    }


    def numericSize(cls, size):
        cls.mapping[size]

    def getSize(cls, prob=random.random()):
        if prob < .30: # 30% chance
            return "ENVELOPE"
        elif prob < .60: # 30% chance
            return "SMALL"
        elif prob < .80: # 20% chance
            return "MEDIUM"
        elif  prob < .95 # 15% chance
            return "LARGE"
        else: # 5% chance
            return "OVERSIZE"
