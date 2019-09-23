import pytest
from player import Player


@pytest.mark.parametrize("valid", map(lambda x: str(x), range(1, 10)))
def test_input(monkeypatch, valid):
    monkeypatch.setattr('builtins.input', lambda _: valid)
    p = Player("X")
    x = p.choose_tile()
    assert x == int(valid)


@pytest.mark.parametrize("invalid", ["123", "-32", "123 3    ", "1.0"])
def test_input_invalid_num(monkeypatch, invalid):
    monkeypatch.setattr('builtins.input', lambda _: invalid)
    p = Player("X")
    x = p.choose_tile()
    assert x is None


def test_input_non_ascii(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Ǎ ǖ 2 ǘ ǚ ǜ")
    p = Player("X")
    x = p.choose_tile()
    assert x is None


@pytest.mark.parametrize("user_input", ["Y", "y", "Y    ", "  y "])
def test_play_again_yes(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    p = Player("X")
    x = p.play_again()
    assert x


@pytest.mark.parametrize("user_input", ["N", "n", " N  ", " n "])
def test_play_again_no(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    p = Player("X")
    x = p.play_again()
    assert not x


@pytest.mark.parametrize("user_input", ["da s", "ǘ", " 213 ", " dfg "])
def test_play_again_bad(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    p = Player("X")
    x = p.play_again()
    assert not x
