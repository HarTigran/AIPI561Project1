from q_and_a import tester


def test_tester():
    test_string = "Who am I?, I am Robert"
    assert isinstance(tester(test_string), str) == True
