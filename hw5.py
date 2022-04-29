
# Problem 1 (2 points)
# Assign the 'name' variable an object that is your name of type str.
name = "taylor.pubins"

# Problem 2 (2 points)
# Create a class and implement it for your problem of interest


class Player:
    def __init__(self, idfg, idespn, name, team, pos, *args, **kwargs):
        self.idFangraphs = idfg
        self.idESPN = idespn
        self.name = name
        self.team = team
        self.pos = pos

# Problem 3 (2 points)
# Create another class and implement it for your problem of interest


class Hitter(Player):
    def __init__(self, r, hr, rbi, sbn, obp, slg, *args, **kwargs):
        self.R = r
        self.HR = hr
        self.RBI = rbi
        self.SBN = sbn
        self.OBP = obp
        self.SLG = slg
        super(Hitter, self).__init__(*args, **kwargs)


# Problem 4 (2 points)
# Create another class and implement it for your problem of interest


# If you need to, you can create any additional classes or functions here as well.


# Problem 5 (2 points)
# Assign a variable named 'obj_1' an example instance of one of your classes


# Problem 6 (2 points)
#  Assign a variable named 'obj_2' an example instance of another one of your
#  classes


# Problem 7 (2 points)
#  Assign a variable named 'obj_3' an example instance of one of your classes
#  that extends another class


# Problems 8 through 14 are worth 4 points each.
#    For each problem you must implement a test method in the following
#     TestCase class. Each method name should be unique and start with 'test_'.
#     Each method should test something different about the classes you created
#     above. Use unittest.TestCase's assert methods to check your implementation.
#     You will get 2 points for each test method created. You will get 2
#     additional points for each of these tests that complete successfully.
#     See https://docs.python.org/3/library/unittest.html for examples.

import unittest
import sys
import inspect
###################################################
#DO NOT MODIFY this class's name or what it extends
###################################################
class MyTestCases(unittest.TestCase):

    # Problem 8
    # add test case method

    # Problem 9
    # add test case method

    # Problem 10
    # add test case method
    
    # Problem 11
    # add test case method

    # Problem 12
    # add test case method

    # Problem 13
    # add test case method

    # Problem 14
    # add test case method

    ##################################################
    #DO NOT MODIFY any of these test case methods
    ##################################################

    def get_classes(self):
        clses = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member is not MyTestCases)
        return clses

    def test_name_assigned(self):
        m = sys.modules[__name__]
        name = getattr(m,"name",None)
        self.assertTrue(name is not None)
        self.assertTrue(isinstance(name,str))
        self.assertTrue(len(name) > 0)

    def test_one_class_created(self):
        self.assertTrue(len(self.get_classes()) >= 1)

    def test_two_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 2)

    def test_three_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 3)

    def test_obj_1_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_1 is not None)
        self.assertTrue(isinstance(obj_1,tuple([cls[1] for cls in clses])))

    def test_obj_2_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_2 = getattr(m,"obj_2",None)
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_2 is not None)
        self.assertTrue(isinstance(obj_2,tuple([cls[1] for cls in clses])))
        self.assertNotEqual(type(obj_2),type(obj_1))

    def test_obj_3_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_3 = getattr(m,"obj_3",None)
        self.assertTrue(obj_3 is not None)
        self.assertTrue(isinstance(obj_3,tuple([cls[1] for cls in clses])))
        bases = tuple(b for b in type(obj_3).__bases__ if b is not object)
        print(dir(obj_3))
        self.assertTrue(len(bases) > 0)
        
##################################################
#DO NOT MODIFY any of the code below!
##################################################
if __name__ == "__main__":
    unittest.main()

