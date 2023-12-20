str = [10, 20, 30, 40]
def func(str):
    str.append(50)
    print("insude function: ",str)

func(str)
print("Outside function: ", str)