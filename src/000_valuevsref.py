def mult(a):
    for idx in range(len(a)):
        a[idx] *= 2


my_list = [1, 2, 3, 4]

mult(my_list)
print(my_list)  # [2, 4, 6, 8]


def rename(a):
    a = None


rename(my_list)
print(my_list)  # still [2, 4, 6, 8]


def mult_one(num):
    num *= 2
    return num


x = 5
mult_one(x)
print(x)  # 5
print(mult_one(x))  # 10
