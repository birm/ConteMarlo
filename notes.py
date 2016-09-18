import struct, math
"""
ConteMarlo
A "Monte-Carlo-Like" tester.
-Ryan Birmingham

The concept is simple (and probably already done better): detailed Monte-Carlo
but without the randomness.

Currently only works in 1d, but I want to generalize once I Get 1d working well.
I also want to construct tests first, so I know I don't break things.

Classes:
    Resolver - A generator for the next distribution value pair
    Distribution - A distribution, samplable at [0,1]
"""
class Resolver(Object):
    def __init__(self, distribution, *args, **kwargs):
        """Parse through resolver inputs, and prepare for generator."""
        # check if is existing Distribution, else, make it once
        if isinstance(distribution, Distribution):
            self.distribution = distribution
        else if callable(distribution):
            #  give it a "passed in" function
            self.distribution = Distribution(distribution)
        else:
            raise TypeError("Distribution passed is not callable.")
        self.layer = 1
        # set to one less than addressable int ln_2(max(INT) ) on system.
        if kwargs["high"]:
            self.high = kwargs["high"]
        else:
            self.high = (struct.calcsize("P") * 8)-1)
        # Finish preparation for generator for giving it an internal position.
        self.position = 1

    def next(self, n):
        """A generator to return the next [x,f(x)] pair from distribution."""
        a = 0.0
        while (a <= self.max):
            a = 2.0 ** math.ceil((math.log((self.position + 1), 2)))
            b = (2.0 * (a - self.position - 1) + 1) / a
            yield [a, self.distribution(a)]
            self.postion = self.position+1


class Distribution(Object):
    def __init__(name, *args, **kwargs):
        """Parse through and return a distributon object to call later.
        Any distribution input space should be [0,1]. Scale after."""
        supported = ["normal", "custom"]
        self.args=args
        self.kwargs=kwargs
        if name.lower() in supported:
            self.name=name
        else if isinstance(args[0], basestring):
            self.name = args[0]
        else if callable(args[0]):
            self.name = "passed_in"
            self.fcn = args[0]
        else:
            self.name = "custom"
        # call the proper construction function
        getattr(Distribution, self.name)()

    def passed_in(self):
        """We already have the function, just go on."""
        pass

    def __call__(self,  point):
        """Allow for the distribution to be called."""
        return self.fcn(point)

    def custom(self):
        """Take in a custom function, supplied by the user."""
        if callable(self.kwargs["dist"]):
            self.fcn = self.kwargs["dist"]
        else if callable(self.kwargs["distribution"]):
            self.fcn = self.kwargs["distribution"]
        else if callable(self.kwargs["fcn"]):
            self.fcn = self.kwargs["fcn"]
        else:
            raise ValueError("Did not find distribtion type " +
                             self.kwargs["distribution"]) # TODO fix
