import pytest
from q_and_a import tester

# Arrange
@pytest.fixture
def input_qn():
    return "Who am I?, I am Robert"


def test_tester(input_qn):
    assert isinstance(tester(input_qn), str) == True
