""" Basic Operation Problems """
import random

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table

class BasicOpProblem:
    """ This module allows the creation of basic operation problems involving two numbers
    """

    ADD = "add"
    SUB = "sub"
    MULT = "mult"
    DIV = "div"

    name = "basicOp"
    handled_types = [ADD, SUB, MULT, DIV]
    operators = {
        ADD : '+',
        SUB : u"\u2796", # Heavy Minus http://www.fileformat.info/info/unicode/char/2796/index.htm
            # u"\u2212" # Minus http://www.fileformat.info/info/unicode/char/2212/index.htm
        MULT : '\xc3\x97',
        DIV:  '\xc3\xb7'
    }
    def __init__(self, specs, num1=None, num2=None):
        """ Create a new adding ("add"), subtraction ("sub"), multiplication ("mult") or division ("div") operation

        Parameters
        ----------
        operation (str): "add", "sub", "mult" or "div" to set the problem type
        num1 (int):
        num2 (int):
        """
        if specs['type'] not in ["add", "sub", "mult", "div"]:
            raise ValueError("Unsupported Operation Type: Must be \"add\", \"sub\", \"mult\", or \"div\"")

        self.num1 = num1
        self.prob_type = "BasicOp"
        self.num2 = num2
        self.operation = specs['type']
        self.op_symbol = self.operators[self.operation]
        if specs['randomize']:
            self.randomize_nums(specs['min_value'], specs['max_value'])

    @property
    def ans(self):
        ''' returns the automatically computered ans based on num1, num2 and the operation '''
        if self.num1 == None or self.num2 == None:
            raise ValueError("Answer not set yet. Num1 and Num2 are required.")
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "sub":
            return self.num1 - self.num2
        elif self.operation == "mult":
            return self.num1 * self.num2
        elif self.operation == "div":
            return self.num1 // self.num2

    def randomize_nums(self, min_value=1, max_value=10):
        ''' sets num1 and num2 to a randomized min and max value in the given range '''
        if min_value > max_value:
            raise ValueError("Min must be less than max")
        self.num1 = random.randint(min_value, max_value)
        self.num2 = random.randint(min_value, max_value)


    def set_num1(self, min_value=1, max_value=10):
        self.num1 = random.randint(min_value, max_value)

    def set_num2(self, min_value=1, max_value=10):
        self.num2 = random.randint(min_value, max_value)

    def screen_display(self):
        print(str(self.num1) + self.op_symbol + str(self.num2))

    def reportlab_display(self):
        data = [["", str(self.num1)], [self.op_symbol, str(self.num2)], ["", ""]]
        t=Table(data, style=[
            ('BOX',(0,2),(1,2), 2, colors.black),
            ('ALIGN', (1,0), (1,1), "RIGHT")
        ])
        return t

