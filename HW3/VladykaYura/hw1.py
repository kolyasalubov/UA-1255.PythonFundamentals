import this
zen_of_python = "".join([this.d.get(c, c) for c in this.s])
zen_of_python= zen_of_python.upper()

print(zen_of_python)

count_is = zen_of_python.count("IS")
count_better = zen_of_python.count("BETTER")
count_never = zen_of_python.count("NEVER")

print(f'Number "IS": {count_is}')
print(f'Number "BETTER": {count_better}')
print(f'Number "NEVER": {count_never}')

replace_i = zen_of_python.replace('I','&')
print(replace_i)

