import unittest
from foo import ClassUnderTest

# Fourphases of testing:Setup, Exercise, Verify, and Teardown

# class ClassUnderTest:
# 	def krajik(self, foo):
# 		return 0

class CheckCut(unittest.TestCase):
	def runTest(self):
		cut = ClassUnderTest()
		actual = cut.krajik(17)
		expected = 34
		assert expected ==actual, 'you are screwed'

testCase = CheckCut()

runner = unittest.TextTestRunner()		
runner.run(testCase)

