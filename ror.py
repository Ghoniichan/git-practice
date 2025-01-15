def count(num: int):
    for i in range(1, num+1, 2):
        print(i)
    pass

def tiger(num: int):
    for i in range(num):
        print("ROAAAAR")

def wolf(num):
    print("AWO" + ("O"*num))

count(10)
tiger(3)
wolf(10)