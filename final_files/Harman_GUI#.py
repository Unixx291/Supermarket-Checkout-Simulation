import random
import tkinter as tk
import threading
import time
from customers import simulation
import os


class Customer:
    def __init__(self, customer_id, num_items):
        self.customer_id = customer_id
        self.num_items = num_items

    def _calculate_checkout_times(self):
        regular_lane_time = round(3 + self.num_items * 0.1, 2)
        self_checkout_time = round(2 + self.num_items * 0.1, 2)
        return regular_lane_time, self_checkout_time

    def _check_award_eligibility(self, winning_probability=0.1):
        return self.num_items >= 10 and random.random() < winning_probability

    def generate_info(self):
        regular_lane_time, self_checkout_time = self._calculate_checkout_times()
        won_lottery = self._check_award_eligibility()
        title = f"Customer {self.customer_id} - Items: {self.num_items}"
        text = f"Self-checkout: {self_checkout_time} seconds\nRegular Lane: {regular_lane_time} seconds\nLottery: {'Won' if won_lottery else 'Lost'}"
        return title, text


def run_simulation(stop_event):
    simulation(stop_event=stop_event)


class MyGUI:
    def __init__(self):
        self.simulation_thread = threading.Thread(target=run_simulation, args=(self.stop_simulation,))
        self.stop_simulation_flag = threading.Event()
        self.customer_count = 0
        self.window = tk.Tk()
        self.window.geometry('800x600')
        self.window.title("Customer Simulation")
        self.label_customer_count = tk.Label(self.window, text=f'Number of Customers: {self.customer_count}',
                                             font=('Arial', 16))
        self.label_customer_count.pack(pady=10)
        self.frame_customer_info = tk.Frame(self.window)
        self.frame_customer_info.pack(pady=10, expand=True, fill=tk.BOTH)
        self.text_customer_info = tk.Text(self.frame_customer_info, height=20, width=80, font=('Arial', 12))
        self.text_customer_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.frame_customer_info, command=self.text_customer_info.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_customer_info.config(yscrollcommand=self.scrollbar.set)
        self.btn_generate = tk.Button(self.window, text='Start Simulation', font=('Arial', 16),
                                      command=self.start_simulation)
        self.btn_generate.pack(pady=1)
        self.btn_generate_f2 = tk.Button(self.window, text='Start F2', font=('Arial', 16), command=self.start_f1)
        self.btn_generate_f2.pack(pady=1)
        self.btn_stop = tk.Button(self.window, text='Stop Simulation', font=('Arial', 16), command=self.stop_simulation)
        self.btn_stop.pack(pady=1)
        self.btn_exit = tk.Button(self.window, text='Exit', font=('Arial', 16), command=self.exit_simulation)
        self.btn_exit.pack(pady=1)
        self.window.mainloop()

    def start_simulation(self):
        self.simulation_thread = threading.Thread(target=run_simulation, args=(self.stop_simulation_flag,))
        self.simulation_thread.start()

    def start_f1(self):
        self.customer_count = random_customer_count()
        self.label_customer_count.config(text=f'Number of Customers: {self.customer_count}')
        self.stop_simulation_flag.clear()
        self.generate_customers()

    def generate_customers(self):
        customers_info = []
        for customer_id in range(1, self.customer_count + 1):
            if self.stop_simulation_flag.is_set():
                break
            num_items = random.randint(1, 20)
            customer_instance = Customer(customer_id, num_items)
            title, text = customer_instance.generate_info()
            customers_info.append((title, text))
            self.display_customer_info(customers_info)
            time.sleep(2)

    def stop_simulation(self):
        if self.simulation_thread is not None and self.simulation_thread.is_alive():
            self.stop_simulation_flag.set()

    @staticmethod
    def exit_simulation():
        os._exit(0)

    def display_customer_info(self, customers_info):
        self.text_customer_info.delete(1.0, tk.END)
        for title, text in customers_info:
            self.text_customer_info.insert(tk.END, f"{title}\n{text}\n\n")
        self.text_customer_info.update()


def random_customer_count():
    return random.randint(1, 10)


if __name__ == "__main__":
    my_gui = MyGUI()
