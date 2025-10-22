"""
random_customer.py has the functionality of generating random customers with a random amount of items in their basket
"""
# Author Name: Harmanpreet Singh
# Author Student ID: 001289568
# Python interpreter used: Python 3.10

# random_customer.py

import random


class RandCustomer:
    def __init__(self, customer_num):
        """
        Initializes a Customer object with a given customer number.
        """
        self.customer_num = customer_num

    @staticmethod
    def generate_random_items():
        """
        Generates a random number of items between 1 and 30 for each customer.
        """
        return random.randint(1, 30)

    @staticmethod
    def calculate_checkout_times(num_items):
        """
        Calculates the time it takes to check out each customer's items in the regular lane and self-checkout.
        """
        regular_lane_time = (num_items * 4)  # checkout_time for regular_lane
        self_checkout_time = (num_items * 6)  # for self_checkout, calculate the time
        return round(regular_lane_time, 2), round(self_checkout_time, 2)

    @staticmethod
    def is_lottery_winner(num_items):
        """
        Determine if the customer wins the lottery
        :return:
        """
        return num_items >= 10 and random.randint(1,10) == 1  # creating 10% chances of anyone with more than 10 items wins lottery

    def generate_random_customers(self):

        """
        Generates a list of randomly generated customers.
        """
        customers = []
        for customer_number in range(1, self.customer_num + 1):
            number_of_items = self.generate_random_items()  # generates random of items
            regular_lane_time, self_checkout_time = self.calculate_checkout_times(
                number_of_items)  # calculates the checkout_time
            checkout_status = 'incomplete'

            won_lottery = self.is_lottery_winner(number_of_items)

            customer_info = {
                'customer_id': customer_number,
                'num_items': number_of_items,
                'won_lottery': won_lottery,
                'self_checkout_time': self_checkout_time,
                'regular_lane_time': regular_lane_time,
                'checkout_status': checkout_status
            }

            customers.append(customer_info)

        return customers


customer_in_total = random.randint(1, 10)  # generates a random number of customers
print(f"There are a total of {customer_in_total} customers")  # prints how many customers there are in total
c = RandCustomer(customer_in_total)  # creates a variable of the class

# / uses a method within the class to assign the customer info and
# stores the data in a variable "generated_customers" /
generated_customers = c.generate_random_customers()

# prints the customer information
for customer in generated_customers:
    print(f"\nCustomer {customer['customer_id']}:")
    print(f"Number of items: {customer['num_items']}")
    print(f"Self checkout time: {customer['self_checkout_time']} seconds")
    print(f"Regular lane time: {customer['regular_lane_time']} seconds")
    if customer['won_lottery']:
        print("Congratulations! They won the lottery.")
    else:
        print("They did not win the lottery.")
