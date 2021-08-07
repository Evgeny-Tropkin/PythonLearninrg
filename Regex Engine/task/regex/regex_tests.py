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

    def test_process_string(self):
        self.assertTrue(regex.process_string("abc", ['.', "bc"]))
        self.assertTrue(regex.process_string("abc", ['a', '.', 'c']))
        self.assertTrue(regex.process_string("abc", ["ab", '.']))
        self.assertTrue(regex.process_string("a bc", ["bc"]))
        self.assertTrue(regex.process_string(" abc", ["bc"]))
        self.assertTrue(regex.process_string("abc ", ["bc"]))
