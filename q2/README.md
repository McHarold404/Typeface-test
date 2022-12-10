### Phonetically Similar words

Using the *Double Metaphone* library to find phonetically similar words with NORMAL threshold. Please change threshold in line 46 to either STRONG/NORMAL/WEAK depending upon the strength of matching required for the use case. 

The `doublemetaphone` method returns a tuple of two characters key, which are a phonetic translation of the passed in word.

#### How to Run

`pip3 install -r requirements.txt`
`python3 phonetic.py`

#### Input Format 

`<word> <file_name>`

Assumptions: Input is given in the same line and file contains newline separated words.

#### Output

A list of words from the file which are phonetically similar to the input word.