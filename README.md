# Inventory System (Python)

## Description
This project is a simple inventory management system developed in Python. Its main purpose is to allow the user to manage products in an organized way through different functions.

The program lets the user add products, display the inventory, and calculate useful statistics. It is designed to practice fundamental programming concepts such as control flow, loops, and data structures.

---

## Functionality

The system is divided into several functions, each responsible for a specific task.

The function to add products asks the user for the product name, price, and amount. This information is stored in a dictionary and then added to a list that represents the inventory. This allows multiple products to be saved and managed easily.

Another function is responsible for displaying the inventory. It goes through the list of products using a loop and prints each one in a structured format. It also checks if the inventory is empty and shows a message if no products have been registered.

The statistics function calculates important values such as the total number of units and the total value of the inventory. It also identifies the most expensive and least expensive products. These calculations are done using built-in Python functions like `sum()`, `max()`, and `min()`.

Finally, there is a function that presents all these statistics in a clear and organized way. It also shows the subtotal for each product, which is calculated by multiplying the price by the amount.

---

## Data Handling
All products are stored in a list, where each product is represented as a dictionary containing its name, price, and amount. This structure makes it easy to access and manipulate the data when needed.

---

## Objective
The goal of this project is to strengthen the understanding of key programming concepts such as conditional statements, loops, and data structures, while building a functional and easy-to-read inventory system.

---

## Flow Chart
![Week 2 Flow Chart](https://github.com/user-attachments/assets/3b8e2e5c-a55f-4cae-97e8-e1ab2f53769f)

