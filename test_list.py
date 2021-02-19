import unittest


class TestListMethods(unittest.TestCase):
	def test_liubov_peleshenko_fi_94(self):
		list [1, 2, 3, 4, 5, 6]
		self.assertEqual(swap_first_last_elements(list),[6, 2, 3, 4, 5, 1])

    def test_liubov_peleshenko_fi_94(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
