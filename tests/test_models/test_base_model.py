#!/usr/bin/python3
"""Unittest for base_model.py"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model.py"""

    def test_instantiation(self):
        """Tests instantiation of BaseModel class"""

        bm = BaseModel()
        self.assertEqual(str(type(bm)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(issubclass(type(bm), BaseModel))

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


if __name__ == "__main__":
    unittest.main()
