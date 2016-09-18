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
    Resolver - Gets the values for the resolution set.
    Distribution - A distribution, samplable at [0,1]
"""
class Resolver(Object):
    def __init__(self, distribution, *args, **kwargs):
        # check if is existing Distribution, else, make it once
        if isinstance(distribution, Distribution):
            self.distribution = distribution
        else if callable(distribution):
            #  give it a "passed in" function
            self.distribution = Distribution(distribution)
        else:
            raise BaseError("What?") # TODO fix
        self.layer = 1
        # set to one less than addressable int ln_2(max(INT) ) on system.
        if kwargs["high"]:
            self.high = kwargs["high"]
        else:
            self.high = (struct.calcsize("P") * 8)-1)


    def eval_layer(self, n):
        """Evaluate the distribution at the odd fractions of the power of 2."""
        return [distribution(point)
                for point in range(1,2**n) where m%2==1]
        # not sure if this is more efficient than computing layer separately

    def next(self, n):
        self.out_vec.extend(self.eval_layer(self.layer))
        self.layer = self.layer+1

    def result(self, n):
        # quickly order for linspace
        # determine what fraction a position represents, make sure long
        a = 2.0**math.ceil((math.log((n+1),2)))
        return (2.0*(a-n-1)+1)/a

class Distribution(Object):
    def __init__(name, *args, **kwargs):
        """Parse through and return a distributon object to call later."""
        """Any distribution input space should be [0,1]. Scale after."""
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
        getattr(Distribution, self.name)())

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
            raise BaseError("What?") # TODO fix
