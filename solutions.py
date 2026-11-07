# Question 1: Multiply all items in a list
def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

sample_list = [2, 3, 6]
print("Question 1 - Result:", multiply_list(sample_list))


# Question 2: Sort list of tuples by last element
def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Question 2 - Result:", sort_by_last_element(sample))


# Question 3: Combine two dictionaries by adding values for common keys
def combine_dicts(d1, d2):
    result = dict(d1)
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print("Question 3 - Result:", combine_dicts(d1, d2))


# Question 4: Generate dictionary with (i, i*i) for 1..n
def square_dict(n):
    return {i: i * i for i in range(1, n + 1)}

n = 8
print("Question 4 - Result:", square_dict(n))


# Question 5: Sort a tuple by its float element (descending by float value)
def sort_tuple_by_float(tuples_list):
    return sorted(tuples_list, key=lambda x: float(x[1]), reverse=True)

lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print("Question 5 - Result:", sort_tuple_by_float(lst))


# Question 6: Set operations
# Create a set
my_set = {0, 1, 2, 3, 4}
print("Question 6 - Created set:", my_set)

# Iteration over set
print("Question 6 - Iteration:")
for item in my_set:
    print(item, end=" ")
print()

# Add members and remove items
my_set.add(5)
my_set.update([6, 7])
print("After adding:", my_set)
my_set.discard(3)
my_set.remove(0)
print("After removing:", my_set)
