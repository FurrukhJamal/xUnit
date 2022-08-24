from TestSuperClass import TestCase
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        # self.name = name
        self.wasSetUp = 0
        self.test = None
        TestCase.__init__(self,name)

    def testMethod(self):
        self.wasRun = 1
        self.log= self.log + " testMethod "

    def setUp(self):
        self.wasRun = None
        self.wasSetUp= 1
        self.log = "setUp"

    def tearDown(self):
        self.log = self.log + "tearDown "

    def BrokenTest(self):
        raise Exception
        

    # def run(self):
    #     # self.testMethod()
    #     method = getattr(self, self.name)
    #     method()