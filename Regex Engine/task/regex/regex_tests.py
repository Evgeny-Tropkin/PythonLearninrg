import unittest

import regex


class TestRegex(unittest.TestCase):
    def test_parse_reg_ex(self):
        #  tests for Stage 3
        self.assertEqual(regex.parse_reg_ex("a.bc"), ['a', '.', "bc"])
        #  tests for Stage 4
        self.assertEqual(regex.parse_reg_ex("^abc^"), ['^', "abc^"])
        self.assertEqual(regex.parse_reg_ex("$abc$"), ["$abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc$"), ['^', "abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc"), ['^', "abc"])
        self.assertEqual(regex.parse_reg_ex("abc$"), ["abc", '$'])

    def test_process_string(self):
        #  tests for Stage 3
        self.assertTrue(regex.process_string("abc", ['.', "bc"]))
        self.assertTrue(regex.process_string("abc", ['a', '.', 'c']))
        self.assertTrue(regex.process_string("abc", ["ab", '.']))
        self.assertTrue(regex.process_string("a bc", ["bc"]))
        self.assertTrue(regex.process_string(" abc", ["bc"]))
        self.assertTrue(regex.process_string("abc ", ["bc"]))
        #  tests for Stage 4
        self.assertTrue(regex.process_string("abc", ['^', "ab"]))
        self.assertTrue(regex.process_string("abc", ["bc", '$']))
        self.assertTrue(regex.process_string("abc", ['^', "abc", '$']))
        self.assertTrue(regex.process_string("become", ['^', "be"]))
        self.assertFalse(regex.process_string("to be", ['^', "be"]))
        self.assertTrue(regex.process_string("section", ["tion", '$']))
        self.assertFalse(regex.process_string("sections", ["tion", '$']))
