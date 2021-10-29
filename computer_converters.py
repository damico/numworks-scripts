#!/usr/bin/python3

in_binary_str = input("Please enter a binary string:\n")

def convert(binary_str, is_negative):
    array_len = len(binary_str)
    binary_array = []
    for e in binary_str:
        int_e = int(e)
        if int_e == 0 or int_e == 1:
            binary_array.append(int_e)
        else:
            raise Exception()
    if not is_negative:
        binary_array.reverse()
    exp = 0
    result = 0
    signal = 1
    if is_negative:
        signal = -1
        exp = 1
    for e in binary_array:
        if exp >=0:
            exp = exp * signal
        exp_calc = e*(2**exp)
        print(e,'*',2,'E',exp,'=',exp_calc)
        result = exp_calc + result
        if exp < 0:
            exp = exp - 1
        else:
            exp = exp + 1

    return result


try:
    result = 0
    split = in_binary_str.split('.')
    if len(split) > 2:
        raise Exception()
    else:
        result = convert(split[0], False)
        if len(split) == 2:
            result = result + convert(split[1], True)
    print(result)
except Exception as inst:
    print('The input is not a binary value.')
