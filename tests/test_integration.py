from calculator.app import calculate

def test_full_addition_flow():
    result = calculate(5, "+", 3)
    assert result == 8

def test_clear_after_calculation():
    result = calculate(10, "-", 4)
    cleared = calculate(result, "C")
    assert cleared == 0