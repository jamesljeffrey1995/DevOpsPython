import pytest
from Challengeoftheday import alphaString

def test_endsPy():
    assert alphaString.stringSplit("Hello,world,this,is,me") == ['Hello', 'is', 'me', 'this', 'world']
    assert alphaString.stringSplit("Hello    ,world   ,this, is, me") == ['Hello', 'is', 'me', 'this', 'world']