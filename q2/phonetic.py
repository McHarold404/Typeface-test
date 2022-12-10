from metaphone import doublemetaphone
from enum import Enum

class Threshold(Enum):
    WEAK = 0
    NORMAL = 1
    STRONG = 2

def double_metaphone(value):
    # print(doublemetaphone(value))
    return doublemetaphone(value)

def double_metaphone_compare(tuple1, tuple2, threshold):
    '''
    (Primary Key = Primary Key) = Strongest Match
    (Secondary Key = Primary Key) = Normal Match
    (Primary Key = Secondary Key) = Normal Match
    (Alternate Key = Alternate Key) = Minimal Match

    Performs all the higher thresholds
    For example, for Normal threshold, returns true if either Normal or Strong is satsified
    '''
    if tuple1[0] == tuple2[0]:
        return True
    if threshold == Threshold.NORMAL or threshold == Threshold.WEAK:
        if tuple1[0] == tuple2[1] or tuple1[1] == tuple2[0]:
            return True
    if threshold == Threshold.WEAK:
        if tuple1[1] == tuple2[1]:
            return True
    return False

# input format (in same line): <word> <file_name>
input_word, file_name = input().split()
input_unicode = input_word #.decode('utf-8') # decode to UNICODE if necessary
input_metaphone_value = double_metaphone(input_unicode)

words = open(file_name).read().split()
# print(words)

ans = []
for w in words:
    unicode_of_word = w # str(w, 'utf-8')
    word_metaphone_value = double_metaphone(unicode_of_word)

    if double_metaphone_compare(input_metaphone_value, word_metaphone_value, Threshold.NORMAL):
        ans.append(w)

print(ans)