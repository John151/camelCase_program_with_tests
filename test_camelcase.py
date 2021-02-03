import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))

    def test_blank_or_empty(self):
        self.assertEqual('', camelCase.camel_case(''))

    # def test_single_word(self):
    #
    #
    # def test_numbers_or_punctuation(self):
    #
    #
    # def test_strings_with_newline_or_tab(self):

    def test_strings_with_whitespace(self):
        input_and_expected_outputs = {
            '    Spaces Before': 'spacesBefore',
            'Spaces after     ': 'spacesAfter',
            '  Spaces     all    over    ': 'spacesAllOver',
            '\tThere is a \t tab here': 'thereIsATabHere',
            'There is a \n newline here\n': 'thereIsANewlineHere'
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camelCase.camel_case(input_val))



