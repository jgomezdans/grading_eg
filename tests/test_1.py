#!/usr/bin/env python
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from assignment1 import assignment_one

def test_one():
    sample_string = "A boring tedious string"
    assert len(sample_string) == assignment_one(sample_string)