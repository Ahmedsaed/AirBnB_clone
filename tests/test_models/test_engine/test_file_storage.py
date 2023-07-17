#!/usr/bin/python3
"""
Test File Storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    def test_instances(self):
        """Test Instantiation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test function definitions"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_file_path(self):
        """Test file path"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__file_path, str)

    def test_objects(self):
        """Test objects"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__objects, dict)

    def test_all(self):
        """Test all"""
        obj = FileStorage()
        self.assertIsInstance(obj.all(), dict)

    def test_new(self):
        """Test new"""
        obj = FileStorage()
        obj.new(BaseModel())
        self.assertTrue(obj.all())

    def test_save(self):
        """Test save"""
        obj = FileStorage()
        obj.save()
        self.assertTrue(obj.all())

    def test_reload(self):
        """Test reload"""
        obj = FileStorage()
        obj.reload()
        self.assertTrue(obj.all())


if __name__ == '__main__':
    unittest.main()
