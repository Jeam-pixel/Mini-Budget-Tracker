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

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `csv`, `sys`, `re`, `os`, `tabulate`, `pytest`.

### Installation

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

- `main()`: Entry point of the application.
- `add_expense()`:   - The `main()` function serves as the starting point for the Personal Finance Tracker application. It begins by prompting the user for their name and then welcomes them to the program. The function enters an infinite loop, displaying a menu of options that allows the user to add an expense, calculate the total expenses, view all expenses, or exit the program. Based on the user's choice, the appropriate function (`add_expense()`, `calculate_expense()`, `view_expense()`) is called. If the user chooses to exit, the program terminates with a goodbye message.
- `calculate_expense()`: Calculates and displays the total amount of expenses.
- `view_expense()`: Displays all recorded expenses in a formatted table.
- `option_check(command)`: Validates the user command input.
- `file_check(file)`: Validates the CSV file.
- `input_check(amount, date)`: Validates the format of the amount and date inputs.
- `append_dict(dictionary, filename)`: Appends a dictionary entry to the CSV file.

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
