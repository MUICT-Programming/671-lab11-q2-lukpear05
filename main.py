# YOUR CODE HERE
def summation(lst1, lst2):
    updated_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return updated_list

def find_min_max(lst):
    return (min(lst), max(lst))

n = int(input())

lst1 = []

for i in range(n):
    lst1.append(int(input()))

lst2 = []

for i in range(n):
    lst2.append(int(input()))

updated_list = summation(lst1, lst2)

print(updated_list)

min_max = find_min_max(updated_list)

print(min_max)
