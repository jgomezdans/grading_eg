#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.abspath(".."))

from assignment2 import assignment_two


def test_two():
    sample_string = "A boring tedious string"
    sol = sample_string.replace("ri", "#")
    assert sol == assignment_two(sample_string)
