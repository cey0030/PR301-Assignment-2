from cmd import Cmd
from controller import Controller


class Command(Cmd):
    controller = Controller()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>>"
        self.my_name = "unknown"

    # Luna
    def do_load(self, file):
        """
        Syntax: load [file]
        Load the PlantUML file that users want to convert into code frame
        :param file: a .txt or .docx file for PlantUML
        :return:
        """
        self.controller.load_file(file)

    # Clement
    def do_create_class_files(self, file_dir):
        """
        Syntax: create_class_files [file_dir]
        Saves the file entered (either a .txt or docx file)
        :param file_dir: for the location of the file e.g. C:\\
        :return: none
        """
        self.controller.save_file(file_dir)

    # Rajan
    # Change commands and options: Luna: /a; Rajan: /p; Clement: /l
    def do_display(self, option):
        """
        Syntax: display [/a | /p | /l]
        Display bar chart, pie chart or line graph
        :param option: /a: display bar chart
                       /p: display pie chart
                       /l: display line graph
        :return: none
        """
        tokendict = {
            "/a": self.controller.create_bar_chart,
            "/p": self.controller.create_pie_chart,
            "/l": self.controller.create_line_chart}
        if option and option.strip():
            if option in tokendict:
                tokendict[option]()
        else:
            print("please choose one or see help display")

    def do_quit(self, line):
        print("Quitting ......")
        return True


if __name__ == "__main__":
    command = Command()
    command.cmdloop()
