"""
Implement the  unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
def- used to create funtion
"""


def unique_in_order(iterable):
    result = []
    i = 0
    while i < len(iterable)-1:
        if iterable[i] == iterable[i+1]:
            i += 1
            continue
        result.append(iterable[i])
        i += 1
    result.append(iterable[i])
    return result

print(unique_in_order('AAAABBBCCDAABBB'))
