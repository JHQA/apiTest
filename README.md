-To get started-
Add user name and key the credential portion of every test file.

    # Credentials
    email = ''
    apiKey = ''

Make sure to have requests library installed(pip install requests).
Navigate to the main folder containing the tests.
Type 'Python3 -m unittest' in terminal to run the full suite.
Add the file name to only run that specific test, such as 'Python3 -m unittest test_List.py'.

-What are these tests?-
Each file contains at least 5 general tests of an api endpoint, verifying the output.

-Why unittest-
With increased scope I would of opted for a more feature rich test framework, but as
unittest is included in the standard library it is one less thing that reviewers would
need to install.