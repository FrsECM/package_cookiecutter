import pytest
import {{cookiecutter.project_name_cleaned}}


# Remove this tes to make your own.
@pytest.fixture
def x():
    return 0
@pytest.fixture
def dummy_dict():
    return {'test':0}


def test_base(x,dummy_dict):
    assert x==0,"x should be equal to zero"
    with pytest.raises(KeyError):
        dummy_dict['not_existing']
