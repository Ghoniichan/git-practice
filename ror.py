def count(num: int):
    for i in range(1, num+1, 2):
        print(i)
    pass

def tiger(num: int):
    for i in range(num):
        print("ROAAAAR")

count(10)
tiger(3)