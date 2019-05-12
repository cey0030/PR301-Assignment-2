import os
import docx


class FileInput:

    def __init__(self, fileprocessor):
        self.class_list = []
        self.fileProcessor = fileprocessor

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
        self.fileProcessor.relationship_list = class_list[0]
        self.class_list = class_list[1:]
        return self.class_list
