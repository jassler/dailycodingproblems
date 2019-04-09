def with_division(input: list):
    result = []
    product = 1

    zeros = 0
    for x in input:
        if x is 0:
            zeros += 1
        else:
            product *= x
    
    if zeros == 0:
        for x in input:
            result.append(product / x)
    
    elif zeros == 1:
        for n in input:
            if n == 0:
                result.append(product)
            else:
                result.append(0)

    else:
        result = [0] * len(input)
    
    return result

# TODO single pass
