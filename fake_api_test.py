# fake_api_test.py
# Test: PRoof should detect math.super_advanced_sqrt as hallucinated (not in Python's math module).

import math


def calculate():
    return math.super_advanced_sqrt(16)
