#!/usr/bin/python3
"""
    Module contains unittetst for base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class defines tests for base model"""

    def setup(self):
        """setup method for class test"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

    def test_name(self):
        """tests model name"""
        self.assertEqual(my_model.name, "My First Model")

    def test_number(self):
        """tests model number"""
        self.assertEqual(my_model.my_number, 89)


"""
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
    type(my_model_json[key]), my_model_json[key]))
"""

if __name__ == "__main__":
    unittest.main()
