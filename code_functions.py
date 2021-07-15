def most_frequency(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


str1= input("Enter a string: ")
print(most_frequency (str1))



