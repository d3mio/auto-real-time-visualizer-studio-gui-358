import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time

class RealTimeDataVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title('Real-Time Data Visualizer Studio GUI #358')
        self.root.geometry('800x600')
        self.root.configure(bg='#2E3440')
        self.setup_ui()
        self.data_stream = []
        self.update_thread = threading.Thread(target=self.update_data, daemon=True)
        self.update_thread.start()

    def setup_ui(self):
        self.main_frame = ttk.Frame(self.root, padding='10')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.chart_frame = ttk.Frame(self.main_frame)
        self.chart_frame.pack(fill=tk.BOTH, expand=True)

        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_facecolor('#3B4252')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill=tk.X, pady=10)

        self.start_button = ttk.Button(self.control_frame, text='Start', command=self.start_data_stream)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(self.control_frame, text='Stop', command=self.stop_data_stream)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ttk.Button(self.control_frame, text='Clear', command=self.clear_chart)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(self.control_frame, text='Status: Idle', foreground='#88C0D0')
        self.status_label.pack(side=tk.RIGHT, padx=5)

    def start_data_stream(self):
        self.status_label.config(text='Status: Streaming')
        self.data_stream = []

    def stop_data_stream(self):
        self.status_label.config(text='Status: Stopped')

    def clear_chart(self):
        self.ax.clear()
        self.ax.set_facecolor('#3B4252')
        self.canvas.draw()

    def update_data(self):
        while True:
            if self.status_label.cget('text') == 'Status: Streaming':
                new_data = random.randint(0, 100)
                self.data_stream.append(new_data)
                self.ax.clear()
                self.ax.plot(self.data_stream, color='#88C0D0')
                self.ax.set_facecolor('#3B4252')
                self.canvas.draw()
            time.sleep(1)

if __name__ == '__main__':
    root = tk.Tk()
    app = RealTimeDataVisualizer(root)
    root.mainloop()