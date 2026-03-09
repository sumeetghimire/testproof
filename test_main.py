"""Tests for main module."""

import pytest
from main import greet, farewell, greet_formal


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("testproof") == "Hello, testproof!"


def test_farewell_default():
    assert farewell() == "Goodbye, World!"


def test_farewell_with_name():
    assert farewell("testproof") == "Goodbye, testproof!"


def test_greet_formal_default():
    assert greet_formal() == "Good day, World."


def test_greet_formal_with_name():
    assert greet_formal("Alice") == "Good day, Alice."
