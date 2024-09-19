print("Task_1")
print()
# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
#   "better", "never" and "is" in the given line

zen_of_python = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""

count_better = zen_of_python.count("better")
count_never = zen_of_python.count("never")
count_is = zen_of_python.count("is")

# print('The number of occurences of the words: \n'
#       '    "better" -', count_better, 'times, \n'
#       '    "never" -', count_never, 'times, \n'
#       '    "is" - ', count_is, 'times.')

print(f'The number of occurences of the words: \n'
      f'    "better" - {count_better} times, \n'
      f'    "never" - {count_never} times, \n'
      f'    "is" -  {count_is} times.')
print()

# - you need to display all text in uppercase (all letters in uppercase)
zen_of_python_uppercase = zen_of_python.upper()
print(f'"Zen of python" in uppercase: \n'
      f'{zen_of_python_uppercase}')
print()

# - replace all occurrences of the symbol “i” with “&”
replace_i = zen_of_python.replace("i", "&").replace("I", "&")
print(f'"Zen of python" with "&" instead of "i": \n'
      f'{replace_i}')
