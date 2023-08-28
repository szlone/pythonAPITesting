import pytest
# NOTE 1: A Test Case code must be written inside a method
# NOTE 2: must contain 'test_' in the initial name for the testcase code for oytest to view it a test case!

# decorator
# @pytest.mark.skip("skipping as this functinality not working - developer will fix")
# or can use e.g.:
# a = 100
# @pytest.mark.skipif(a > 100, reason="skipping as this functinality not working - developer will fix")

@pytest.mark.smoke
def test_TestCase6_Login_Logout_Testing():
    print("This is test case 6 - smoke test case...")

@pytest.mark.sanity
def test_TestCase7_Login_Logout_Invalid_Credentials():
    print("This is test case 7 -sanity test case ...")

# for print statements to be displayed in the console for the tests use the switch -s
# to show detailed status to be displayed in the console for the tests use the switch -v (verbose mode)\
# use -k and then the name of the testcase to be de-selected
