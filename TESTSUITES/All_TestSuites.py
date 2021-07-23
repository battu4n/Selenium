import unittest
from PACKAGE1.TC_LoginTest import Logintest
from PACKAGE1.TC_signuptest import Signuptest

from PACKAGE2.TC_paymenttest import paymenttest
from PACKAGE2.TC_paymentreturntest import paymentreturn

#To get all test cases from all packages

tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(Signuptest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymenttest)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymentreturn)

#Create test suites
#sanityTestSuite=unittest.TestSuite([tc1,tc2])#sanity suite
#functionalTestSuite=unittest.TestSuite([tc3,tc4])
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner().run(masterTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
#unittest.TextTestRunner().run(sanityTestSuite)