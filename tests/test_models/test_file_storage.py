#!/usr/bin/python3
"""Test module for file storage"""
import unittest

from models.engine.file_storage import FileStorage
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """Unit tests for the instantiation of the FileStorage class"""

    def test_file_storage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_storage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_file_storage_initialization(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unit tests for the methods of FileStorage"""

    # Add your test methods for FileStorage methods here


if __name__ == "__main__":
    unittest.main()
