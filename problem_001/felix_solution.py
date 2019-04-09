def naive(numbers: list, sums_to: int) -> bool:
    for i in range(0, len(numbers[:-1])):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sums_to:
                return True
    return False

def single_pass_with_sort(numbers: list, sums_to: int) -> bool:
    numbers.sort()
    start, end = 0, len(numbers) - 1

    while start < end:
        if numbers[start] + numbers[end] == sums_to:
            return True
        
        while numbers[start] + numbers[end] < sums_to:
            start += 1
        
        while numbers[start] + numbers[end] > sums_to:
            end -= 1

    return False
