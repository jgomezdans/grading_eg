from ..assignment1 import assignment_one

def test_one():
    sample_string = "A boring tedious string"
    assert len(sample_string) == assignment_one(sample_string)