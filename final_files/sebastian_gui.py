import tkinter as tk
from regular_lane import print_lanes_info
from customers import simulation
import threading
import os


class SimulationApp:
    def __init__(self, master):
        self.master = master
        master.title("Supermarket Simulation")

        # Button for starting the simulation
        self.start_button = tk.Button(master, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

        # Button for running sub feature v of F1
        self.run_feature_button = tk.Button(master, text="Run Sub-Feature", command=self.run_sub_feature)
        self.run_feature_button.pack()

        # Button for stopping simulation but not exiting the GUI window
        # / Because of the way the code logic works within the simulation() function, the loop of adding customers is
        # stopped, but the user needs to wait for the current batch of customers in the lane to check out before the
        # simulation stops /
        self.stop_button = tk.Button(master, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.pack()

        # Button for exiting the simulation and the GUI window
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_simulation)
        self.exit_button.pack()

        # Define flags and threads
        self.simulation_thread = None
        self.stop_event = threading.Event()

    def start_simulation(self):  # Start thread for running the simulation
        self.stop_event.clear()
        self.simulation_thread = threading.Thread(target=self.run_simulation, args=(self.stop_event,))
        self.simulation_thread.start()

    @staticmethod
    def run_simulation(stop_event):  # Run the simulation
        simulation(stop_event)

    @staticmethod
    def run_sub_feature():  # Run sub-feature v for F1
        print("Running Sub-Feature for F1:")
        print_lanes_info()

    def stop_simulation(self):  # Stop the simulation after the current batch of customers get removed
        if self.simulation_thread is not None and self.simulation_thread.is_alive():
            self.stop_event.set()  # Set the stop event to signal the simulation thread to stop

    # noinspection PyProtectedMember
    @staticmethod  # Forcefully exit both simulation and GUI window
    def exit_simulation():
        os._exit(0)


# run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
