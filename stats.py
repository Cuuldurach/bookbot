def get_num_words (text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_num_chars (text):
    letter_counts = {}
    lowered = text.lower()
    for letter in lowered:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_num_chars (letter_counts):
    sorted_list = []
    for char, count in letter_counts.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list