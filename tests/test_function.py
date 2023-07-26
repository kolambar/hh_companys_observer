import pytest
from src.function import ask_for_adding_employer

def test_ask_for_adding_employer():
    list_numbers = [1, 2, 3]
    ask_for_adding_employer(list_numbers)
    assert list_numbers == [1, 2, 3, 4]
