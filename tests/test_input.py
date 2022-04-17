import pytest

from src.main import boggle_solver


def test_command_line_input():

    # Check if at least one input is given
    with pytest.raises(Exception):
        boggle_solver()

    # Check that no more than two input is given
    with pytest.raises(AttributeError):
        # More than 3 parameter is bad
        boggle_solver(["main.py", "filename", "extra"])

    # Check if impossible file raise an error
    with pytest.raises(FileNotFoundError):
        # File doesn't exist
        boggle_solver(["main.py", "filename.potato"])
