import unittest
import poker_spades as PS


class MyTestCase(unittest.TestCase):
    def test_straight(self):
        # check positive case when in order
        result = PS.check_straight('S8', 'S9', 'S10')
        self.assertEqual(result, 10)
        # check non-ordered (positive case)
        result = PS.check_straight('S9', 'S8', 'S10')
        self.assertEqual(result, 10)
        # check nonconsecutive (negative case)
        result = PS.check_straight('S3', 'S9', 'S10')
        self.assertEqual(result, 0)

    def test_triple(self):
        # check positive cases
        result = PS.check_3ofa_kind('S2', 'S2', 'S2')
        self.assertEqual(result, 2)
        result = PS.check_3ofa_kind('SQ', 'SQ', 'SQ')
        self.assertEqual(result, 12)
        # check negative case
        result = PS.check_3ofa_kind('SQ', 'S6', 'SQ')
        self.assertEqual(result, 0)


    def test_flush(self):
        # check positive case
        result = PS.check_royal_flush('SQ', 'SK', 'SA')
        self.assertEqual(result, 14)
        # check straight but not royal
        result = PS.check_royal_flush('S7', 'S6', 'S8')
        self.assertEqual(result, 0)
        # check triplet, not royal
        result = PS.check_royal_flush('S10', 'S10', 'S10')
        self.assertEqual(result, 0)
        # check royal triplet
        result = PS.check_royal_flush('SA', 'SA', 'SA')
        self.assertEqual(result, 0)
        # check not straight or royal or triplet (garbage)
        result = PS.check_royal_flush('S10', 'S2', 'S8')
        self.assertEqual(result, 0)


    def test_play(self):
        # test 2 equal flushes
        result = PS.play_cards('SQ', 'SK', 'SA', 'SQ', 'SK', 'SA')
        self.assertEqual(result, 0)
        # test 2 flushes, left flush higher
        result = PS.play_cards('SQ', 'SK', 'SA', 'S9', 'S10', 'SJ')
        self.assertEqual(result, -1)
        # test 2 flushes, right flush higher
        result = PS.play_cards('S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
        self.assertEqual(result, 1)
        # test 2 straights, equal
        result = PS.play_cards('S3', 'S4', 'S5', 'S4', 'S5', 'S3')
        self.assertEqual(result, 0)
        # test 2 straights, left wins
        result = PS.play_cards('S3', 'S4', 'S5', 'S5', 'S4', 'S2')
        self.assertEqual(result, -1)
        # test 2 straights, right wins
        result = PS.play_cards('S2', 'S3', 'S4', 'S7', 'S5', 'S6')
        self.assertEqual(result, 1)
        # test left straight, right triple
        result = PS.play_cards('S3', 'S4', 'S5', 'S9', 'S9', 'S9')
        self.assertEqual(result, -1)
        # test right straight, left triple
        result = PS.play_cards('S9', 'S9', 'S9', 'S3', 'S4', 'S5')
        self.assertEqual(result, 1)
        # test 2 equal triplets
        result = PS.play_cards('S9', 'S9', 'S9', 'S9', 'S9', 'S9')
        self.assertEqual(result, 0)
        # test 2 triplets, left triplet higher
        result = PS.play_cards('S9', 'S9', 'S9', 'S3', 'S3', 'S3')
        self.assertEqual(result, -1)
        # test 2 triplets, right triplet higher
        result = PS.play_cards('S3', 'S3', 'S3', 'S9', 'S9', 'S9')
        self.assertEqual(result, 1)
        # test left triplet, right garbage
        result = PS.play_cards('S3', 'S3', 'S3', 'S9', 'S9', 'S2')
        self.assertEqual(result, -1)
        # test right triplet, left garbage
        result = PS.play_cards('S3', 'S8', 'S3', 'S2', 'S2', 'S2')
        self.assertEqual(result, 1)
        # test both garbage
        result = PS.play_cards('S3', 'S8', 'S6', 'S2', 'S9', 'S4')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
