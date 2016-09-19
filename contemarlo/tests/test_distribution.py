import pytest
# pytest dir fix?
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Resolver import Resolver
from Resolver import Resolver_md
from Distribution import Distribution

def test_explicit_config():
    """Test the Distribution class given a function."""
    def custom_dist(input):
        return 0.5
    b = Distribution(custom_dist)

def test_bad_config():
    """Test a bad "distribution"."""
    with pytest.raises(TypeError):
        a = Resolver("LemonDistribution")
