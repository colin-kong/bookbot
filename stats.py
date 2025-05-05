def get_num_words(path_to_file):
    with open(path_to_file, 'r') as file:
        file_content = file.read()
    word_array= file_content.split()
    numword= len(word_array)
    return numword

def get_num_letters(path_to_file):
    with open(path_to_file, 'r') as file:
        file_content = file.read()
    file_content=file_content.lower()
    word_arrays= file_content.split()
    char_counts = {}
    for word in word_arrays:
        for letter in word:
            char_counts[letter] = char_counts.get(letter, 0) + 1
    #print (char_counts)

    return char_counts

def sort_report(letter_dict):
      # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each char:count pair to a dictionary and add to list
    for char, count in letter_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list by the "num" value in descending order
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list