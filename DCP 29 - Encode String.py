
# 0(n)
def encode_string(s):
    temp = []
    output = []

    temp.append(s[0])

    for i in range(1, len(s)):
        print(temp)
        if s[i] != temp[-1]:
            len_temp = str(len(temp))
            output.extend([len_temp, temp[0]])
            temp = []
            temp.append(s[i])
        else:
            temp.append(s[i])

    output.extend([str(len(temp)), temp[0]])

    return ''.join(output)


def encode_string2(s):
    output = []
    count = 1

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            output.extend([str(count), s[i - 1]])
            count = 1
        else:
            count += 1
    
    output.extend([str(count), s[-1]])
    return ''.join(output)


s = 'AAAABBBCCDAA'
print(encode_string(s))
print(encode_string2(s))