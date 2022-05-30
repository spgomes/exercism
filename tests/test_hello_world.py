from src.helloWorld import hello


def test_hello_world():
    string_hello = hello()
    assert string_hello == 'Hello, world!'

