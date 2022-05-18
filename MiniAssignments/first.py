from itertools import combinations


class StringClass:
    # First Problem

    def __init__(self, inp):
        self.input = inp

    def length(self):
        return len(self.input)

    def list(self):
        lst = list(self.input)
        return lst


class PairsPossible(StringClass):
    # Second Problem
    def storing_pairs(self, test_list):
        self.res = list(combinations(test_list, 2))

    def displaying_pairs(self):
        print(str(self.res).replace(', ', ' '))


class SearchCommonElements:
    # Third Problem
    def common_element(self, str1, str2):
        a_set = set(str1)
        b_set = set(str2)

        if a_set & b_set:
            print(a_set & b_set)
        else:
            print("No common elements")


class EqualSumPairs:
    # forth Problem
    def pairs(self, test_list):
        summation = []
        result = [sum((int(n), int(j))) for idx, n in enumerate(test_list) for j in test_list[idx+1:]]
        print(result)
        n = len(result)
        sums = dict()

        for num in range(n):
            if result[num] in sums.keys():
                sums[result[num]] += 1
            else:
                sums[result[num]] = 1
        for num in sums:
            if sums[num] == 1:
                summation.append(num)
        print(summation)
        print(len(summation))


string1 = input("Enter a string :")
obj1 = StringClass(string1)
print(obj1.length())
lst1 = obj1.list()
print(lst1)

obj2 = PairsPossible(obj1)
obj2.storing_pairs(lst1)
obj2.displaying_pairs()

string2 = input("Enter string to compare :")
obj3 = SearchCommonElements()
obj3.common_element(string1, string2)

print('sum of pairs')
obj4 = EqualSumPairs()
obj4.pairs(lst1)
