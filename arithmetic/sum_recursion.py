# 用递归实现sum函数

def sum(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0]
    return list[0] + sum(list[1:len(list)])

if __name__ == "__main__":
    list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
    print(sum(list))