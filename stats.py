def get_num_words(words):
    return len(words.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_chars(chars_dict):
    list_chars = list(chars_dict.items())
    def sort_on(item):
        return item[1]
    list_chars.sort(key=sort_on, reverse=True)
    return list_chars

