def reverse_string(input):
    length = len(input)

    if type(input) != str:
        return 'input is not a string'
    
    if not length:
        return 'string is empty'

    if length == 1:
        return input

    
    iterations = length // 2
    output = []
    output[:] = input

    for i in range(iterations):
        temp = output[i]
        output[i] = output[(length - 1) - i]
        output[(length - 1) - i] = temp
    
    return ''.join(output)


def reverse_string2(input):
    output = []

    for c in range(len(input) - 1, -1, -1):
        output.append(input[c])
    
    return ''.join(output)


def reverse_string3(input):
    reversed_list = [c for c in input]
    reversed_list.reverse()
    return ''.join(reversed_list)

def reverse_string4(input):
    return ''.join(reversed(input))


input = 'gnoD si eman ym iH'

print(reverse_string(input))
print(reverse_string2(input))
print(reverse_string3(input))
print(reverse_string4(input))
