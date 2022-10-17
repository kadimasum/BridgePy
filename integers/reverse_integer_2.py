
def reverse_int(num):
    abs_num = abs(num)
    num_char_array = list(str(abs_num))
    str_reversed_num = ''
    start = 0
    end = len(num_char_array) - 1
    while end >= start:
        str_reversed_num += num_char_array[end]
        end -=1

    int_reversed_num = int(str_reversed_num)

    if num < 0: int_reversed_num *= -1

    return int_reversed_num

result = reverse_int(25)
print(result)

