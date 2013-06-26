import example


def test_example():
    assert example.REDIS_HOST != '127.0.0.1'
    assert example.REDIS_HOST == '127.0.0.1'
