import pytest
from Challengeoftheday import joinStrings

def test_endsPy():
    assert joinStrings.joinTwo("String","Fridge") == 'SFtrriidngge'
    assert joinStrings.joinTwo("Dog","Cat") == 'DCoagt'