import pytest
from project_pes.app import Dog


def test_dog_name_uniqueness():
    dog1 = Dog("male", "Buddy", 4)
    dog2 = Dog("male", "Buddy", 3)

    assert dog1.name == "Buddy"
    assert dog2.name == "Buddy2"


def test_dog_str_representation():
    dog = Dog("Female", "Lucy", 2)
    result = str(dog)

    
    assert "Lucy" in result
    assert "2-year-old" in result
    assert "female" in result