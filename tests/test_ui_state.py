import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ui_state import DEFAULT_VIEW, normalize_view, view_after_analysis


class UiStateTest(unittest.TestCase):
    def test_unknown_view_falls_back_to_assessment(self):
        self.assertEqual(normalize_view("not-a-real-view"), DEFAULT_VIEW)

    def test_analyze_moves_user_to_results_view(self):
        self.assertEqual(view_after_analysis("assessment"), "results")


if __name__ == "__main__":
    unittest.main()
