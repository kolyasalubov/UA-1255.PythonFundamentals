# Task 1
Zen = """
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
"""

# Task 1.1
print(Zen.split().count("better"))
print(Zen.split().count("never"))
print(Zen.split().count("is"))

# Task 1.2
print(Zen.upper())

# Task 1.3
print(Zen.replace("i", "&"))


# Task 2

# Task 2.1
number = int(input("Enter four-digit number, please - "))
num_1 = number // 1000
num_2 = (number // 100) % 10
num_3 = (number // 10) % 10
num_4 = number % 10
product = num_1 * num_2 * num_3 * num_4
print(product)

# Task 2.2
number = str(number)
print(int(number[::-1]))

# Task 2.3
#number = int("".join(sorted(list(set(number)))))
number = list(number)
number.sort()
print(int("".join(number)))


# Task 3
a = 10
b = 20
a,b = b,a
print(f"{a = } and {b = }")