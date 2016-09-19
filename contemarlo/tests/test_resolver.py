import pytest
# pytest dir fix?
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Resolver import Resolver
from Resolver import Resolver_md
from Distribution import Distribution

def test_min_config():
    """Test the Resolver class given a function."""
    def custom_dist(input):
        return 0.5
    a = Resolver(custom_dist)

def test_explicit_config():
    """Test the Resolver class given a Distrbution object."""
    def custom_dist(input):
        return 0.5
    b = Distribution(custom_dist)
    a = Resolver(b)

def test_bad_config():
    """Test a bad "distribution" for the resolver."""
    with pytest.raises(TypeError):
        a = Resolver(1)

def test_iterator_round():
    """Ensure that the interator uses float instead of int."""
    def custom_dist(input):
        return 0.5
    a = Resolver(custom_dist)
    assert next(a.next()) == [0.25,0.5]

def test_iterator_end():
    """Ensure that the iterator will end at some point in safe mode."""
    def custom_dist(input):
        return 0.5
    a = Resolver(custom_dist)
    a.high = 1
    with pytest.raises(Warning):
        for i in range (1,3):
            next(a.next())
