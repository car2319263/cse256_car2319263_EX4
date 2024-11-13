import unittest
from word_guessing_game import choose_word, get_word
class MyTestCase(unittest.TestCase):
    def test_choose_word(self):
        words = ["computer", "python", "mesa", "programming", "game"]
        assert choose_word() in words
    def test_get_word(self):
        word = "programming"
        letters = {'p','a', 'g'}
        assert get_word(word, letters) == 'p__g_a____g'
        word2 = "mesa"
        letters2 = {'m','e','s','a'}
        assert get_word(word2, letters2) == 'mesa'

if __name__ == '__main__':
    unittest.main()
