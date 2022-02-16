def convert_to_lowercase_and_split(string):
    converted_string = string.lower().split()
    return converted_string

def get_unique_words(words: list):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

def get_unique_word_counts(unique_words: list, string):
    counts = []
    for unique_word in unique_words:
        count = 0
        for word in convert_to_lowercase_and_split(string):
            if word == unique_word:
                count +=1
        counts.append((count, unique_word))
    return counts


def get_most_common_words():
    user_input = input(' Enter text string: ')
    words = convert_to_lowercase_and_split(user_input)

    unique_words = get_unique_words(words)
        
    counts = get_unique_word_counts(unique_words, user_input)

    counts.sort()
    counts.reverse()

    for i in range(min(3, len(counts))):
        count, word = counts[i]
        print(f"{word} appears {count} times")


if __name__ == '__main__':
    get_most_common_words()