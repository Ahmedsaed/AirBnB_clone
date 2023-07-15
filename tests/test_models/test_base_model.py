#!/usr/bin/python3
"""Unittest for base_model.py"""

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

        # def test_3_instantiation(self):
        #     """Tests instantiation of BaseModel class."""

        #     b = BaseModel()
        #     self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        #     self.assertIsInstance(b, BaseModel)
        #     self.assertTrue(issubclass(type(b), BaseModel))

        # def test_3_init_no_args(self):
        #     """Tests __init__ with no arguments."""
        #     self.resetStorage()
        #     with self.assertRaises(TypeError) as e:
        #         BaseModel.__init__()
        #     msg = "__init__() missing 1 required positional argument: 'self'"
        #     self.assertEqual(str(e.exception), msg)

        # def test_3_init_many_args(self):
        #     """Tests __init__ with many arguments."""
        #     self.resetStorage()
        #     args = [i for i in range(1000)]
        #     b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        #     b = BaseModel(*args)

        # def test_3_attributes(self):
        #     """Tests attributes value for instance of a BaseModel class."""

        #     attributes = storage.attributes()["BaseModel"]
        #     o = BaseModel()
        #     for k, v in attributes.items():
        #         self.assertTrue(hasattr(o, k))
        #         self.assertEqual(type(getattr(o, k, None)), v)

        # def test_3_datetime_created(self):
        #     """Tests if updated_at & created_at are current at creation."""
        #     date_now = datetime.now()
        #     b = BaseModel()
        #     diff = b.updated_at - b.created_at
        #     self.assertTrue(abs(diff.total_seconds()) < 0.01)
        #     diff = b.created_at - date_now
        #     self.assertTrue(abs(diff.total_seconds()) < 0.1)

        # def test_3_id(self):
        #     """Tests for unique user ids."""

        #     l = [BaseModel().id for i in range(1000)]
        #     self.assertEqual(len(set(l)), len(l))

        # def test_3_save(self):
        #     """Tests the public instance method save()."""

        #     b = BaseModel()
        #     time.sleep(0.5)
        #     date_now = datetime.now()
        #     b.save()
        #     diff = b.updated_at - date_now
        #     self.assertTrue(abs(diff.total_seconds()) < 0.01)

        # def test_3_str(self):
        #     """Tests for __str__ method."""
        #     b = BaseModel()
        #     rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        #     res = rex.match(str(b))
        #     self.assertIsNotNone(res)
        #     self.assertEqual(res.group(1), "BaseModel")
        #     self.assertEqual(res.group(2), b.id)
        #     s = res.group(3)
        #     s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        #     d = json.loads(s.replace("'", '"'))
        #     d2 = b.__dict__.copy()
        #     d2["created_at"] = repr(d2["created_at"])
        #     d2["updated_at"] = repr(d2["updated_at"])
        #     self.assertEqual(d, d2)

        # def test_3_to_dict(self):
        #     """Tests the public instance method to_dict()."""

        #     b = BaseModel()
        #     b.name = "Laura"
        #     b.age = 23
        #     d = b.to_dict()
        #     self.assertEqual(d["id"], b.id)
        #     self.assertEqual(d["__class__"], type(b).__name__)
        #     self.assertEqual(d["created_at"], b.created_at.isoformat())
        #     self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        #     self.assertEqual(d["name"], b.name)
        #     self.assertEqual(d["age"], b.age)

        # def test_3_to_dict_no_args(self):
        #     """Tests to_dict() with no arguments."""
        #     self.resetStorage()
        #     with self.assertRaises(TypeError) as e:
        #         BaseModel.to_dict()
        #     msg = "to_dict() missing 1 required positional argument: 'self'"
        #     self.assertEqual(str(e.exception), msg)

        # def test_3_to_dict_excess_args(self):
        #     """Tests to_dict() with too many arguments."""
        #     self.resetStorage()
        #     with self.assertRaises(TypeError) as e:
        #         BaseModel.to_dict(self, 98)
        #     msg = "to_dict() takes 1 positional argument but 2 were given"
        #     self.assertEqual(str(e.exception), msg)

        # def test_4_instantiation(self):
        #     """Tests instantiation with **kwargs."""

        #     my_model = BaseModel()
        #     my_model.name = "Holberton"
        #     my_model.my_number = 89
        #     my_model_json = my_model.to_dict()
        #     my_new_model = BaseModel(**my_model_json)
        #     self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

        # def test_4_instantiation_dict(self):
        #     """Tests instantiation with **kwargs from custom dict."""
        #     d = {"__class__": "BaseModel",
        #          "updated_at":
        #          datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
        #          "created_at": datetime.now().isoformat(),
        #          "id": uuid.uuid4(),
        #          "var": "foobar",
        #          "int": 108,
        #          "float": 3.14}
        #     o = BaseModel(**d)
        #     self.assertEqual(o.to_dict(), d)

        # def test_5_save(self):
        #     """Tests that storage.save() is called from save()."""
        #     self.resetStorage()
        #     b = BaseModel()
        #     b.save()
        #     key = "{}.{}".format(type(b).__name__, b.id)
        #     d = {key: b.to_dict()}
        #     self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        #     with open(FileStorage._FileStorage__file_path,
        #               "r", encoding="utf-8") as f:
        #         self.assertEqual(len(f.read()), len(json.dumps(d)))
        #         f.seek(0)
        #         self.assertEqual(json.load(f), d)

        # def test_5_save_no_args(self):
        #     """Tests save() with no arguments."""
        #     self.resetStorage()
        #     with self.assertRaises(TypeError) as e:
        #         BaseModel.save()
        #     msg = "save() missing 1 required positional argument: 'self'"
        #     self.assertEqual(str(e.exception), msg)

        # def test_5_save_excess_args(self):
        #     """Tests save() with too many arguments."""
        #     self.resetStorage()
        #     with self.assertRaises(TypeError) as e:
        #         BaseModel.save(self, 98)
        #     msg = "save() takes 1 positional argument but 2 were given"
        #     self.assertEqual(str(e.exception), msg)


if __name__ == "__main__":
    unittest.main()
