# Carla Aleman
# CIS256 Fall 2024
# EX4 (EX 4)
import unittest
from word_guessing_game import choose_word, get_word
class MyTestCase(unittest.TestCase):
    # Test choose word method to select word from list randomly
    def test_choose_word(self):
        words = ["computer", "python", "mesa", "programming", "game"]
        assert choose_word() in words
    # Test get word to make sure output is correct
    def test_get_word(self):
        # Some letters test
        word = "programming"
        letters = {'p','a', 'g'}
        assert get_word(word, letters) == 'p__g_a____g'
        # All letters test
        word2 = "mesa"
        letters2 = {'m','e','s','a'}
        assert get_word(word2, letters2) == 'mesa'
        # No letters tests
        letters3 = {}
        assert get_word(word2, letters3) == '____'

if __name__ == '__main__':
    unittest.main()
