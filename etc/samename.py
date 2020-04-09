def find_same_name(a):
    name_dict = dict()
    name_set= set()

    for x in a:
        if x in name_dict:
            name_dict[x] += 1
        else:
            name_dict[x] = 1
    
    for k in name_dict.keys():
        if name_dict[k] >= 2:
            name_set.add(k)
    
    return name_set

name = ["Tom","Jerry","Mike","Tom"]
print(find_same_name(name))
name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name))
