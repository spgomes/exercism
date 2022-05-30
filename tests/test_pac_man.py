from src.pac_man import eat_ghost, score, lose, win

def test_eat_ghost_has_power_touch_ghost():
    can_eat_ghost = eat_ghost(True, True)
    assert can_eat_ghost == True

def test_eat_ghost_not_has_power_touch_ghost():
    can_eat_ghost = eat_ghost(False, True)
    assert can_eat_ghost == False

def test_eat_ghost_has_power_not_touch_ghost():
    can_eat_ghost = eat_ghost(True, False)
    assert can_eat_ghost == False

def test_eat_ghost_not_has_power_not_touch_ghost():
    can_eat_ghost = eat_ghost(False, False)
    assert can_eat_ghost == False

def test_score_touch_power_not_touch_dot():
    pac_man_score = score(True, False)
    assert pac_man_score == True

def test_score_touch_power_touch_dot():
    pac_man_score = score(True, True)
    assert pac_man_score == True

def test_score_not_touch_power_touch_dot():
    pac_man_score = score(False, True)
    assert pac_man_score == True

def test_score_not_touch_power_not_touch_ghost():
    pac_man_score = score(False, False)
    assert pac_man_score == False

def test_lose_1():
    pac_man_lose = lose(False, True)
    assert pac_man_lose == True

def test_lose_2():
    pac_man_lose = lose(False, False)
    assert pac_man_lose == False

def test_lose_3():
    pac_man_lose = lose(True, True)
    assert pac_man_lose == False

def test_lose_4():
    pac_man_lose = lose(True, False)
    assert pac_man_lose == False

def test_win_eaten_dots_has_power():
    pac_man_win = win(True, True, True)
    assert pac_man_win == True

def test_win_not_eaten_dots_has_power():
    pac_man_win = win(False, True, True)
    assert pac_man_win == False

def test_win_eaten_dots_has_no_power_touch_ghost():
    pac_man_win = win(True, False, True)
    assert pac_man_win == False

def test_win_eaten_dots_has_no_power_dont_touch_ghost():
    pac_man_win = win(True, False, False)
    assert pac_man_win == True