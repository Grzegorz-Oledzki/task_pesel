from .utils import check_pesel

valid_pesels = [
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


invalid_valid_pesels = [
    "72062279122",
    "59091241227",
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


def test_valid_pesels():
    for pesel in valid_pesels:
        result, _ = check_pesel(pesel)
        assert result == True


def test_invalid_pesels():
    for pesel in invalid_valid_pesels:
        print(pesel)
        result, _ = check_pesel(pesel)
        assert result == False
