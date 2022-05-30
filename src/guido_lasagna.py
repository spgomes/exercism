EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time_now):
    return EXPECTED_BAKE_TIME - time_now

def preparation_time_in_minutes(number_of_layers):
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, time_passed ):
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + time_passed

