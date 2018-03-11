import unittest
from unittest.mock import patch
import cli_dictionary

class TestDictionary(unittest.TestCase):

    def test_get_def(self):
        result = cli_dictionary.get_def("dirt")
        self.assertEqual(result[0], 'Any unclean substance, such as mud, dust, dung etc.')

    def test_get_matches(self):
        with patch('builtins.input', return_value='Y'):
            result = cli_dictionary.get_matches("tripleeee")
            self.assertEqual(result, 
            ['To make three times as great.',
            'To become three times as great.',
            'Composed of three elements or parts.',
            'In mathematics, an ordered list of three elements.'])

if __name__ == '__main__':
    unittest.main()