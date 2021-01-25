# ==============================
#         Information
# ==============================

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# ==============================
#         Solution
# ==============================


def matching_prefix(query, word_list):
    matched_words = []
    word_set = set(word_list)

    for word in word_set:
        if word[:2] == query:
            matched_words.append(word)
    
    return matched_words


def matching_prefix2(query, word_list):
    matched_words = []
    word_set = set(word_list)

    for word in word_set:
        if word.startswith(query):
            matched_words.append(word)
    
    return matched_words


query = 'de'
word_list = ['dog', 'deer', 'deal']

print(matching_prefix(query, word_list))


