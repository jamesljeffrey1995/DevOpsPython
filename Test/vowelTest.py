import pytest
from Challengeoftheday import countVowels

def test_endsPy():
    assert countVowels.countVowelsCalc("ilovepy") == 4
    assert countVowels.countVowelsCalc("ilovvepy") == 5