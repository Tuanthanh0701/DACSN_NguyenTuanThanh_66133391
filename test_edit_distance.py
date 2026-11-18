import unittest
from edit_distance import levenshtein_distance, weighted_damerau_levenshtein

class TestEditDistance(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(levenshtein_distance("học", "học"), 0)

    def test_empty_strings(self):
        self.assertEqual(levenshtein_distance("", "abc"), 3)
        self.assertEqual(levenshtein_distance("abc", ""), 3)

    def test_hand_calculated_pairs(self):
        # Ví dụ 1 trong báo cáo: "hocj" -> "học" (thay o->ọ, xóa j => khoảng cách = 2)
        self.assertEqual(levenshtein_distance("hocj", "học"), 2)
        
        # Ví dụ thực hành: "ca" -> "cá" (thay a->á => khoảng cách = 1)
        self.assertEqual(levenshtein_distance("ca", "cá"), 1)
        
        # Ví dụ khác: "mèo" -> "mẹ" (thay è->ẹ, xóa o => khoảng cách = 2)
        self.assertEqual(levenshtein_distance("mèo", "mẹ"), 2)

    def test_weighted_and_transposition(self):
        # "hocj" -> "học" có trọng số (o->ọ = 0.5, xóa j = 1.0 => 1.5)
        self.assertEqual(weighted_damerau_levenshtein("hocj", "học"), 1.5)
        
        # Ví dụ 2 trong báo cáo: lỗi đảo phím "ngờưi" -> "người" (hoán vị = 0.5)
        self.assertEqual(weighted_damerau_levenshtein("ngờưi", "người"), 0.5)

if __name__ == "__main__":
    unittest.main()
