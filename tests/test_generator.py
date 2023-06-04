import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to sys.path to import Generator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.generator import Generator

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def tearDown(self):
        self.generator = None

    @patch('openai.ChatCompletion.create')
    def test_base_generation(self, mock_create):
        # Mock the response from the OpenAI API
        mock_create.return_value.choices[0].message.content = "Hello, world!"

        # Call the function with a prompt
        response = self.generator.base_generation("Hello")

        # Assert that the response matches the mock response
        self.assertEqual(response, "Hello, world!")

    # Repeat the process for other methods of the Generator class

if __name__ == '__main__':
    unittest.main()
