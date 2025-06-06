def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowercase = text.lower()
    characters_num = {}
    for character in lowercase:
        if character in characters_num:
            characters_num[character] += 1
        else:
            characters_num[character] = 1
    return characters_num