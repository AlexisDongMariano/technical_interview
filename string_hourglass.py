def string_hourglass(input):
    n = len(input)
    mid = n // 2

    for i in range(n):
        if i <= mid:
            print(input[i:n-i].center(n))
        else:
            print(input[n-1-i:i+1].center(n))


input = 'strings'

string_hourglass(input)