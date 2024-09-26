import os
from unittest.mock import Mock, patch
import pandas as pd
import csv

import pytest

from src.pandas_work import read_csv_file, read_excel_file


@patch("src.pandas_work.pd.read_csv")
def test_read_csv_file(mock_read):
    mock_read.return_value = pd.DataFrame({"test1": [1], "test2": [2]})
    assert read_csv_file("../data/example.csv") == [{"test1": 1, "test2": 2}]


@patch("src.pandas_work.pd.read_csv")
def test_read_csv_file_empty_df(mock_read):
    mock_read.return_value = pd.DataFrame({"": []})
    assert read_csv_file("../data/example.csv") == []


def test_read_csv_file_invalid_path():
    with pytest.raises(FileNotFoundError):
        read_csv_file("../data/123.csv")


@patch("src.pandas_work.pd.read_excel")
def test_read_excel_file(mock_read):
    mock_read.return_value = pd.DataFrame({"test1": [1], "test2": [2]})
    assert read_excel_file("../data/example.csv") == [{"test1": 1, "test2": 2}]


def test_read_excel_file_invalid_path():
    with pytest.raises(FileNotFoundError):
        read_excel_file("../data/123.xlsx")
