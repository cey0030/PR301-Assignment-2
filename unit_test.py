from fileHandler import PrintClass
import unittest
from validator import Validator
from controller import Controller


class TestDataExtraction(unittest.TestCase):
    # Clement
    def setUp(self):
        self.test_class = PrintClass()
        self.validator = Validator()

    def test_get_class_name_normal(self):
        list_1 = ['class a {\n', '    n : String\n', '    add()\n', '}\n']
        self.assertEqual(self.test_class.get_class_name(list_1), 'a')

    def test_get_class_name_none(self):
        list_2 = ['class  {\n', '    n : String\n', '    add()\n', '}\n']
        self.assertEqual(self.test_class.get_class_name(list_2), '')

    def test_get_class_name_gone(self):
        list_3 = ['    name : String\n', '    add_attributes()\n', '}\n']
        self.assertIsNone(self.test_class.get_class_name(list_3))

    def test_validate_attribute_name_true_attribute(self):
        self.assertTrue(self.validator.validate_attribute_name("attribute"))

    def test_validate_attribute_name_true_clement(self):
        self.assertTrue(self.validator.validate_attribute_name("clement"))

    def test_validate_attribute_name_false_mixed(self):
        self.assertFalse(self.validator.validate_attribute_name("<clement"))

    def test_validate_attribute_name_false_mixed2(self):
        self.assertFalse(self.validator.validate_attribute_name("??i"))

    def test_validate_attribute_name_false_special(self):
        self.assertFalse(self.validator.validate_attribute_name("break"))

    def test_validate_attribute_name_false_special2(self):
        self.assertFalse(self.validator.validate_attribute_name("pass"))

    def test_validate_attribute_name_false_number(self):
        self.assertFalse(self.validator.validate_attribute_name(42))

    def test_validate_attribute_name_false_float(self):
        self.assertFalse(self.validator.validate_attribute_name(3.14))

    def test_validate_attribute_name_false_long(self):
        self.assertFalse(self.validator.validate_attribute_name(
            '--------------------------------------'
            '-------------------------------------'
        ))

    # Luna
    def test_validate_class_name_is_true(self):
        validator = Validator()
        result_1 = validator.validate_class_name("Name")
        result_2 = validator.validate_class_name("ClassName")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_class_name_using_special_char(self):
        validator = Validator()
        result = validator.validate_class_name("Name$%^&")
        self.assertFalse(result)

    def test_validate_class_name_using_lower(self):
        validator = Validator()
        result = validator.validate_class_name("name")
        self.assertFalse(result)

    def test_validate_class_name_start_with_num(self):
        validator = Validator()
        result = validator.validate_class_name("123Name")
        self.assertFalse(result)

    def test_read_word_file(self):
        print_class = PrintClass()
        actual = print_class.read_word_file("test2.docx")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual)

    def test_read_txt_file(self):
        print_class = PrintClass()
        actual = print_class.read_txt_file("test2.txt")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual)

    def test_load_word_file(self):
        controller = Controller()
        actual = controller.load_file("test2.docx")
        expected = [['class ToyBox {\n', '    name : String\n', '}\n'],
                    ['class Toy {\n', '}\n']]
        self.assertEqual(expected, actual)

    def test_load_txt_file(self):
        controller = Controller()
        actual = controller.load_file("test2.txt")
        expected = [['class ToyBox {\n', '    name : String\n', '}\n'],
                    ['class Toy {\n', '}\n']]
        self.assertEqual(expected, actual)

    def test_load_file_not_found_exception(self):
        controller = Controller()
        actual = controller.load_file("C:\\Users\\Luna\\ICT\\test2.txt")
        self.assertRaises(FileNotFoundError, actual)

    def test_load_incorrect_file_exception(self):
        controller = Controller()
        actual = controller.load_file("test2.csv")
        self.assertRaises(NameError, actual)

    def test_get_method_name(self):
        print_class = PrintClass()
        class_item = print_class.class_handler("test_method.docx")
        actual_one = print_class.get_methods(class_item[0])
        expected_one = ["add_toy", "get_toy"]
        actual_two = print_class.get_methods(class_item[1])
        expected_two = ["__str__"]
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    # Rajan
    def test_validate_method_name_is_false(self):
        validator = Validator()
        result_1 = validator.validate_method_name("Get")
        result_2 = validator.validate_method_name("1_get")
        result_3 = validator.validate_method_name("get_Name")
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)

    def test_validate_method_name_is_true(self):
        validator = Validator()
        result_1 = validator.validate_method_name("method_name")
        result_2 = validator.validate_method_name("get")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_method_name_using_special_char(self):
        validator = Validator()
        result = validator.validate_method_name("Name$%^&")
        self.assertFalse(result)

    def test_read_txt_file3(self):
        print_class = PrintClass()
        actual = print_class.read_txt_file("test3.txt")
        expect = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n",
                  "    name : String\n", "}\n", "\n", "class Toy {\n",
                  "    number: int\n", "}\n",
                  "@enduml\n"]
        self.assertEqual(expect, actual)

    def test_load_txt_file3(self):
        controller = Controller()
        actual = controller.load_file("test3.txt")
        expected = [['class ToyBox {\n', '    name : String\n', '}\n'],
                    ['class Toy {\n', '    number: int\n', '}\n']]
        self.assertEqual(expected, actual)

    def test_validate_method_name_is_true2(self):
        validator = Validator()
        result_1 = validator.validate_method_name("_get")
        result_2 = validator.validate_method_name("get1")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_method_name_start_with_num(self):
        validator = Validator()
        result = validator.validate_class_name("123")
        self.assertFalse(result)

    def test_validate_method_name_start_with_capital(self):
        validator = Validator()
        result = validator.validate_method_name("N")
        self.assertFalse(result)

    def test_load_incorrect_file_format(self):
        controller = Controller()
        actual = controller.load_file("test.csv")
        self.assertRaises(NameError, actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
