class FileProcessor:
    def __init__(self):
        self.relationship_list = []
        self.class_name_list = []
        self.num_all_attribute_list = []
        self.num_all_method_list = []
        self.compo_1_to_1 = []
        self.aggr_1_to_1 = []
        self.compo_1_to_many = []
        self.aggr_1_to_many = []
        self.association_list = []
        self.dependency_list = []

    def get_class_name(self, class_array):
        for listItem in class_array:
            if "class" in listItem:
                temp_class = listItem[:listItem.index(" {")]
                class_name = temp_class.split(' ')[1]
                return class_name

    def get_attributes(self, class_array):
        attributes = []
        for listItem in class_array:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        num_attribute = len(attributes)
        self.num_all_attribute_list.append(num_attribute)
        return attributes

    def get_methods(self, class_array):
        methods = []
        for listItem in class_array:
            if "(" in listItem:
                methods.append(listItem[:listItem.index("\n")-2].strip())
        num_method = len(methods)
        self.num_all_method_list.append(num_method)
        return methods

    def get_relationship(self, class_name):
        temp_relationship = []
        for a_relationship in self.relationship_list:
            r_class_name = a_relationship.split(" ")
            first_c_name = r_class_name[0]
            second_c_name = r_class_name[-1].replace("\n", "")
            if class_name == first_c_name:
                temp_relationship += self.identify_r_type(a_relationship,
                                                          second_c_name)
        return temp_relationship

    def identify_r_type(self, a_relationship, name):
        a_r = ''
        if len(a_relationship.split(" ")) == 3:
            a_r = self.handle_normal_relationship(a_r, a_relationship, name)
        else:
            a_r = self.handle_one_to_many_relationship(a_r, a_relationship, name)
        return a_r

    def handle_one_to_many_relationship(self, a_r, a_relationship, name):
        if '"1" *-- "many"' in a_relationship:
            self.compo_1_to_many.append(name)
            a_r = "        # self. my_" + name.lower() + ": list" + " -> " \
                  + name + "\n" + "        self." + name.lower() + " = " \
                  + "None\n"
        elif '"1" o-- "many"' in a_relationship:
            self.aggr_1_to_many.append(name)
        return a_r

    def handle_normal_relationship(self, a_r, a_relationship, name):
        tokenDict = {"*--": self.add_composition(a_r, name), "o--": self.aggr_1_to_1.append(name),
                     "<--": self.association_list.append(name), "<..": self.dependency_list.append(name)}
        if a_relationship in tokenDict:
            tokenDict[a_relationship]()
        return a_r

    def add_composition(self, a_r, name):
        self.compo_1_to_1.append(name)
        a_r += "        # self. my_" + name.lower() + " -> " + name \
               + "\n" + "        self." + name.lower() + " = " + "None \n"
        return a_r

    def get_all_num(self):
        class_num = len(self.class_name_list)
        attribute_num = sum(self.num_all_attribute_list)
        method_num = sum(self.num_all_method_list)
        all_num = [class_num, attribute_num, method_num]
        return all_num
