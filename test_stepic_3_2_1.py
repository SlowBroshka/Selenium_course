def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        "expected {}. got {}".format(expected_result, actual_result)

def test_substring(full_string, substring):
    assert substring in full_string, \
        "expected \'{}\' to be substring of \'{}\'".format(substring, full_string)


test_substring('fulltext', 'some_value')