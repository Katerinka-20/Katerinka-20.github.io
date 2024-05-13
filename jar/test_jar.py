from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("abc")
    assert Jar().capacity == 12

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "\N{Cookie}" * 3

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
