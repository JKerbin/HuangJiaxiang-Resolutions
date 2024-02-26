def modify_string(input, k):
    output = ''
    detector = ''
    for i, char in enumerate(input):
        if char in detector:
            output += '-'
        else:
            output += char
        if i >= k:
            detector = detector[1:]
        detector += char
    return output


if __name__ == '__main__':
    input_str = input('输入字符串：')
    input_k = int(input('请输入k：'))
    res = modify_string(input_str, input_k)
    print(res)
