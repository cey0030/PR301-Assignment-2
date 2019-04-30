from validator import Validator
from fileProcessor import FileProcessor
import os


class PrintClass:
    fileProcessor = FileProcessor()

    def __init__(self):
        self.class_name_list = self.fileProcessor.class_name_list

    def output_class(self, class_item):
        class_name = self.get_class_name(class_item)
        self.class_name_list.append(class_name)
        attribute_list = self.get_attributes(class_item)
        method_list = self.get_methods(class_item)
        relationship_list = self.get_relationship(class_name)
        result = "class " + class_name + ":\n    def __init__(self"

        for listItem in attribute_list:
            result += ', ' + listItem

        result += '):\n'

        if Validator.validate_class_name(class_name):
            pass

        for listItem in attribute_list:
            try:
                if Validator.validate_attribute_name(listItem):
                    result += '        self.' + \
                              listItem + ' = ' + listItem + '\n'
                else:
                    raise NameError('Invalid name: ' + listItem)
            except NameError as e:
                print(e)

        if len(attribute_list) == 0:
            result += "        pass\n"

        for list_item in relationship_list:
            result += list_item

        for listItem in method_list:
            if Validator.validate_method_name(listItem):
                result += '\n'
                result += 'def ' + listItem + '(self):\n     # Todo: inco' \
                                              'mplete\n        pass\n'
            else:
                result += "# method name is invalid\n"
        return result

    def output_classes(self, file_dir):
        files = []
        for classItem in self.class_list:
            files.append(file_dir + self.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_list, files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)
        print("Files are created")

    def get_all_num(self):
        return self.fileProcessor.get_all_num()

    def class_handler(self, file_name):
        return self.fileInput.class_handler(file_name)

    def identify_r_type(self, a_relationship, name):
        return self.fileProcessor.identify_r_type(a_relationship, name)

    def get_class_name(self, class_array):
        return self.fileProcessor.get_class_name(class_array)

    def read_txt_file(self, file_name):
        return self.fileInput.read_txt_file(file_name)

    def get_attributes(self, class_array):
        return self.fileProcessor.get_attributes(class_array)

    def get_methods(self, class_array):
        return self.fileProcessor.get_methods(class_array)

    def get_relationship(self, class_array):
        return self.fileProcessor.get_relationship(class_array)

    def read_word_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = docx.Document(file_name)
                content = []
                for para in file.paragraphs:
                    content.append(para.text + "\n")
                return content
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("Cannot find this file")

    # Clement: load data from .txt file
    # Rajan: exception
    def read_txt_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = open(file_name, 'r').readlines()
                return file
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("File doesn't exist")

    def class_handler(self, file_name):
        class_list = [[]]
        file_content = []
        if ".txt" in file_name[-4:]:
            file_content = self.read_txt_file(file_name)
        elif ".docx" in file_name[-5:]:
            file_content = self.read_word_file(file_name)
        for i, m in enumerate(file_content[1:-1]):
            if m == "\n":
                if i != len(file_content[1:-1]) - 1:
                    class_list.append([])
            else:
                class_list[-1].append(m)
        self.relationship_list = class_list[0]
        self.class_list = class_list[1:]
        return self.class_list
