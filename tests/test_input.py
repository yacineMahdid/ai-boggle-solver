import pytest

from src.main import boggle_solver


def test_command_line_input():

    # Check if the input are not correct
    with pytest.raises(Exception):
        # No input is bad
        boggle_solver()

    with pytest.raises(Exception):
        # More than 3 parameter is bad
        boggle_solver(["main.py", "filename", "extra"])