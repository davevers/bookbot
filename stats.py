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