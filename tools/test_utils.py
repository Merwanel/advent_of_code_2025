import typing

def shouldBeEqual(func: typing.Callable, kwargs: dict, expect: any):
    res = func(**kwargs)
    try:
        assert res == expect
    except :
        print(f"failed for {kwargs} : got {res}, expected {expect}")
