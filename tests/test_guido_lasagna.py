from src.guido_lasagna import bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes

def test_bake_time_remaining():
    still_remaining = bake_time_remaining(30)
    assert 10

def test_preparation_time_in_minutes():
    preparation_time = preparation_time_in_minutes(2)
    assert 4

def test_elapsed_time_minutes():
    elapsed_time_in_minutes(3,20)
    assert 26
