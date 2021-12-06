def last_indexof_max(numbers):
    if not numbers:
        return -1
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[index]:
            index = i
    return index
