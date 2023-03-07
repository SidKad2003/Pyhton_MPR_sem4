import tkinter as tk
from tkinter import simpledialog

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BSTVisualizer:
    def __init__(self):
        self.root = None
        self.width = 800
        self.height = 600
        self.node_radius = 20
        self.node_distance = 50
        self.node_fill = 'white'
        self.node_outline = 'black'
        self.node_font = ('Arial', 10)
        self.canvas = tk.Canvas(width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.add_node)

    def add_node(self, event):
        x, y = event.x, event.y
        value = int(tk.simpledialog.askstring('Add node', 'Enter a value for the new node:'))
        self.root = self.insert(self.root, value)
        self.canvas.delete('all')
        self.draw_node(self.root, self.width//2, self.node_distance, self.width//4)

    def insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        return node

    def draw_node(self, node, x, y, level):
        if node is None:
            return

        self.canvas.create_oval(x-self.node_radius, y-self.node_radius, 
                                x+self.node_radius, y+self.node_radius, 
                                fill=self.node_fill, outline=self.node_outline)
        self.canvas.create_text(x, y, text=str(node.value), font=self.node_font)

        if node.left:
            x_left = x - level//2
            y_left = y + self.node_distance
            self.canvas.create_line(x, y+self.node_radius, x_left, y_left-self.node_radius)
            self.draw_node(node.left, x_left, y_left, level//2)

        if node.right:
            x_right = x + level//2
            y_right = y + self.node_distance
            self.canvas.create_line(x, y+self.node_radius, x_right, y_right-self.node_radius)
            self.draw_node(node.right, x_right, y_right, level//2)

# Example usage:
visualizer = BSTVisualizer()
tk.mainloop()
