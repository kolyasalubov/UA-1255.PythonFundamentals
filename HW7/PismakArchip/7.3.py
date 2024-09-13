def character_count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = "hello"
output = character_count(input_string)
print(output)  