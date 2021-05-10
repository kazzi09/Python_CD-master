import lib

def test_increment():
    assert lib.increment(2,2) == 4
    assert lib.increment(2,3) == 5
    assert lib.increment(100,300) == 400
