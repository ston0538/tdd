# 곱셈 테스트 p.43
def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10

# NameError: name 'Dollar' is not defined
