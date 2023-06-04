import unittest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.comparator import Comparator

class TestComparator(unittest.TestCase):
    @patch('modules.comparator.DatabaseManager')
    @patch('modules.comparator.Expander')
    @patch('modules.comparator.Generator')
    def setUp(self, MockGenerator, MockExpander, MockDatabaseManager):
        # Mock the Generator, Expander, and DatabaseManager objects in the Comparator object
        self.generator = MockGenerator()
        self.expander = MockExpander()
        self.db_manager = MockDatabaseManager()
        self.comparator = Comparator()

    def test_base_evaluation_function(self):
        # Mock the behaviors of the generator and db_manager
        self.db_manager.read.return_value = "File content"
        self.expander.base_expansion.return_value = "Expanded prompt"
        self.generator.base_generation.return_value = "0.9"

        # Test the function
        result = self.comparator.base_evaluation_function("Prompt", "Filename")

        # Assert that the score is a float
        self.assertIsInstance(result, float)

    def test_evaluate_reliability_function(self):
        # Mock the base_evaluation_function to return a specific value
        self.comparator.base_evaluation_function = MagicMock(return_value=0.9)

        # Test the function
        result = self.comparator.evaluate_reliability_function("Prompt")

        # Assert that the result is as expected
        self.assertEqual(result, 0.9)

    def test_evaluate_validity_function(self):
        # Mock the base_evaluation_function to return a specific value
        self.comparator.base_evaluation_function = MagicMock(return_value=0.9)

        # Test the function
        result = self.comparator.evaluate_validity_function("Prompt")

        # Assert that the result is as expected
        self.assertEqual(result, 0.9)

    def test_base_comparator_function(self):
        # Mock the behaviors of the generator, expander, and db_manager
        self.db_manager.read.return_value = "Prompt content"
        self.db_manager.get_latest_file.return_value = ["File1", "File2", "File3"]
        self.comparator.evaluate_reliability_function = MagicMock(return_value=0.9)
        self.comparator.evaluate_validity_function = MagicMock(return_value=0.9)
        self.expander.base_expansion.return_value = "Expanded output"
        self.generator.base_generation.return_value = "Generated input"

        # Test the function
        result = self.comparator.base_comparator_function()

        # Assert that the result is as expected
        self.assertEqual(result, "Generated input")

if __name__ == '__main__':
    unittest.main()
