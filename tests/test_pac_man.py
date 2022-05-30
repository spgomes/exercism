from src.pac_man import eat_ghost, score, lose

def test_eat_ghost_1():
    can_eat_ghost = eat_ghost(True, True)
    assert can_eat_ghost == True

def test_eat_ghost_2():
    can_eat_ghost = eat_ghost(False, True)
    assert can_eat_ghost == False

def test_eat_ghost_3():
    can_eat_ghost = eat_ghost(True, False)
    assert can_eat_ghost == False

def test_eat_ghost_4():
    can_eat_ghost = eat_ghost(False, False)
    assert can_eat_ghost == False

def test_score_1():
    pac_man_score = score(True, False)
    assert pac_man_score == True

def test_score_2():
    pac_man_score = score(True, True)
    assert pac_man_score == True

def test_score_3():
    pac_man_score = score(False, True)
    assert pac_man_score == True

def test_score_4():
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

def test_win_1():
    pac_man_win = win(True, test_lose_2)
    assert pac_man_win == True