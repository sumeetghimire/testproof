"""Tests for main module."""

import pytest
from main import greet, farewell, greet_formal, thanks, welcome


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


def test_thanks_default():
    assert thanks() == "Thank you, you!"


def test_thanks_with_name():
    assert thanks("contributor") == "Thank you, contributor!"


def test_welcome_default():
    assert welcome() == "Welcome, guest!"


def test_welcome_with_name():
    assert welcome("developer") == "Welcome, developer!"
