import math
from boat import RowBoat, Oars, Rower, BoatController


def test_rowboat_move_forward():
    boat = RowBoat(coordinates=(0, 0), angle=0)
    distance = 10

    boat.move_forward(distance)

    expected_coordinates = (10, 0)
    assert math.isclose(boat.coordinates[0], expected_coordinates[0], rel_tol=1e-9)
    assert math.isclose(boat.coordinates[1], expected_coordinates[1], rel_tol=1e-9)

def test_rowboat_turn_left():
    boat = RowBoat(angle=0)
    degrees = 90

    boat.turn_left(degrees)

    expected_angle = -90
    assert math.isclose(boat.angle, expected_angle, rel_tol=1e-9)

def test_rowboat_turn_right():
    boat = RowBoat(angle=0)
    degrees = 90

    boat.turn_right(degrees)

    expected_angle = 90
    assert math.isclose(boat.angle, expected_angle, rel_tol=1e-9)

def test_oars_get_power():
    oars = Oars(power=2)

    power = oars.get_power()

    assert power == 2

def test_rower_row():
    rower = Rower(strength=1, stamina=5)
    oars = Oars(power=1)
    boat = RowBoat(coordinates=(0, 0), angle=0)
    target_x, target_y = 10, 0

    rower.row(oars, boat, target_x, target_y)

    assert math.isclose(boat.coordinates[0], 1, rel_tol=1e-9)
    assert rower.stamina == 4

def test_rower_rest():
    rower = Rower(strength=1, stamina=0)

    rower.rest()

    assert rower.stamina == 10
    assert not rower.is_tired()

def test_boatcontroller_calculate_target_angle():
    boat = RowBoat(coordinates=(0, 0), angle=0)
    controller = BoatController(boat, Rower(), Oars())
    target_x, target_y = 10, 0

    target_angle = controller.calculate_target_angle(target_x, target_y)

    assert math.isclose(target_angle, 0, rel_tol=1e-9)

def test_boatcontroller_turn_towards_target():
    boat = RowBoat(coordinates=(0, 0), angle=0)
    controller = BoatController(boat, Rower(), Oars())
    target_angle = 90

    controller.turn_towards_target(target_angle)

    assert math.isclose(boat.angle, 10, rel_tol=1e-9)

def test_boatcontroller_move_to_target():
    boat = RowBoat(coordinates=(0, 0), angle=0)
    rower = Rower(strength=1, stamina=10)
    oars = Oars(power=1)
    controller = BoatController(boat, rower, oars)
    target_x, target_y = 5, 0

    controller.move_to_target(target_x, target_y)

    assert math.isclose(boat.coordinates[0], 5, rel_tol=1e-9)
    assert math.isclose(boat.coordinates[1], 0, rel_tol=1e-9)

