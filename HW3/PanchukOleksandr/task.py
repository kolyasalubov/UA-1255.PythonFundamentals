# Task 1
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
count_better = zen.count('better')
count_never = zen.count('never')
count_is = zen.count('is')
print(f"better = {count_better}, never = {count_never}, is = {count_is}")
print(zen.upper())
replaced_zen = zen.replace('i', '&')
print(replaced_zen)


# Task 2
number = 7528
counter = 1
for digit in str(number):
    counter *= int(digit)
print(f"Result = {counter}")

number_resersed = str(number)[::-1]
print(f"Reversed = {number_resersed}")

number_sorted = sorted(str(number))
print(f"Sorted = {''.join(number_sorted)}")

# Task 3
number_1 = 256
number_2 = 372
print(f"Before: {number_1}, {number_2}")
number_1, number_2 = number_2, number_1
print(f"After: {number_1}, {number_2}")