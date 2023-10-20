import unittest
from logic import *


class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(2, 3), 12)

    def test_2(self):
        empty_arr = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     ]
        a = [x for x in range(1, 17)]

        self.assertEqual(a, get_empty_list(empty_arr))

    def test_3(self):
        empty_arr = [[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     ]
        a = []

        self.assertEqual(a, get_empty_list(empty_arr))

    def test_4(self):
        self.assertEqual(get_index_from_number(15), (3, 2))

    def test_5(self):
        mas1 = [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                ]
        self.assertEqual(is_zero_in_mas(mas1), False)

    def test_6(self):
        mas1 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                ]
        self.assertEqual(is_zero_in_mas(mas1), True)

    def test_7(self):
        mas1 = [[1, 1, 1, 1],
                [1, 0, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                ]
        self.assertEqual(is_zero_in_mas(mas1), True)

    def test_8(self):
        mas = [[0, 0, 2, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [2, 0, 0, 4],
               ]

        pon = [[2, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [2, 4, 0, 0],
               ]
        self.assertEqual(move_left(mas), pon)

    def test_9(self):
        mas = [[2, 2, 0, 4],
               [2, 0, 4, 0],
               [0, 0, 0, 0],
               [2, 8, 8, 0],
               ]
        rez = [[4, 4, 0, 0],
               [2, 4, 0, 0],
               [0, 0, 0, 0],
               [2, 16, 0, 0],
               ]
        self.assertEqual(move_left(mas), rez)

    def test_10(self):
        mas = [[0, 0, 2, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [2, 0, 0, 4],
               ]
        rez = [[0, 0, 0, 2],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 2, 4],
               ]

        self.assertEqual(move_right(mas), rez)

    def test_11(self):
        mas = [[2, 2, 0, 4],
               [2, 0, 4, 0],
               [2, 2, 4, 4],
               [2, 8, 8, 0],
               ]
        rez = [[0, 0, 4, 4],
               [0, 0, 2, 4],
               [0, 0, 4, 8],
               [0, 0, 2, 16],
               ]
        self.assertEqual(move_right(mas), rez)

    def test_12(self):
        mas = [[2, 2, 0, 4],
               [2, 4, 4, 0],
               [4, 2, 4, 2],
               [4, 0, 0, 0],
               ]
        rez = [[4, 2, 8, 4],
               [8, 4, 0, 2],
               [0, 2, 0, 0],
               [0, 0, 0, 0],
               ]
        self.assertEqual(move_up(mas), rez)

    def test_13(self):
        mas = [[2, 2, 0, 4],
               [2, 4, 4, 0],
               [4, 2, 4, 2],
               [4, 0, 0, 0],
               ]
        rez = [[0, 0, 0, 0],
               [0, 2, 0, 0],
               [4, 4, 0, 4],
               [8, 2, 8, 2],
               ]
        self.assertEqual(move_down(mas), rez)


if __name__ == "main":
    unittest.main()
