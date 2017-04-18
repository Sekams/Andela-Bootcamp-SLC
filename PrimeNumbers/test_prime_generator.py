from unittest import TestCase

import prime_generator


class TestPrimeGenerator(TestCase):
    def setUp(self):
        self.prime_gen = prime_generator.PrimeGenerator(1)

    def test_is_integer(self):
        self.assertIsInstance(self.prime_gen.n, int, msg="Value not an integer")

    def test_not_negative(self):
        if isinstance(self.prime_gen.n, int):
            self.assertGreater(self.prime_gen.n, 0, msg="Value not positive integer")

    def test_is_greater_than_or_equal_to_two(self):
        if isinstance(self.prime_gen.n, int):
            self.assertGreater(self.prime_gen.n, 2, msg="Value not in the prime number scope")

    def test_is_output_a_list_of_integers(self):
        self.assertTrue(any(isinstance(x, int) for x in self.prime_gen.prime_generator()), msg="Output is not a list of integers")

    def test_is_output_a_list(self):
        self.assertTrue(isinstance(self.prime_gen.prime_generator(), list), msg="Output is not a list")
