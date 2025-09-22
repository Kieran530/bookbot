def get_word_count(text):
    count=len(text.split())
    return count


def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item["num"]


def sort_dict(dict):
    sorted_list = []


    for key, value in dict.items():
        sorted_list.append({"char":key,"num":value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


        
        

