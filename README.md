# Supermarket-Checkout-Simulation
Python-based simulation of a supermarket checkout system that models customer arrivals, queue management, and cashier efficiency. Uses probability and timing logic to analyze waiting times and optimize checkout performance.


---------------
**🛒 Supermarket Checkout Simulation**
**🧭 Overview**

This project simulates a supermarket checkout system to study and optimize queue management, customer flow, and lane efficiency. It models both regular checkout lanes and a self-service lane, using object-oriented programming principles (inheritance, abstraction, and encapsulation) to represent real-world supermarket dynamics.

A Tkinter GUI is included for interactive control, allowing users to start, stop, and monitor the simulation visually.

**⚙️ Features:**

🧍 Dynamic customer generation: Randomly creates customers with varying basket sizes and checkout times

🧾 Lane management: Customers are automatically distributed between regular and self-service lanes

⏱️ Concurrent processing: Multithreading simulates multiple customers checking out simultaneously

🎰 Lottery system: Some customers with large baskets have a small chance of “winning”

🪟 Graphical interface (Tkinter): Start, stop, and monitor the simulation in real time

🧩 OOP design: Reusable lane classes with inheritance for regular and self-service checkouts

🧠 Technical Details

**Language:** Python 3.10

**Core Concepts:**

Object-Oriented Programming (OOP)

Multithreading

Discrete Event Simulation

GUI Development (Tkinter)

**Main Libraries:**

threading — to simulate simultaneous checkouts

random — for stochastic customer behavior

tkinter — for GUI

datetime — for time tracking
