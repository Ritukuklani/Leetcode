# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".
def commonCharacterCount(s1, s2):
    my_dict = {}
    for i in range(len(s1)):
        if s1[i] not in my_dict:
            my_dict[s1[i]] = 1
        else:
            my_dict[s1[i]] += 1
    my_dict2 = {}
    for i in range(len(s2)):
        if s2[i] not in my_dict2:
            my_dict2[s2[i]] = 1
        else:
            my_dict2[s2[i]] += 1
    cc = 0
    for val in my_dict:
        if val in my_dict2:
            cc += min(my_dict[val], my_dict2[val])
    return cc

#from collections import Counter
# def commonCharacterCount(s1, s2):
#     return sum((Counter(s1) & Counter(s2)).values())