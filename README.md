-To get started-
Add a user email and key to the credential portion of every test file.

    # Credentials
    email = ''
    apiKey = ''

Make sure to have requests library installed(pip install requests).
Navigate to the main folder containing the tests.
Type 'Python -m unittest' in terminal to run the full suite, 64 total tests.
Add the file name to only run that specific test, such as 'Python -m unittest test_List.py'.

-What are these tests?-
Each file contains at least 5 general tests of an api endpoint, verifying every market output.

-Why unittest-
With increased scope I would of opted for a more feature rich test framework, but as
unittest is included in the Python standard library it is one less thing that reviewers would
need to install.
