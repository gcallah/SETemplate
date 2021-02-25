from unittest import TestCase

from sample import main

SUCCESS = 0


class SampleTestCase(TestCase):
    def test_main(self):
        self.assertTrue(main() == SUCCESS)
