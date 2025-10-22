"""
lane_parent.py contains the parent class for "Lane" which defines arguments which will be inherited by any subclasses
"""
# Author Name: Sebastian Carp
# Author Student ID: 001289569
# Python interpreter used: Python 3.10


class Lane:
    def __init__(self, lane_type, lane_no, lane_status, customers_in_lane):  # arguments to be inherited by subclasses
        self.lane_type = lane_type
        self.lane_no = lane_no
        self.lane_status = lane_status
        self.customers_in_lane = customers_in_lane

    def set_status(self, lane_status):  # update status to open / closed
        self.lane_status = lane_status

    def get_lane_info(self):  # returns the lane info for a specific lane
        info = f'Lane Number ({self.lane_type}): {self.lane_no},' ' ' \
               f'Status: {self.lane_status},' ' ' \
               f'Customers in lane: {self.customers_in_lane}'
        return info
