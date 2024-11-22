import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")

        # Set the background color of the window to white
        self.root.configure(bg="white")

        # Create a canvas to draw the clock
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Radius of the clock
        self.radius = 150
        self.center = (200, 200)  # Center of the clock (x, y)
        
        # Draw the clock face
        self.draw_clock_face()

        # Update the clock every second
        self.update_time()

    def draw_clock_face(self):
        # Draw clock circle
        self.canvas.create_oval(self.center[0] - self.radius, self.center[1] - self.radius,
                                self.center[0] + self.radius, self.center[1] + self.radius, outline="black", width=2)

        # Draw clock numbers in black
        for i in range(1, 13):
            angle = math.radians(360 * (i / 12) - 90)  # Angle for each number
            x = self.center[0] + self.radius * 0.8 * math.cos(angle)
            y = self.center[1] + self.radius * 0.8 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Helvetica", 12), fill="black")

    def update_time(self):
        # Get the current time
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Clear the previous hands
        self.canvas.delete("hands")

        # Draw the clock hands
        self.draw_hand(hour * 30 + (minute / 60) * 30, self.radius * 0.5, "black", 6)  # Hour hand
        self.draw_hand(minute * 6, self.radius * 0.8, "blue", 4)  # Minute hand
        self.draw_hand(second * 6, self.radius * 0.9, "red", 2)  # Second hand

        # Update the time every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time)

    def draw_hand(self, angle, length, color, width):
        angle_rad = math.radians(angle - 90)  # Rotate clockwise
        x_end = self.center[0] + length * math.cos(angle_rad)
        y_end = self.center[1] + length * math.sin(angle_rad)
        self.canvas.create_line(self.center[0], self.center[1], x_end, y_end, fill=color, width=width, tags="hands")

if __name__ == "__main__":
    # Create the Tkinter window
    root = tk.Tk()

    # Create the AnalogClock instance
    clock = AnalogClock(root)

    # Start the Tkinter event loop
    root.mainloop()
