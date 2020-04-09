dic = { 39:'Justin', 14:'John', 67:'Mike', 105:'Summer'}

def find_name(num):
    if num in dic.keys():
        print(num, ':', dic[num])
    else:
        print("?")


find_name(39)
find_name(14)
find_name(67)
find_name(105)
find_name(17)
