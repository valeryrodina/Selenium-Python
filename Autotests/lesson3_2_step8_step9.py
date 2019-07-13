
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, "expected " + expected_result + ", got " + actual_result


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)
