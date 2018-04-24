import random

mapping = {
    "ENVELOPE" : 1,
    "SMALL" : 3,
    "MEDIUM" : 6,
    "LARGE" : 10,
    "OVERSIZE" : 15
}


def numericSize(size):
    return mapping[size]


def get_size(prob=random.random()):
    if prob < .30:  # 30% chance
        return "ENVELOPE"
    elif prob < .60:  # 30% chance
        return "SMALL"
    elif prob < .80:  # 20% chance
        return "MEDIUM"
    elif prob < .95:  # 15% chance
        return "LARGE"
    else:  # 5% chance
        return "OVERSIZE"
