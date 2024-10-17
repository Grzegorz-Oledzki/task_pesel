from task.pesel_corectness_checker import PeselValidator
import pytest

TRUE_PESELS = [
    "72062279128",
    "59091281227",
    "96062327322",
    "74051192629",
    "75021469417",
    "68082478928",
    "76061285768",
    "49022613533",
    "90060938748",
    "81101852189",
    "49111046468",
    "61120467115",
    "89120173766",
    "85042062757",
    "76050332378",
]


FALSE_PESELS = [
    "72062279122",
    "abcabcacbab",
    "96062357322",
    "74061192629",
    "75021569417",
    "68082471928",
    "76061225768",
    "49022622533",
    "90060948748",
    "81101842189",
    "49111041468",
    "6",
    "891201766",
    "8504206227517",
    "76010332123123117",
]


@pytest.mark.parametrize("pesel", TRUE_PESELS)
def test_true_pesels_are_correct(pesel: str):
    assert PeselValidator(pesel).is_valid()


@pytest.mark.parametrize("pesel", FALSE_PESELS)
def test_false_pesels_are_incorrect(pesel: str):
    assert not PeselValidator(pesel).is_valid()
