from quick_calc.calculator import Calculator

def test_full_addition_flow():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_after_operation():
    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20

    cleared = calc.clear()
    assert cleared == 0p