import bank

def test_value_zero():
    assert bank.value("здравствуйте, как дела?") == 0

def test_value_twenty():
    assert bank.value("зачем вы здесь?") == 20

def test_value_hundred():
    assert bank.value("привет, я пришел за кредитом") == 100
