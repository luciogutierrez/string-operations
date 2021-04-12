print(bag_of_words)
term_freq = []
for row in new_corpus:
    word_freq = []
    for word in bag_of_words:
        num_ocurrences = row.count(word)
        word_freq.append(num_ocurrences)
    term_freq.append(word_freq)
print(term_freq)
