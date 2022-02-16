import unittest
from solution import convert_to_lowercase_and_split, get_unique_word_counts, get_unique_words

class TestCommonWords(unittest.TestCase):

    def test_can_lower_and_split_string(self):
        string = "Nick is A good DEVELOPER"
        result = convert_to_lowercase_and_split(string)
        expected = ['nick', 'is', 'a', 'good', 'developer']
        self.assertEqual(result, expected)
    
    def test_get_unique_words(self):
        string = "Nick is A good DEVELOPER and nick likes to play. Nick is a coder. A coder codes. Nick loves Python."
        words = convert_to_lowercase_and_split(string)
        result = get_unique_words(words)
        expected = ['nick', 'is','a','good','developer', 'and','likes','to','play.', 'coder.','coder','codes.','loves','python.']
        self.assertEqual(result, expected)
    
    def test_get_unique_word_counts(self):
        string = "nick is a good  good good good boy boy boy coder coder"
        words = convert_to_lowercase_and_split(string)
        unique = get_unique_words(words)
        result = get_unique_word_counts(unique, string)
        expected = [(1, 'nick'), (1, 'is'), (1, 'a'), (4, 'good'), (3, 'boy'), (2, 'coder')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()