"""
customers.py is used to run the supermarket simulation
            inheritance, abstraction and encapsulation have all been used for the file to run accordingly
"""
# Author Name: Sebastian Carp, Harmanpreet Singh
# Author Student ID: 001289569, 001289568
# Python interpreter used: Python 3.10


import random
import time
import threading
from regular_lane import print_lanes_info, list_of_regular_lanes, lane1, lane2, lane3, lane4, lane5, lane6
from random_customer import

# define a threading lock for printing
# / Each lane info update may seem 'laggy', but this ensures no printing
# overlapping when two customers check out at the same time, no matter the lane.
# The only time that overlapping might happen is when
# customers are generated and a customer checks out at the same time /
print_lock = threading.Lock()


class Customer:
    """
    Class to which all the customers will be modelled by
    """
    def __init__(self, customer_number, number_of_items, checkout_time, checkout_status):
        self.customer_number = customer_number
        self.number_of_items = number_of_items
        self.checkout_time = checkout_time
        self.checkout_status = checkout_status
        self.assigned_lane = None  # Initialize initial assigned_lane attribute
        self.lottery_winner = False  # Initialize lottery_winner attribute

    def add_customer_to_lane(self):
        """
        Adds customers to lanes based on basket size, lane criteria and lane capacity
        :return:
        """
        if self.number_of_items < 10:  # If a customer has less than 10 items, he can go to self-checkout
            if lane6.customers_in_lane >= 15:  # If the self-checkout lane is full, customers will go to a regular lane
                for lane in list_of_regular_lanes:  # Checking which regular lane is best to join
                    if lane.customers_in_lane < 5:
                        lane.customers_in_lane += 1
                        self.assigned_lane = lane  # Assigns customer to regular lane
                        break
                else:
                    min_lane = min(list_of_regular_lanes, key=lambda x: x.customers_in_lane)
                    min_lane.customers_in_lane += 1
                    self.assigned_lane = min_lane  # Assigns customer to next less crowded lane
            else:
                lane6.customers_in_lane += 1  # Adding customer to self-checkout lane
                self.assigned_lane = lane6
        elif self.number_of_items >= 10:  # If a customer has more than 10 items, he needs to go to a regular lane
            for lane in list_of_regular_lanes:  # Checking which regular lane is best to join
                if lane.customers_in_lane < 5:
                    lane.customers_in_lane += 1
                    self.assigned_lane = lane  # Assigns customer to lane
                    break
            else:
                min_lane = min(list_of_regular_lanes, key=lambda x: x.customers_in_lane)
                min_lane.customers_in_lane += 1
                self.assigned_lane = min_lane  # Assigns customer to next less crowded lane

    def remove_customer_from_lane(self):
        """
        Removes a customer from their lane based on basket size
        :return:
        """
        if self.checkout_status == 'complete':
            if self.number_of_items < 10:
                lane6.customers_in_lane -= 1
            if self.number_of_items > 10:
                if self.assigned_lane:
                    self.assigned_lane.customers_in_lane -= 1

    def simulate_checkout_and_remove_customer(self):
        """
        Using real elapsed time since the start of the simulation to set a customers checkout status to complete
        and remove them from their lane
        :return:
        """
        start_time = time.time()  # Record the start time of the simulation

        while time.time() - start_time < self.checkout_time:
            # Keep checking if the checkout time has elapsed
            pass

        self.checkout_status = 'complete'  # Update the checkout status to 'complete'

        # Check if the customer wins the lottery
        self.lottery_winner = self.checkout_status == 'complete' and self.is_lottery_winner()
        if self.lottery_winner:  # If the customer meets the conditions for winning the lottery
            print(f'Customer {self.customer_number} has won the lottery')  # Prints the customer number which has won

        self.remove_customer_from_lane()  # Removes the customer from the lane

        # Printing the lanes info with a lock to ensure synchronized printing
        with print_lock:
            print_lanes_info()

    # def is_lottery_winner(self):
    #     """
    #     Determine if the customer wins the lottery
    #     :return:
    #     """
    #     return self.number_of_items >= 10 and random.randint(1, 10) == 1


def simulate_checkout_for_lane(customers):
    """
    Removes the customers given
    :param customers:
    :return:
    """
    for customer in customers:
        customer.simulate_checkout_and_remove_customer()


def generate_random_customer(customer_number):
    """
    Generates a random customer
    :param customer_number:
    :return:
    """
    number_of_items = random.randint(1, 30)  # Random number of items between 1 and 30
    checkout_time = number_of_items * 6 if number_of_items < 10 else number_of_items * 4
    # checkout time --> x items * 6 for self-checkout; x items * 4 for regular lanes
    checkout_status = 'incomplete'  # Initial checkout status

    # Stores each customer as a variable of the Customer class
    return Customer(customer_number, number_of_items, checkout_time, checkout_status)


def get_customers_in_lane(customers, lane):
    """
    Returns the customers within a specific lane
    :param customers:
    :param lane:
    :return:
    """
    return [customer for customer in customers if customer.assigned_lane == lane]


def simulation(stop_condition):
    for _ in range(8):
        if stop_condition():
            break  # Exit the loop if the stop condition is True

        num_customers = random.randint(1, 10)
        random_customers = [generate_random_customer(i) for i in range(1, num_customers + 1)]

        for customer in random_customers:
            customer.add_customer_to_lane()

        lanes = [lane1, lane2, lane3, lane4, lane5, lane6]
        lane_customers = [get_customers_in_lane(random_customers, lane) for lane in lanes]
        lane6_customers_to_checkout = lane_customers[-1][:8]

        print(f" {num_customers} customers added. Simulating checkout...")
        print_lanes_info()

        threads = [threading.Thread(target=simulate_checkout_for_lane, args=(lane_customers[i],)) for i in range(5)]
        threads += [threading.Thread(target=customer.simulate_checkout_and_remove_customer) for customer in lane6_customers_to_checkout]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()  # Wait for all threads to finish before continuing

        time.sleep(30)

    print_lanes_info()
