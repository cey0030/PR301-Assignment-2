from fileHandler import PrintClass
import unittest
from controller import Controller
from command import Command


class TestBadSmells(unittest.TestCase):

    def setUp(self):
        self.printClass = PrintClass()
        self.printClass.class_list = [['class Zoo {\n',
                                       '    name : String\n',
                                       '    location : String\n',
                                       '    add_animal()\n',
                                       '    get_animal()\n',
                                       '}\n'],
                                      ['class Animal {\n',
                                       '    name : String\n',
                                       '    number : Integer\n',
                                       '    __str__()\n',
                                       '}\n']]
        self.controller = Controller()
        self.command = Command()

    def test_get_class_name(self):
        self.assertEqual(self.printClass.get_class_name(
            ['class z {\n', '    n : String\n', '    add()\n', '}\n']), 'z')
        self.printClass.get_class_name(
            [' z {\n', '    n : String\n', '    add()\n', '}\n'])

    def test_output_class_exception_invalid_attribute_name(self):
        try:
            self.printClass.output_class(
                ['class Zoo {\n',
                 '    Name : String\n',
                 '    location : String\n',
                 '    add_animal()\n',
                 '    get_animal()\n', '}\n'])
        except NameError:
            self.fail("output_class raised NameError unexpectedly")

    def test_output_class_exception_invalid_method_name(self):
        self.assertEqual(
            self.printClass.output_class(
                [
                    'class Zoo {\n',
                    '    name : String\n',
                    '    location : String\n',
                    '    Add_animal()\n',
                    '    Get_animal()\n',
                    '}\n']),
            'class Zoo:\n'
            '    def __init__(self, name, location):\n'
            '        self.name = name\n'
            '        self.location = location\n'
            '# method name is invalid\n'
            '# method name is invalid\n')

    def test_get_all_num(self):
        self.printClass.get_all_num()

    def test_read_text_file(self):
        self.printClass.read_txt_file("clement.txt")

    def test_identify_r_type(self):
        self.printClass.identify_r_type("o-- <-- <..", "name")
        self.printClass.identify_r_type("<-- <-- <--", "name")
        self.printClass.identify_r_type("o-- o-- o--", "name")
        self.printClass.identify_r_type("<.. <.. <..", "name")
        self.printClass.identify_r_type("<.. <..", "name")
        self.printClass.identify_r_type('"_ #~~ _"', "name")
        self.printClass.identify_r_type(
            '"1" *-- "many" "1" *-- "many"', "name")

    def test_class_handler(self):
        self.printClass.class_handler("test3.csv")
        self.printClass.class_handler("test4.txt")

    def test_fileHandler(self):
        self.controller.load_file("uml.txt")
        self.controller.save_file("")
        self.controller.load_file("test.docx")
        self.controller.save_file("")
        self.controller.load_file("test1.docx")
        self.controller.save_file("")
        self.controller.load_file("test2.docx")
        self.controller.save_file("")
        self.controller.load_file("test3.docx")
        self.controller.save_file("")
        self.controller.load_file("test3.csv")
        self.controller.save_file("")


if __name__ == '__main__':
    unittest.main(verbosity=2)
