from __future__ import division


def test_memoize_method_nested():
    from pytools import memoize_method_nested

    class SomeClass:
        def __init__(self):
            self.run_count = 0

        def f(self):

            @memoize_method_nested
            def inner(x):
                self.run_count += 1
                return 2*x

            inner(5)
            inner(5)

    sc = SomeClass()
    sc.f()
    assert sc.run_count == 1
