import re


class Validator:
    # Luna
    @staticmethod
    def validate_class_name(class_name):
        """
        >>> Validator.validate_class_name("ClassBuilder")
        True
        >>> Validator.validate_class_name("ClassName123")
        True
        >>> Validator.validate_class_name("classBuilder")
        False
        >>> Validator.validate_class_name("C!#Name")
        False
        >>> Validator.validate_class_name("ClassName>")
        False
        >>> Validator.validate_class_name("1ClassName>")
        False
        """
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
        if class_name[0].isupper() and regex.search(class_name) is None:
            return True
        else:
            return False

    # Clement
    @staticmethod
    def validate_attribute_name(name):
        """
        >>> Validator.validate_attribute_name("Name")
        False
        >>> Validator.validate_attribute_name("and")
        False
        >>> Validator.validate_attribute_name("assert")
        False
        >>> Validator.validate_attribute_name("class")
        False
        >>> Validator.validate_attribute_name("continue")
        False
        >>> Validator.validate_attribute_name("def")
        False
        >>> Validator.validate_attribute_name("del")
        False
        >>> Validator.validate_attribute_name("elif")
        False
        >>> Validator.validate_attribute_name("else")
        False
        >>> Validator.validate_attribute_name("except")
        False
        >>> Validator.validate_attribute_name("exec")
        False
        >>> Validator.validate_attribute_name("finally")
        False
        >>> Validator.validate_attribute_name("for")
        False
        >>> Validator.validate_attribute_name("from")
        False
        >>> Validator.validate_attribute_name("global")
        False
        >>> Validator.validate_attribute_name("if")
        False
        >>> Validator.validate_attribute_name("import")
        False
        >>> Validator.validate_attribute_name("in")
        False
        >>> Validator.validate_attribute_name("is")
        False
        >>> Validator.validate_attribute_name("lambda")
        False
        >>> Validator.validate_attribute_name("not")
        False
        >>> Validator.validate_attribute_name("or")
        False
        >>> Validator.validate_attribute_name("pass")
        False
        >>> Validator.validate_attribute_name("print")
        False
        >>> Validator.validate_attribute_name("raise")
        False
        >>> Validator.validate_attribute_name("return")
        False
        >>> Validator.validate_attribute_name("try")
        False
        >>> Validator.validate_attribute_name("while")
        False
        >>> Validator.validate_attribute_name("break")
        False
        >>> Validator.validate_attribute_name("a")
        False
        >>> Validator.validate_attribute_name(1234)
        False
        >>> Validator.validate_attribute_name("attribute")
        True
        >>> Validator.validate_attribute_name("Sometimes" \
                "python programming can be hard")
        False
        >>> Validator.validate_attribute_name("/&*(")
        False
        >>> Validator.validate_attribute_name("name1")
        False
        """

        # above is doctest

        regex = re.compile('[@!#$%^&*()<>?/|}{~:A-Z]')
        res = [
            'and',
            'assert',
            'break',
            'class',
            'continue',
            'def',
            'del',
            'elif',
            'else',
            'except',
            'exec',
            'finally',
            'for',
            'from',
            'global',
            'if',
            'import',
            'in',
            'is',
            'lambda',
            'not',
            'or',
            'pass',
            'print',
            'raise',
            'return',
            'try',
            'while',
        ]
        if not isinstance(name, str) or name in res or \
                not 1 < len(name) < 31 or regex.search(name) is not None or \
                any(char.isdigit() for char in name):
            return False
        else:
            return True

    # Rajan

    @staticmethod
    def validate_method_name(name):
        """
        >>> Validator.validate_method_name("Name")
        False
        >>> Validator.validate_method_name("method_name")
        True
        >>> Validator.validate_method_name("get_A")
        False
        >>> Validator.validate_method_name("get")
        True
        >>> Validator.validate_method_name("_get")
        True
        >>> Validator.validate_method_name("get_method_name")
        True
        >>> Validator.validate_method_name("getName")
        False
        >>> Validator.validate_method_name("NameGet")
        False
        >>> Validator.validate_method_name("name")
        True
        >>> Validator.validate_method_name("name")
        True
        >>> Validator.validate_method_name("1_get")
        False
        >>> Validator.validate_method_name("@_get")
        False
        >>> Validator.validate_method_name("*name")
        False
        >>> Validator.validate_method_name("!name")
        False
        >>> Validator.validate_method_name(":method_name")
        False
        >>> Validator.validate_method_name("/get_name")
        False
        >>> Validator.validate_method_name("$name")
        False
        >>> Validator.validate_method_name("/name")
        False
        >>> Validator.validate_method_name("~name")
        False
        >>> Validator.validate_method_name("^name")
        False
        >>> Validator.validate_method_name("%name")
        False
        >>> Validator.validate_method_name("name")
        True
        >>> Validator.validate_method_name("get_name")
        True
        >>> Validator.validate_method_name("NAME_GET")
        False
        >>> Validator.validate_method_name("(get_name)")
        False
        >>> Validator.validate_method_name("MethodName>")
        False
        >>> Validator.validate_method_name("1methodName>")
        False
        >>> Validator.validate_method_name("get1")
        True
        """

        # below is doctest

        regex = re.compile('[@!#$%^&*()<>?/|}{~:A-Z]')
        if regex.search(name) is not None or name[0].isdigit():
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
