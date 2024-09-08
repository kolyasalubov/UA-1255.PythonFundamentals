import this 

text = "".join([this.d.get(c , c)for c in this.s])

count_better = text.count("better")
count_never = text.count("never")
count_is = text.count("is")

print("Кількість 'better':" , count_better)
print("Кількість 'never':" , count_never)
print("Кількість 'is':" , count_is)

text_upper = text.upper()

text_replaced = text_upper.replace ( "I","&" )

print(text_replaced)