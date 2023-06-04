import unittest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.expander import Expander

class TestExpander(unittest.TestCase):
    @patch('modules.expander.DatabaseManager')
    @patch('modules.expander.Generator')
    def setUp(self, MockGenerator, MockDatabaseManager):
        # Mock the Generator and DatabaseManager objects in the Expander object
        self.generator = MockGenerator()
        self.db_manager = MockDatabaseManager()
        self.expander = Expander()

    def test_base_expansion(self):
        # Test that base_expansion correctly joins prompt parts
        result = self.expander.base_expansion(['Part 1', 'Part 2'])
        self.assertEqual(result, 'Part 1\n\nPart 2')

    @patch('modules.expander.Expander.base_expansion')
    def test_expansion_generator(self, mock_base_expansion):
        # Test that expansion_generator correctly splits expansion text
        self.generator.base_generation.return_value = 'Line 1\nLine 2'
        self.db_manager.read.return_value = 'Prompt'
        mock_base_expansion.return_value = 'Prompt\nUser Prompt'

        result = self.expander.expansion_generator('User Prompt')
        self.assertEqual(result, ['Line 1', 'Line 2'])

if __name__ == '__main__':
    unittest.main()
