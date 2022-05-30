

def eat_ghost(has_power:bool, touch_ghost:bool) -> bool:
    if has_power is True and touch_ghost is True:
        return True
    return False

def score(touch_power_pellet:bool, touch_dot:bool) -> bool:
    if touch_power_pellet is False and touch_dot is False:
        return False
    return True

def lose(has_power_pellet:bool, touch_ghost:bool) -> bool:
    if has_power_pellet is False and touch_ghost is True:
        return True
    return False

def win(eaten_all_dots:bool, has_power:bool, touch_ghost:bool) -> bool:
    if eaten_all_dots is False:
        return False
    if has_power is False and touch_ghost is True:
        return False
    return True
