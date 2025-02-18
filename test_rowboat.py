import pytest
import math
from main import RowBoat, Oars, Rower


def test_initial_state():
    boat = RowBoat()
    assert boat.coordinates == (0, 0)
    assert boat.speed == 0
    assert boat.angle == 0

def test_increase_speed():
    boat = RowBoat()
    boat.increase_speed(2)
    assert boat.speed == 1

def test_move_of_oars():
    boat = RowBoat()
    boat.move_of_oars(True, False)
    assert boat.angle == 15

    boat.move_of_oars(False, True)
    assert boat.angle == 0

    boat.move_of_oars(True, True)
    assert boat.angle == 0


def test_set_row_power():
    oars = Oars()
    oars.set_row_power(5)
    assert oars.row_power == 5

def test_set_row_frequency():
    oars = Oars()
    oars.set_row_frequency(3)
    assert oars.row_frequency == 3


def test_operate_oars():
    rower = Rower(strength=4, stamina=3)
    oars = Oars()
    boat = RowBoat()

    rower.operate_oars(oars, boat)

    assert oars.row_power == 4
    assert boat.speed == 4 * 0.5

def test_reduce_stamina():
    rower = Rower(stamina=2)

    rower.reduce_stamina()
    assert rower.stamina == 1

    rower.reduce_stamina()
    assert rower.stamina == 0
    assert rower.tired is True

def test_rest():
    rower = Rower(stamina=0)
    rower.rest()
    assert rower.stamina == 10
    assert rower.tired is False
