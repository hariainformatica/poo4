import pytest
from reg.regExample import RegExample

def test_vocales():
    assert RegExample.buscar("Luna una cosa oso") == ["una", "oso"]

def test_url():
    assert RegExample.validURL("google") == False
    assert RegExample.validURL("https://www.google.es") == True
    assert RegExample.validURL("http://127.0.0.1") == True
