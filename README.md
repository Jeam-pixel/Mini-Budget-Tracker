# Personal Finance Tracker

#### Video Demo:  [URL HERE]
#### Description:
The Personal Finance Tracker is a command-line application designed to help users manage their personal expenses. Users can add, view, and calculate their expenses, all stored in a CSV file. This project is an intermediate-level Python application that demonstrates skills in file handling, data processing, user input validation, and automated testing.

## Features

- **Add Expense**: Users can add a new expense by providing the purchase description, amount, and date.
- **View Expenses**: Users can view all recorded expenses in a neatly formatted table.
- **Calculate Total Expenses**: Users can calculate the total amount spent based on the recorded expenses.
- **User-Friendly Interface**: Simple command-line interface for ease of use.

## Usage
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/finance-tracker.git
    cd finance-tracker
    ```

2. Install the required packages:
    ```sh
    pip install tabulate pytest
    ```

### Running the Application

1. Run the main script:
    ```sh
    python finance_tracker.py
    ```

2. Follow the on-screen prompts to interact with the Personal Finance Tracker.
## Code Overview

### Main Functions

- `main()`:  The `main()` function serves as the starting point for the Personal Finance Tracker application. It begins by prompting the user for their name and then welcomes them to the program. The function enters an infinite loop, displaying a menu of options that allows the user to add an expense, calculate the total expenses, view all expenses, or exit the program. Based on the user's choice, the appropriate function (`add_expense()`, `calculate_expense()`, `view_expense()`) is called. If the user chooses to exit, the program terminates with a goodbye message.
  
- `add_expense()`: This function facilitates the addition of a new expense record to the CSV file. It first prompts the user to specify the CSV file to which the expense will be added. After verifying the validity of the file, the function asks the user to enter the details of the expense, including the purchase description, amount, and date. It uses input validation to ensure the data is correctly formatted. Once validated, the expense data is appended to the specified CSV file. If the file does not already exist, the function creates it and includes a header row. A confirmation message is displayed once the expense is successfully added.

- `calculate_expense()`: This function prompts for a file like the other 2 but this time, after validating using `file_check`, opens the file on readmode. It initializes a counter variable called `amount` to 0 then loops through the list of dictionaries from the reader. The value of each amount for each row key get accumulated to the counter variable then the function prints out the total amount spent.
  
- `view_expense()`: The last big function's main purpose is to make the budget csv file readable and organized. First it prompts the user for a file, then opens it in read mode, then appends every row from the reader using a for loop in a list. Once complete, it prints out an organized table using the `tabulate` function from the tabulate library.
  
- `option_check(command)`: This checking function accepts a command as a parameter, if the command isn't an integer or an integer between 0 and 5 it re-prompts the user. Otherwise it returns the verified command
  
- `file_check(file)`: This function has one parameter being the filename, if the name of the file doesn't end with ".csv" or have characters to the left of ".csv" it'll return False. I applied regex for checking with the logic similar to the week 7 problem sets.
  
- `input_check(amount, date)`: This function is mainly used in the `add_expense` function to validate the input from the user. Similar to `file_check` I also used regex in checking the amount to see if it's only integers, while making the '$', and decimal to be optional. On the other hand, the date is stated to be in `YYYY/MM/DD` format but I'm just relying on the honor system here, the user could technically input something like 9999-42-12 and it would still work. Otherwise, if no `ValueError`s are raised, it returns `True`.
  
- `append_dict(dictionary, filename)`: This function first checks to see if a file exists or not, either way it opens the file on write mode and sets the headers to `["purchase", "amount", "date"]`. If the file doesn't exist just it writes the headers, otherwise it writes the dictionary received as a row.

### Testing

- The test file `test_finance_tracker.py` contains unit tests for the main functions using the `pytest` framework.
- Tests include validation of user inputs, file operations, and data processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [tabulate Documentation](https://pypi.org/project/tabulate/)

## Contact

For any questions or suggestions, feel free to contact me at [rcgalut1@gmail.com].
