"""Tests for main module."""

import pytest
from main import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("testproof") == "Hello, testproof!"
