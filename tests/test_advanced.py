# -*- coding: utf-8 -*-

from .context import hello_world_pyautogui

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(hello_world_pyautogui.hmm())


if __name__ == '__main__':
    unittest.main()
