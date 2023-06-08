import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    msg_error = "tipo inválido para message"
    key_error = "tipo inválido para key"

    assert encrypt_message(message="abcde", key=2) == "edc_ba"
    assert encrypt_message(message="abcde", key=3) == "cba_ed"
    assert encrypt_message(message="abcde", key=5) == "edcba"
    assert encrypt_message("edcba", 5) != "edcba"

    with pytest.raises(TypeError, match=key_error):
        encrypt_message("abcc", "abcde")

    with pytest.raises(TypeError, match=msg_error):
        encrypt_message(2, 2)
