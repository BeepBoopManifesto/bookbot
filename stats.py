def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowercase = text.lower()
    characters_dict = {}
    for character in lowercase:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for ch in characters_dict:
        sorted_list.append({"char": ch, "num": characters_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
