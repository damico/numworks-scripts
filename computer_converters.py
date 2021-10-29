#!/usr/bin/python3


def switch_base(base):
    switcher = {
        "2": "01",
        "8": "01234567",
        "10": "0123456789",
        "16": "0123456789ABCDEF"
    }
    return switcher.get(base, "Invalid base")


def convert_to_decimal(number_str, is_negative, in_base_str):
    array_len = len(number_str)
    number_array = []
    int_base = int(in_base_str)
    for e in number_str.upper():
        base_elements_array = switch_base(in_base_str)
        if e not in base_elements_array:
            raise Exception()
        else:
            number_array.append(base_elements_array.index(e))

    if not is_negative:
        number_array.reverse()
    exp = 0
    result = 0
    signal = 1
    if is_negative:
        signal = -1
        exp = 1
    for e in number_array:
        if exp >=0:
            exp = exp * signal
        exp_calc = e*(int_base**exp)
        print(e,'*',int_base,'E',exp,'=',exp_calc)
        result = exp_calc + result
        if exp < 0:
            exp = exp - 1
        else:
            exp = exp + 1

    return result


def main():
    try:
        in_number_str = input("Please enter a number:\n")
        in_base_str = input("Please enter the number base:\n")
        result = 0
        split = in_number_str.split('.')
        if len(split) > 2:
            raise Exception()
        else:
            result = convert_to_decimal(split[0], False, in_base_str)
            if len(split) == 2:
                result = result + convert_to_decimal(split[1], True, in_base_str)
        print(result)
    except Exception as inst:
        print('The input is not a binary value.', type(inst))


def prepare_from_decimal():
    try:
        in_number_str = input("Please enter a number:\n")
        in_base_str = input("Please enter the number base:\n")
        result = 0
        split = in_number_str.split('.')
        if len(split) > 2:
            raise Exception()
        else:
            result = convert_to_decimal(split[0], False, in_base_str)
            if len(split) == 2:
                result = result + convert_to_decimal(split[1], True, in_base_str)
        print(result)
    except Exception as inst:
        print('The input is not a binary value.', type(inst))


main()

