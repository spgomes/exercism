

def eat_ghost(has_power:bool, touch_ghost:bool) -> bool:
    if has_power == True and touch_ghost == True:
        return True
    else:
        return False

def score(touch_power_pellet:bool, touch_dot:bool) -> bool:
    if touch_power_pellet == False and touch_dot == False:
        return False
    else:
        return True

def lose(has_power_pellet:bool, touch_ghost:bool) -> bool:
    if has_power_pellet == False and touch_ghost == True:
        return True
    else:
        return False