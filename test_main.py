"""Tests for main module."""

import pytest
from main import greet, farewell, greet_formal, thanks, welcome, greet_loud, bye
from validation import validate_name


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


def test_validate_name_returns_default_for_empty():
    assert validate_name("") == "World"
    assert validate_name("   ") == "World"


def test_validate_name_returns_cleaned_name():
    assert validate_name("Alice") == "Alice"
    assert validate_name("  Bob  ") == "Bob"


def test_validate_name_rejects_invalid_chars():
    assert validate_name("Alice@") == "World"
    assert validate_name("Bob!") == "World"


def test_greet_loud_default():
    assert greet_loud() == "HELLO, WORLD!"


def test_greet_loud_with_name():
    assert greet_loud("Alice") == "HELLO, ALICE!"


def test_bye_default():
    assert bye() == "Bye, you!"


def test_bye_with_name():
    assert bye("team") == "Bye, team!"
