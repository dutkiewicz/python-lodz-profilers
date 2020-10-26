import unittest
import main


class TestIsDuplicate(unittest.TestCase):
    def test_returns_true_if_duplicate_in_haystack(self):
        haystack = ["aaa", "Abd", "Random", "duplicate", "Duplicate"]
        self.assertEqual(main.is_duplicate("duplicate", haystack), True)

    def test_returns_false_if_not_duplicate_in_haystack(self):
        haystack = ["aaa", "Abd", "unique", "duplicate", "Duplicate"]
        self.assertEqual(main.is_duplicate("unique", haystack), False)

    def test_returns_false_if_absent_in_haystack(self):
        haystack = ["aaa", "Abd", "unique", "duplicate", "Duplicate"]
        self.assertEqual(main.is_duplicate("iDontExist", haystack), False)


class TestFindDuplicates(unittest.TestCase):
    def test_returns_duplicated_entries(self):
        duplicated_source = ["a", "b", "b", "c"]
        self.assertEqual(main.find_duplicates(duplicated_source), {"b"})

    def test_returns_empty_list_when_all_entries_are_unique(self):
        duplicated_source = ["a", "b", "d", "c"]
        self.assertEqual(main.find_duplicates(duplicated_source), set())


if __name__ == "__main__":
    unittest.main()
