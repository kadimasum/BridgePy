def count_down(num):
    print(num)
    if num <= 0: return
    else: count_down(num - 1)

result = count_down(15)
print(result)