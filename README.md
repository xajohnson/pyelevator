# Simple Elevator Simulator

Simulates an elevator.  Written in python.  Graphical UI.
It's a toy, not meant for serious use.

Requires
* Python 3
* pygame library

To run:

```python3 -m pyelevator```


### Code
The brains are in controller.py.  Key events are:

`on_elevator_arrived`

`on_floor_up_button_pushed`

`on_floor_down_button_pushed`

`on_elevator_panel_button_pushed`

Logic is very simple at the moment:
* Idle elevator is called to a floor when up/dn is pressed
* Elevator goes to floors lit on it's panel buttons

### Suggestions:
* Visit floors in the direction of travel
* Don't call an elevator if one is already on its way
* Add door opening and closing
* Add people to the elevators
* Implement load generator that simulates people going to different floors
* Implement more unit-tests
* Improve the graphics

