from callLimit import call_limit


@call_limit(3)
def f():
    print("f()")


@call_limit(1)
def g():
    print("g()")


for _ in range(3):
    f()
    g()
