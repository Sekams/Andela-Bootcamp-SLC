from unittest import TestCase
from word_count import words


class TestWords(TestCase):
    """
       Test cases for the words function
    """

    # Test if the function counts one word
    def test_word_occurance1(self):
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )

    # Test if the function counts distinct words
    def test_word_occurance2(self):
        self.assertDictEqual(
            {'one': 1, 'of': 1, 'each': 1},
            words("one of each"),
            msg='should count one of each'
        )

    # Test if the function counts multiple occurrences of words
    def test_word_occurance3(self):
        self.assertDictEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            words("one fish two fish red fish blue fish"),
            msg='should count multiple occurrences'
        )

    # Test if the function counts occurrences of punctuations
    def test_word_occurance4(self):
        self.assertDictEqual(
            {'car': 1,
             ":": 2,
             'carpet': 1,
             'as': 1,
             'java': 1,
             'javascript!!&@$%^&': 1
             },
            words('car : carpet as java : javascript!!&@$%^&'),
            msg='should include punctuation'
        )

    # Test if the function counts integers and returns them as integers in the return dictionary
    def test_word_occurance5(self):
        self.assertDictEqual(
            {'testing': 2, 1: 1, 2: 1},
            words('testing 1 2 testing'),
            msg='should include numbers'
        )

    # Test if the function counts differently cased words as distinct words
    def test_word_occurance6(self):
        self.assertDictEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            words('go Go GO'),
            msg='should respect case'
        )

    # Test if the function counts international characters properly
    def test_word_occurance7(self):
        self.assertDictEqual(
            {"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "Привет!": 1},
            words('¡Hola! ¿Qué tal? Привет!'),
            msg='should count international characters properly'
        )

    # Test if the function counts multilines
    def test_word_occurance8(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\nworld'),
            msg='should not count multilines'
        )

    # Test if the function does not count tabs
    def test_word_occurance9(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\tworld'),
            msg='should not count tabs'
        )

    # Test if the function counts multiple spaces as one
    def test_word_occurance0(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello  world'),
            msg='should count multiple spaces as one'
        )
