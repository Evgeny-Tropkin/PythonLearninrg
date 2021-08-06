import unittest

import regex


class TestRegex(unittest.TestCase):
    def test_parse_reg_ex(self):
        self.assertEqual(regex.parse_reg_ex("a.bc"), ['a', '.', "bc"])
        self.assertEqual(regex.parse_reg_ex("^abc^"), ['^', "abc^"])
        self.assertEqual(regex.parse_reg_ex("$abc$"), ["$abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc$"), ['^', "abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc"), ['^', "abc"])
        self.assertEqual(regex.parse_reg_ex("abc$"), ["abc", '$'])
