#!/usr/bin/python3
"""Unittest for base_model.py"""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model.py"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.clearStorageSystem()
        pass

    def clearStorageSystem(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}

        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of BaseModel class"""
        bm = BaseModel()
        self.assertEqual(str(type(bm)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(issubclass(type(bm), BaseModel))

    def test_init_with_many_args(self):
        """Tests instantiation with many kwargs"""
        self.clearStorageSystem()
        bm = BaseModel(1, 2, 3, 4, 5, 6, 7, 8, 9)
        bm2 = BaseModel([i for i in range(1000)])

        self.assertEqual(str(type(bm)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm, BaseModel)

    def test_init_with_many_kwargs(self):
        """Tests instantiation with many kwargs"""
        self.clearStorageSystem()
        bm = BaseModel(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
        bm2 = BaseModel(**{'a': 1, 'b': 2, 'c': 3, 'd': 4})

        self.assertEqual(str(type(bm)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm, BaseModel)

    def test_attributes(self):
        """Tests attributes"""
        base_model_attributes = storage.attributes()["BaseModel"]
        bm = BaseModel()
        for k, v in base_model_attributes.items():
            self.assertTrue(hasattr(bm, k))
            self.assertEqual(type(getattr(bm, k, None)), v)

    def test_id(self):
        """Tests id attribute"""

        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertIsInstance(bm.id, str)

    def test_created_at(self):
        """Tests created_at attribute"""

        bm = BaseModel()
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""

        bm = BaseModel()
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """Tests save method"""

        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_str(self):
        """Tests __str__ method"""

        bm = BaseModel()
        bm_str = bm.__str__()
        self.assertEqual(bm_str,
                         "[BaseModel] ({}) <{}>".format(bm.id, bm.__dict__))

    def test_to_dict(self):
        """Tests to_dict method"""

        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)

    def test_init_from_dict(self):
        """Tests init from dictionary"""

        bm = BaseModel()
        bm_dict = bm.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertEqual(bm.id, bm2.id)
        self.assertEqual(bm.created_at, bm2.created_at)
        self.assertEqual(bm.updated_at, bm2.updated_at)
        self.assertEqual(bm.__dict__, bm2.__dict__)

    def test_FileStorage(self):
        """Tests FileStorage class"""
        self.clearStorageSystem()
        c = BaseModel()
        c.save()
        file_content = {f"{type(c).__name__}.{c.id}": c.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r") as f:
            self.assertEqual(len(f.read()), len(json.dumps(file_content)))
            f.seek(0)
            self.assertEqual(json.loads(f.read()), file_content)

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.clearStorageSystem()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.clearStorageSystem()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == "__main__":
    unittest.main()
