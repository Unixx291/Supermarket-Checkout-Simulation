"""
regular_lane.py has the functionality of inheriting from the parent class "Lane" in the subclass RegLane
                also defines the structure (variables) for the 5 regular lanes used within the simulation
"""
# Author Name: Sebastian Carp
# Author Student ID: 001289569
# Python interpreter used: Python 3.10

# imports for python file to be functional:
from lane_parent import Lane
from self_service import print_self_service_lane_info
from self_service import lane6
from datetime import datetime


def display_lane_saturation():
    """
    In case all lanes are full, display lane saturation (the amount of customers in each lane)
    """
    if all(lane.customers_in_lane >= 5 for lane in list_of_regular_lanes) and lane6.customers_in_lane >= 15:
        print('All lanes are full. Lane saturation:')
        for lane in list_of_regular_lanes:
            print(f"Lane {lane.lane_no}: {lane.customers_in_lane}/5 customers")
        print(f'Lane {lane6.lane_no}: {lane6.customers_in_lane}/15 customers')


def get_total_customers_in_all_lanes():
    """
    Returns the sum of the customers in all lanes as an integer
    :return:
    """
    total_customers = sum(lane.customers_in_lane for lane in list_of_all_lanes)
    return total_customers


def timestamp(start_time):
    """
    Returns the elapsed time since the start of the simulation
    :param start_time:
    :return:
    """
    current_time = datetime.now()
    elapsed_time = current_time - start_time
    elapsed_time_info = str(elapsed_time).split('.')[0]  # formatting elapsed time
    return elapsed_time_info


# marks the start of the simulation with the current time
simulation_start_time = datetime.now()


def print_lanes_info():  # improved by OpenAi
    """
    Returns the info of all lanes, including saturation if lanes are full
    :return:
    """

    # checks for lanes with 0 customers in them and closes them
    for lane in list_of_regular_lanes:
        if lane.customers_in_lane == 0:
            lane.set_status('closed')

    # prints elapsed time and customers waiting to check out
    print(
        f'Total customers waiting to checkout at {timestamp(simulation_start_time)} is '
        f'{get_total_customers_in_all_lanes()}')

    # goes through a series of checks to decide if the next lane should open
    # prints all the regular lanes info
    for idx, lane in enumerate(list_of_regular_lanes, start=1):
        lane.open_next_lane()
        print(lane.get_lane_info())

    # prints the self-service lane info
    print_self_service_lane_info()

    # upon the lanes being full, prints lane saturation
    display_lane_saturation()


class RegLane(Lane):
    """
    Subclass of "Lane" for the regular lanes, inheriting its attributes
    Contains method for checking if the next lane needs to be opened or not
    """
    def __init__(self, lane_type, lane_no, lane_status, customers_in_lane):
        super().__init__(lane_type, lane_no, lane_status, customers_in_lane)  # inheriting from parent class

    # checking if the next lane needs to be opened or not
    def open_next_lane(self):
        for lane in list_of_regular_lanes:
            if self.customers_in_lane >= 5 and lane.lane_status == 'closed' and lane.customers_in_lane > 0:  # check
                # if conditions met
                lane.set_status('open')  # opens next lane if conditions met
                break  # exit the loop once a lane is opened to open only the next one


# assigns lane type, lane number, lane status, and number of customers in lane
# data types for each attribute are mapped (str, int, str, int)
lane1 = RegLane('Reg', 1, 'open', 0)
lane2 = RegLane('Reg', 2, 'closed', 0)
lane3 = RegLane('Reg', 3, 'closed', 0)
lane4 = RegLane('Reg', 4, 'closed', 0)
lane5 = RegLane('Reg', 5, 'closed', 0)

# defining lists for lanes which will be used to manage customers
list_of_regular_lanes = [lane1, lane2, lane3, lane4, lane5]  # list of regular lanes
list_of_all_lanes = [lane1, lane2, lane3, lane4, lane5, lane6]  # list of all lanes
