import time
import tkinter as tk
from regular_lane import print_lanes_info
from customers import simulation
import threading
import os

class SimulationApp:
    def __init__(self, master):
        self.master = master
        master.title("Supermarket Simulation")

        self.start_button = tk.Button(master, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

        self.run_feature_button = tk.Button(master, text="Run Sub-Feature", command=self.run_sub_feature)
        self.run_feature_button.pack()

        self.stop_button = tk.Button(master, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_simulation)
        self.exit_button.pack()

        self.simulation_thread = None
        self.stop_event = threading.Event()

    def start_simulation(self):
        self.stop_event.clear()
        self.simulation_thread = threading.Thread(target=self.run_simulation)
        self.simulation_thread.start()

    def run_simulation(self):
        simulation()

    @staticmethod
    def run_sub_feature():
        print("Running Sub-Feature for F1:")
        print_lanes_info()

    def stop_simulation(self):
        if self.simulation_thread is not None and self.simulation_thread.is_alive():




    def exit_simulation(self):
        os._exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
