"""
final_simulation.py has been created with the purpose of executing the simulation cleanly,
                    without any code being visible
"""
# Author Name: Sebastian Carp, Harmanpreet Singh
# Author Student ID: 001289569, 001289568
# Python interpreter used: Python 3.10

from customers import simulation
import threading


def run_simulation():
    # Create a threading.Event to be able to stop the simulation if needed
    stop_event = threading.Event()

    # Call the simulation function
    simulation(stop_event)


if __name__ == "__main__":
    # Run the simulation in this file
    run_simulation()
