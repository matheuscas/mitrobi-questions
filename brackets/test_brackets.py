from brackets.brackets import check_brackets

def test_trythy_inputs():
    assert check_brackets("{[]}") is True

def test_falsy_inputs():
    assert check_brackets("{{)") is False
    assert check_brackets("{{}(") is False
    assert check_brackets("{{})") is False
