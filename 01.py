my_list = [1, 2, 3, 4, 5]
def my_fun():
    for i in my_list:
        if i % 2 == 0:
            yield i
            print("hhh")


for j in my_fun():
    print(j)
