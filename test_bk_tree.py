import unittest
from bk_tree import BKTree
from edit_distance import levenshtein_distance


class TestBKTree(unittest.TestCase):
    def setUp(self):
        self.sample_words = ["học", "hộc", "hóc", "bọc", "sách", "bàn"]
        self.tree = BKTree(levenshtein_distance)
        self.tree.build_from_list(self.sample_words)

    def test_tree_structure_6_words(self):
        self.assertEqual(self.tree.root.word, "học")
        self.assertEqual(self.tree.root.children[1].word, "hộc")
        self.assertEqual(self.tree.root.children[3].word, "sách")
        self.assertEqual(self.tree.root.children[1].children[1].word, "hóc")
        self.assertEqual(self.tree.root.children[1].children[2].word, "bọc")
        self.assertEqual(self.tree.root.children[3].children[4].word, "bàn")

    def test_search_example_6_words(self):
        results, calls = self.tree.search("họcc", max_dist=1)
        self.assertEqual([w for w, d in results], ["học"])
        self.assertEqual(calls, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
