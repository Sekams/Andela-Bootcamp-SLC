from unittest import TestCase

import prime_generator


class TestPrimeGenerator(TestCase):
    def setUp(self):
        self.prime_gen = prime_generator.PrimeGenerator(3)

    def test_not_negative(self):
        self.assertGreater(self.prime_gen.n, 0, msg="Value not positive integer")

    def test_is_greater_than_two(self):
        self.assertGreater(self.prime_gen.n, 2, msg="Value not in the prime number scope")