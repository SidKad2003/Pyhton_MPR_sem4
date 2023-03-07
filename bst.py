import tkinter as tk

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.width = 800
        self.height = 600
        self.node_radius = 20
        self.node_distance = 50
        self.node_fill = 'white'
        self.node_outline = 'black'
        self.node_font = ('Arial', 10)
        self.canvas = tk.Canvas(width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.draw_node(self.root, self.width//2, self.node_distance, self.width//4)

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
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

visualizer = BSTVisualizer(root)
tk.mainloop()
