# coding=utf-8

dist1 = {"key1": "word1", "key2": "word2"}
dist2 = sorted(dist1,reverse=True)
print dist2

tuple1 = (1,2,3,4)
tuple2 = sorted(tuple1,reverse=True)
print tuple2

str1 = "sdfsfswqb"
str2 = sorted(str1,reverse=True)
print type(str2)


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sort the words."""
    sorted_words2 = sorted(words)
    print sorted_words2
    return sorted_words2


def print_first_word(words):
    """Prints the first word after popping it off."""
    print words
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)