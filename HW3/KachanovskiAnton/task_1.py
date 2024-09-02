zen_of_python = """
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
"""

number_of_occurrences_of_the_word_better = zen_of_python.count("better")
number_of_occurrences_of_the_word_never = zen_of_python.count("never")
number_of_occurrences_of_the_word_is = zen_of_python.count("is")

all_text_in_uppercase = zen_of_python.upper()

first_symbol_string = "i"
second_symbol_string = "&"
replace_all_occurrences_of_the_symbol = zen_of_python.replace(first_symbol_string, second_symbol_string)

print("""\nNumber of occurrences of the words "better" - """, number_of_occurrences_of_the_word_better, """\nNumber of occurrences of the words "never" - """, number_of_occurrences_of_the_word_never, """\nNumber of occurrences of the words "is" - """, number_of_occurrences_of_the_word_is)
print("\nDisplay of all text in uppercase:", all_text_in_uppercase)
print("""\nDisplay of all replaced symbols "i" with "&": """, replace_all_occurrences_of_the_symbol)