# Tests Suite

## 🎯 Overview.

This project provides a Test Suite for the steelers Challenge with Selenium WebDriver, written in Python, using the Page Object Model design pattern and BDD via feature files through Pytest BDD.

## Folder Structure.

    .
    ├── tests                   # Automated tests
    │   ├── features            # Feature files
    │   ├── reports            	# Reports files
    │   │   ├── reports.html    # Automated tests report
    │   ├── step_defs           # Step definition modules for each feature
    │   │   ├── pages           # Pages Object Model (POM)
    │   │   ├── utils           # Shared utils functions for test suites
    │   │   ├── conftest.py     # Shared configuration and functions for test suites
    │   │   ├── constants.py    # Shared constants for the project
    ├── pytest.ini              # Command line options
    ├── requeriments.txt        # Project dependencies
    └── README.md

### Project Structure

- `features` - this folder contains the Gherkin .feature files, one per website page. By separating out the tests for each page into separate feature files we continue the Page Object Model pattern of page independence and make it easier to extend the framework in the future.
- `pages` - the Page Object Model implementation of the individual website pages, one class file per page. Each class is named after the corresponding page.
- `step_defs` - a collection of files containing the implementation of the steps from the BDD feature files. As above, there is one steps file per page and each is named after the page under test.

### How to compile

In the project root folder run the following commands:

1. To activate the project virtual environment: `source virtual_env/bin/activate`
2. Download all the dependencies `pip install -r requirements.txt`

### How to run

To execute all tests run the command:

`$ pytest`
