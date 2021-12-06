def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    while True:
        x += 1
        if x % 5 == 0:
            return x
    return "I don't know :("
