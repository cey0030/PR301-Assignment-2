from validator import Validator
from fileProcessor import FileProcessor
from FileInput import FileInput


class PrintClass:
    def __init__(self):
        self.fileProcessor = FileProcessor()
        self.fileInput = FileInput(self.fileProcessor)
        self.class_list = self.fileInput.class_list
        self.class_name_list = self.fileProcessor.class_name_list

    def output_class(self, class_item):
        result = self.add_class_names(class_item)

        result = self.add_attributes(class_item, result)

        result = self.add_relationships(class_item, result)

        result = self.add_methods(class_item, result)
        return result

    def add_methods(self, class_item, result):
        for listItem in self.get_methods(class_item):
            result = self.check_methods(listItem, result)
        return result

    def check_methods(self, listitem, result):
        if Validator.validate_method_name(listitem):
            result += '\n'
            result += 'def ' + listitem + '(self):\n     # Todo: inco' \
                                          'mplete\n        pass\n'
        else:
            result += "# method name is invalid\n"
        return result

    def add_relationships(self, class_item, result):
        for list_item in self.get_relationship(
                self.get_class_name(class_item)):
            result += list_item
        return result

    def add_attributes(self, class_item, result):
        for listItem in self.get_attributes(class_item):
            result = self.check_attributes(listItem, result)
        if len(self.get_attributes(class_item)) == 0:
            result += "        pass\n"
        return result

    def check_attributes(self, listitem, result):
        try:
            if Validator.validate_attribute_name(listitem):
                result += '        self.' + \
                          listitem + ' = ' + listitem + '\n'
            else:
                raise NameError('Invalid name: ' + listitem)
        except NameError as e:
            print(e)
        return result

    def add_class_names(self, class_item):
        self.class_name_list.append(self.get_class_name(class_item))
        result = "class " + \
            self.get_class_name(class_item) + ":\n    def __init__(self"
        for listItem in self.get_attributes(class_item):
            result += ', ' + listItem
        result += '):\n'
        self.check_class_names(class_item)
        return result

    def check_class_names(self, class_item):
        if not Validator.validate_class_name(self.get_class_name(class_item)):
            print("Invalid class name: " + self.get_class_name(class_item))

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
