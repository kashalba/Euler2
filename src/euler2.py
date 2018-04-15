#!/bin/python3

import unittest

def fibs(n):
    fib_nums = [0, 1]
    while True:
        last = sum(fib_nums[-2:])
        if (last >= n):
            break
        fib_nums.append(last)
    return fib_nums

def sum_even_fibs(n):
    return (sum([i for i in fibs(n) if i % 2 == 0 ]))

class TestEvenFibsTotalMethods(unittest.TestCase):

    def test_zero_should_return_zero(self):
        self.assertEqual(0, sum_even_fibs(0))

    def test_one_should_return_zero(self):
        self.assertEqual(0, sum_even_fibs(1))

    def test_two_should_return_zero(self):
        self.assertEqual(0, sum_even_fibs(2))

    def test_three_should_return_two(self):
        self.assertEqual(2, sum_even_fibs(3))

    def test_ten_should_return_ten(self):
        self.assertEqual(10, sum_even_fibs(10))

if __name__ == '__main__':
    unittest.main()