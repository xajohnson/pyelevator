import pytest
import pyelevator
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def controller():
    return pyelevator.Controller(1, 10)


def test_move_elevator(controller):
    assert controller.time == 0
    elevator = controller.elevators[0]
    elevator.destination = controller.floors[1]

    for i in range(0, 3):
        controller.tick()
        assert elevator.velocity > 0.0

    controller.tick()
    assert elevator.elevation == controller.floors[1].elevation
    assert elevator.velocity == 0.0

