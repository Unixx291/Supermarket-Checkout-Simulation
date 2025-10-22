"""
regular_lane.py has the functionality of inheriting from the parent class "Lane" in the subclass RegLane
                also defines the structure (variables) for the 5 regular lanes used within the simulation
"""
# Author Name: Sebastian Carp
# Author Student ID: 001289569
# Python interpreter used: Python 3.10

# imports for python file to be functional:
from lane_parent import Lane


def print_self_service_lane_info():
    """
    Prints the info of the self-service lane
    :return:
    """
    print(lane6.get_lane_info())  # uses parent class method


class SelfService(Lane):
    """
    Subclass of "Lane" for the self-service lane, inheriting its attributes
    """
    def __init__(self, lane_type, lane_no, lane_status, customers_in_lane):
        super().__init__(lane_type, lane_no, lane_status, customers_in_lane)


# assigns lane type, lane number, lane status, and number of customers in lane
# data types for each attribute are mapped (str, int, str, int)
lane6 = SelfService('Slf', 6, "open", 0)
