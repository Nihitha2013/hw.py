def s(i):
    list = []

    for n in i:
        list.append(n** 2)
    return list

numbers = [13,37,78,56,2]
print(s(numbers))