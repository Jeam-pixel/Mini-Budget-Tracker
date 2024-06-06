import pytest
import os
import csv
from project.project import option_check, file_check, input_check, append_dict

def test_option_check():
    assert option_check("1") == 1
    assert option_check("2") == 2

def test_file_check():
    assert file_check("test.csv") == True
    assert file_check("test.txt") == False

def test_input_check():
    assert input_check("$50.00", "2024-06-04") == True
    assert input_check("50.00", "2024-06-04") == True

def test_append_dict(tmpdir):
    filename = os.path.join(tmpdir, 'test_append.csv')
    data = {"purchase": "notebook", "amount": "$3.00", "date": "2024-06-07"}

    append_dict(data, filename)

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["purchase"] == "notebook"
        assert rows[0]["amount"] == "$3.00"
        assert rows[0]["date"] == "2024-06-07"

if __name__ == "__main__":
    pytest.main()
