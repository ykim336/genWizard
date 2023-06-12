
import unittest
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager()

    def test_write(self):
        test_content = "This is a test"
        self.db_manager.write(1, test_content)
        latest_file_path = self.db_manager.get_latest_file(self.db_manager.path_mapping[1])
        with open(latest_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(test_content, content)

    def test_read(self):
        test_content = "This is a test for read"
        self.db_manager.write(1, test_content)
        latest_file_path = self.db_manager.get_latest_file(self.db_manager.path_mapping[1])
        filename = os.path.basename(latest_file_path)
        read_content = self.db_manager.read(1, filename)
        self.assertEqual(test_content, read_content)

    def test_delete(self):
        test_content = "This is a test for delete"
        self.db_manager.write(1, test_content)
        latest_file_path = self.db_manager.get_latest_file(self.db_manager.path_mapping[1])
        filename = os.path.basename(latest_file_path)
        self.db_manager.delete(1, filename)
        self.assertNotIn(filename, os.listdir(self.db_manager.path_mapping[1]))

    def test_edit(self):
        test_content = "This is a test for edit"
        new_content = "This is edited content"
        self.db_manager.write(1, test_content)
        latest_file_path = self.db_manager.get_latest_file(self.db_manager.path_mapping[1])
        filename = os.path.basename(latest_file_path)
        self.db_manager.edit(1, filename, new_content)
        edited_content = self.db_manager.read(1, filename)
        self.assertEqual(new_content, edited_content)

    def test_get_latest_file(self):
        test_content = "This is a test for get_latest_file"
        self.db_manager.write(1, test_content)
        latest_file_path = self.db_manager.get_latest_file(self.db_manager.path_mapping[1])
        filename = os.path.basename(latest_file_path)
        timestamp = datetime.strptime(filename.split('.')[0], "%Y%m%d%H%M%S")
        now = datetime.now()
        time_difference = now - timestamp
        self.assertLessEqual(time_difference.seconds, 1)  # the difference should be within 1 second

if __name__ == '__main__':
    unittest.main()
