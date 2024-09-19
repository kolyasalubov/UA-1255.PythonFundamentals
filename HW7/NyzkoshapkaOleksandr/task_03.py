def Create_dict_from_string(word = "hello"):
   new_list =[(item, word.count(item)) for item in word]
   print (dict(new_list))
      
Create_dict_from_string()