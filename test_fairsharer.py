import fairsharer


def test_fair_sharer():

    assert fairsharer.fair_sharer([0, 1000, 800, 1100], 2) == [210.0, 800.0, 1010.0, 880.0]
