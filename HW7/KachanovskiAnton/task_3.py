def count_number_of_characters(input_string):
    character_count = {}
    
    for character in input_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    return character_count

def main():
    user_input = input("Enter a string to count characters: ")
    
    result = count_number_of_characters(user_input)
    
    print(result)

if __name__ == "__main__":
    main()