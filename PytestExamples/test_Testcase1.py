import pytest

@pytest.fixture()
def fixture_code(scope="module"):
    # adding scope="module" in the argument above allows for the after execution code to run
    # only at the end of ALL the test cases and not after each test case!
    print("This is fixture code case and will execute before testcase...")
    print("-------------------------------------------------------------")
    yield
    # yield - tells pytest to run the code after execution  of the test case
    print("This is fixture code case and will execute after testcase...")
    print("-*************************************************************")

# note for the fixture code to run one has to pass the fixture code to the test cases
def test_TestCase1_Login_Logout_Testing(fixture_code):
    print("This is test case 1 code...")


@pytest.mark.sanity
@pytest.mark.login # another tag for the same testcase
def test_TestCase3_Login_Logout_Invalid_Credentials(fixture_code):
    print("This is test case 3 - sanity testcase..")


