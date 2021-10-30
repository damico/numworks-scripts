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


def convert_from_decimal(number_str, is_fraction, in_base_str):
    result_str_array = []
    int_num = 0
    frac = 0
    try:
        int_num = int(number_str)
    except:
        frac = float(number_str)
    base = int(in_base_str)
    if not is_fraction:
        while int_num != 0:
            pre_num = int(int_num/base)
            r = int(int_num%base)
            result_str_array.append(r)
            print(int_num,'/',base,':',r)
            int_num = pre_num
        result_str_array.reverse()
    else:
        result_str_array.append('.')
        for e in range(8):
            frac = frac - int(frac)
            pre_num = (frac * base)
            i = int(pre_num)
            result_str_array.append(i)
            print("%.2f" % frac, '*', base, ':', "%.2f" % pre_num, ':', i)
            frac = pre_num
    return result_str_array


def prepare_to_decimal():
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
        print('Result:', result)
    except Exception as inst:
        print('The input is not a base '+in_base_str+' value.')


def prepare_from_decimal():
    try:
        in_number_str = input("Please enter a number:\n")
        in_base_str = input("Please enter the number base:\n")
        result = []
        split = in_number_str.split('.')
        if len(split) > 2:
            raise Exception()
        else:
            result = convert_from_decimal(split[0], False, in_base_str)
            if len(split) == 2:
                result = result + convert_from_decimal(in_number_str, True, in_base_str)
        str_result = ''
        for e in result:
            str_result = str_result + str(e)
        print('Result: ',str_result)
    except Exception as inst:
        print('The input is not a decimal value.')

def prepare_hex_to_binary():
    try:
        result = 0
        in_number_str = input("Hex number:\n")
        in_base_str = '16'
        split = in_number_str.split('.')
        if len(split) > 2:
            raise Exception()
        else:
            result = convert_to_decimal(split[0], False, in_base_str)
            if len(split) == 2:
                result = result + convert_to_decimal(split[1], True, in_base_str)

        in_number_str = str(result)
        in_base_str = '2'
        split = in_number_str.split('.')
        if len(split) > 2:
            raise Exception()
        else:
            result = convert_from_decimal(split[0], False, in_base_str)
            if len(split) == 2:
                result = result + convert_from_decimal(in_number_str, True, in_base_str)
        str_result = ''
        for e in result:
            str_result = str_result + str(e)
        print('Result:',str_result)
    except Exception as inst:
        print('The input is invalid.', type(inst))


def r():
    option = input("Options:\n[1] To Decimal\n[2] From Decimal\n[3] From Hex to Binary\n")
    if "1" in option:
        prepare_to_decimal()
    elif "2" in option:
        prepare_from_decimal()
    elif "3" in option:
        prepare_hex_to_binary()
    else:
        print("Invalid option.")

r()



