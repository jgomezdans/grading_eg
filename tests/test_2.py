from ..assignment2 import assignment_two

def test_two():
    sample_string = "A boring tedious string"
    sol = sample_string.replace("ri", "#")
    assert sol == assignment_two(sample_string)