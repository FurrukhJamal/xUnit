from TestSuperClass import TestCase
from test import WasRun
from TestResult import TestResult
from TestSuite import TestSuite

class TestCaseTest(TestCase):
    
    # def __init__(self, name):
    #     super().__init__(name)
    
    def setUp(self):
        #self.test = WasRun("testMethod")
        # assert(self.test.wasRun)
        self.result = TestResult()

    
    
    # def testRunning(self):
    #     self.test.run()
    #     assert(self.test.wasRun)

    # def testSetUp(self):
    #     self.test.run()
    #     # assert(self.test.wasSetUp)
    #     # print(f"self.test.log: {self.test.log}")
    #     # print("setUp testMethod" == self.test.log)
    #     # print(type("setUp testMethod "))
    #    # print([ord(c) for c in self.test.log])
    #    # print([ord(c) for c in "setUp testMethod"])
    #     assert("setUp testMethod " == self.test.log)
    
    
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        # self.test.run()
        #result = TestResult()
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
    
    # def testRunning(self):
    #     test = WasRun("testMethod")
    #     # assert ( not test.wasRun)
    #     test.run()
    #     assert(test.wasRun)

    # def testSetUp(self):
    #     test= WasRun("testMethod")
    #     test.run()
    #     assert(test.wasSetUp)

    def testResult(self):
        test = WasRun("testMethod")
        #result = TestResult()
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("BrokenTest")
        #result = TestResult()
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        # result= TestResult()
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        #result = TestResult()
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())
    


def main():
    print("main running")
    # TestCaseTest("testRunning").run()
    #TestCaseTest("testSetUp").run()
    #TestCaseTest("testTemplateMethod").run()

    suite= TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))
    result= TestResult()
    suite.run(result)
    print (result.summary()) 

if __name__ == "__main__":
    main()