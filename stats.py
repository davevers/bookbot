def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        low_c = c.lower()
        if low_c in chars:
            chars[low_c] += 1
        else:
            chars[low_c] = 1
    return chars

def get_sorted_chars(chars_dict):
    sorted_chars = []
    for c in chars_dict:
        sorted_chars.append({"char": c, "num": chars_dict[c]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

def sort_on(items):
    return items["num"]