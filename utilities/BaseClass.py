import  pytest

# This class is inherited to all the Test classes so that we can get the fixtures and code looks
# more clean and optimised
@pytest.mark.usefixtures("setup")
class BaseClass:
    pass