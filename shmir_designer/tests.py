#!/usr/bin/python

"""
Test for shmiR application
"""
import unittest
import utils

import errors


class ShmiRTest(unittest.TestCase):
    """Tests for shmiR designer application"""
    def test_input(self):
        """Tests for check_input function"""
        tests = [
            ('acggctTggaacttctggtac', ['acggcttggaacttctggtac', '', 0, 0]),
            ('acggcttGGaacttctggtac gtaccagaagttccaagccgt', [utils.check_complementary('acggcttggaacttctggtac', 'gtaccagaagttccaagccgt')]),
            ('acggcttggAActuctggtac gtaccagaagttccaagccgt', [utils.check_complementary('acggcttggaacttctggtac', 'gtaccagaagttccaagccgt')]),
            ('acggctTggaacttctggtTT', ['acggcttggaacttctggt', '', 0, 0])]
        for list1, expected in tests:
            self.failUnlessEqual(utils.check_input(list1), expected)

    def test_input_exceptions(self):
        """Tests for check_input Exceptions"""
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('acggcttggaactuct')
        self.assertEqual(errors.len_error, str(err.exception))
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('')
        self.assertEqual(errors.len_error, str(err.exception))
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('acttctggtacTTUUUUUUuuuuuuGGG')
        self.assertEqual(errors.len_error, str(err.exception))
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('acggcttGGaacttctggtac gtaccagaagttccaagccgt '\
                'acggcttGGaacttctggtac')
        self.assertEqual(errors.error, str(err.exception))
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('acggcttGGaacttctggtac tgccgaaccttgaagaccatg')
        self.assertEqual(errors.error, str(err.exception))
        with self.assertRaises(errors.InputException) as err:
            utils.check_input('acggctTggactggtwacTT')
        self.assertEqual(errors.patt_error, str(err.exception))

    def test_check_complementary(self):
        """Tests for check_complementary function"""
        tests = [
            ('cttggaacttctggtacat', 'gtaccagaagttccaagccgt', ('cttggaacttctggtacat', 'gtaccagaagttccaagccgt', -4, 2)),

            ('cttggaacttctggtacat', 'tgtaccagaagttccaagccg', ('cttggaacttctggtacat', 'tgtaccagaagttccaagccg', -3, 1)),
            ('cttggaacttctggtacata', 'tgtaccagaagttccaagccg', ('cttggaacttctggtacata', 'tgtaccagaagttccaagccg', -3, 2)),

            ('cttggaacttctggtacatag', 'gtaccagaagttccaagcc', ('cttggaacttctggtacatag', 'gtaccagaagttccaagcc', -2, 4)),
            ('cttggaacttctggtacatag', 'tgtaccagaagttccaagcc', ('cttggaacttctggtacatag', 'tgtaccagaagttccaagcc', -2, 3)),
            ('cttggaacttctggtacatag', 'tagtaccagaagttccaagcc', ('cttggaacttctggtacatag', 'tagtaccagaagttccaagcc', -2, 2)),
            ('cttggaacttctggtacata', 'tagtaccagaagttccaagcc', ('cttggaacttctggtacata', 'tagtaccagaagttccaagcc', -2, 1)),
            ('cttggaacttctggtacat', 'tagtaccagaagttccaagcc', ('cttggaacttctggtacat', 'tagtaccagaagttccaagcc', -2, 0)),

            ('cttggaacttctggtacatgc', 'tgtaccagaagttccaagc', ('cttggaacttctggtacatgc', 'tgtaccagaagttccaagc', -1, 3)),
            ('cttggaacttctggtacatg', 'tgtaccagaagttccaagc', ('cttggaacttctggtacatg', 'tgtaccagaagttccaagc', -1, 2)),
            ('cttggaacttctggtacat', 'tgtaccagaagttccaagc', ('cttggaacttctggtacat', 'tgtaccagaagttccaagc', -1, 1)),
            ('cttggaacttctggtacat', 'atgtaccagaagttccaagc', ('cttggaacttctggtacat', 'atgtaccagaagttccaagc', -1, 0)),
            ('cttggaacttctggtacat', 'catgtaccagaagttccaagc', ('cttggaacttctggtacat', 'catgtaccagaagttccaagc', -1, -1)),


            ('acggcttggaacttctggtac', 'accagaagttccaagccgt', ('acggcttggaacttctggtac', 'accagaagttccaagccgt', 0, 2)),
            ('acggcttggaacttctggtac', 'taccagaagttccaagccgt', ('acggcttggaacttctggtac', 'taccagaagttccaagccgt', 0, 1)),
            ('acggcttggaacttctggtac', 'gtaccagaagttccaagccgt', ('acggcttggaacttctggtac', 'gtaccagaagttccaagccgt', 0, 0)),
            ('acggcttggaacttctggta', 'gtaccagaagttccaagccgt', ('acggcttggaacttctggta', 'gtaccagaagttccaagccgt', 0, -1)),
            ('acggcttggaacttctggt', 'gtaccagaagttccaagccgt', ('acggcttggaacttctggt', 'gtaccagaagttccaagccgt', 0, -2)),


            ('acggcttggaacttctggtac', 'taccagaagttccaagccg', ('acggcttggaacttctggtac', 'taccagaagttccaagccg', 1, 1)),
            ('acggcttggaacttctggtac', 'gtaccagaagttccaagccg', ('acggcttggaacttctggtac', 'gtaccagaagttccaagccg', 1, 0)),
            ('acggcttggaacttctggta', 'gtaccagaagttccaagccg', ('acggcttggaacttctggta', 'gtaccagaagttccaagccg', 1, -1)),
            ('acggcttggaacttctggt', 'gtaccagaagttccaagccg', ('acggcttggaacttctggt', 'gtaccagaagttccaagccg', 1, -2)),
            ('acggcttggaacttctggt', 'agtaccagaagttccaagccg', ('acggcttggaacttctggt', 'agtaccagaagttccaagccg', 1, -3)),

            ('acggcttggaacttctggtac', 'gtaccagaagttccaagcc', ('acggcttggaacttctggtac', 'gtaccagaagttccaagcc', 2, 0)),
            ('acggcttggaacttctggta', 'gtaccagaagttccaagcc', ('acggcttggaacttctggta', 'gtaccagaagttccaagcc', 2, -1)),
            ('acggcttggaacttctggt', 'gtaccagaagttccaagcc', ('acggcttggaacttctggt', 'gtaccagaagttccaagcc', 2, -2)),
            ('acggcttggaacttctggt', 'agtaccagaagttccaagcc', ('acggcttggaacttctggt', 'agtaccagaagttccaagcc', 2, -3)),
            ('acggcttggaacttctggt', 'gagtaccagaagttccaagcc', ('acggcttggaacttctggt', 'gagtaccagaagttccaagcc', 2, -4)),

            ('cacggcttggaacttctggta', 'gtaccagaagttccaagcc', ('cacggcttggaacttctggta', 'gtaccagaagttccaagcc', 3, -1)),
            ('cacggcttggaacttctggt', 'gtaccagaagttccaagcc', ('cacggcttggaacttctggt', 'gtaccagaagttccaagcc', 3, -2)),

            ('gcacggcttggaacttctggt', 'gtaccagaagttccaagcc', ('gcacggcttggaacttctggt', 'gtaccagaagttccaagcc', 4, -2))
            ]
        for seq1, seq2, expected in tests:
            self.failUnlessEqual(utils.check_complementary(seq1, seq2), expected)




if __name__ == '__main__':
    unittest.main()
