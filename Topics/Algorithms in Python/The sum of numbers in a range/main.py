def range_sum(numbers, start, end):
    sum = 0
    for elem in numbers:
        if start <= elem <= end:
            sum += elem
    return sum


input_numbers = map(int, input().split()) # ...
a, b = map(int, input().split()) # ...
print(range_sum(input_numbers, a, b))