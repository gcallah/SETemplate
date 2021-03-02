from unittest import TestCase

import sample

SUCCESS = 0


class SampleTestCase(TestCase):
    def test_main(self):
        self.assertTrue(sample.main() == SUCCESS)
