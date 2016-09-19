from contemarlo import *


def test_explicit_config():
    """Test the Distribution class given a function."""
    def custom_dist(input):
        return 0.5
    b = Distribution(custom_dist)

def test_bad_config():
    """Test a bad "distribution"."""
    with pytest.rasies(ValueError):
        a = Resolver("LemonDistribution")
