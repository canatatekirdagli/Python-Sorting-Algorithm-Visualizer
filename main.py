import tkinter as tk
from tkinter import ttk
import random
import time
import tkinter.messagebox as messagebox

is_animation_running = False

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if not is_animation_running:
                return
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_display(arr)
                time.sleep(speed_slider.get())
                window.update()

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        update_display(arr)
        time.sleep(speed_slider.get())
        window.update()

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update_display(arr)
            time.sleep(speed_slider.get())
            window.update()
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def update_display(arr):
    canvas.delete("all")
    bar_width = canvas_width // len(arr)
    bar_height_ratio = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='sky blue', outline='white')
    window.update_idletasks()

def create_array():
    size = int(size_spinbox.get())
    elements = list(map(int, list_text.get("1.0", tk.END).split()))

    if len(elements) < size:
        messagebox.showerror("Hata", "Dizi boyutundan daha az sayı girdiniz.")
        return None
    elif len(elements) > size:
        messagebox.showerror("Hata", "Dizi boyutundan daha fazla sayı girdiniz.")
        return None

    return elements

def create_graph():
    graph_type = graph_combo.get()
    array = create_array()
    if array is None:
        return
    if graph_type == 'Scatter':
        scatter_graph(array)
    elif graph_type == 'Bar':
        bar_graph(array)
    elif graph_type == 'Stem':
        stem_graph(array)

def scatter_graph(arr):
    canvas.delete("all")
    x_interval = canvas_width / len(arr)
    y_interval = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x = i * x_interval
        y = canvas_height - value * y_interval
        canvas.create_oval(x, y, x, y, width=3, fill='sky blue')
    window.update_idletasks()

def bar_graph(arr):
    canvas.delete("all")
    bar_width = canvas_width // len(arr)
    bar_height_ratio = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='sky blue', outline='white')
    window.update_idletasks()

def stem_graph(arr):
    canvas.delete("all")
    x_interval = canvas_width / len(arr)
    y_interval = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x = i * x_interval
        y = canvas_height - value * y_interval
        canvas.create_line(x, canvas_height, x, y, width=2)
    window.update_idletasks()

def start_animation():
    global is_animation_running
    is_animation_running = True

    selected_algorithm = algorithm_combo.get()
    array = create_array()
    if array is None:
        return
    create_graph()
    if selected_algorithm == 'Bubble Sort':
        bubble_sort(array)
    elif selected_algorithm == 'Quick Sort':
        quick_sort(array, 0, len(array)-1)

def stop_animation():
    global is_animation_running
    is_animation_running = False

def continue_animation():
    selected_algorithm = algorithm_combo.get()
    array = create_array()
    if array is None:
        return
    if selected_algorithm == 'Bubble Sort':
        bubble_sort(array)
    elif selected_algorithm == 'Quick Sort':
        quick_sort(array, 0, len(array)-1)

def reset():
    canvas.delete("all")
    size_spinbox.delete(0, tk.END)
    list_text.delete("1.0", tk.END)

window = tk.Tk()
window.title('Sıralama Algoritması Paneli')
window.geometry('1100x500')

canvas_width = 800
canvas_height = 400

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(side=tk.LEFT, padx=20, pady=20)

settings_frame = tk.Frame(window)
settings_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Size and List Input Section
size_label = tk.Label(settings_frame, text='Liste Boyutu:', font=('Arial', 12))
size_label.pack()

size_spinbox = tk.Spinbox(settings_frame, from_=1, to=100, font=('Arial', 12))
size_spinbox.pack()

list_label = tk.Label(settings_frame, text='Liste Elemanları:', font=('Arial', 12))
list_label.pack()

list_text = tk.Text(settings_frame, height=4, width=20, font=('Arial', 12))
list_text.pack()

# Speed Setting Section
speed_label = tk.Label(settings_frame, text='Sıralama Hızı:', font=('Arial', 12))
speed_label.pack()

speed_slider = ttk.Scale(settings_frame, from_=1.0, to=0.1, length=200, orient='horizontal')
speed_slider.pack()

# Sorting Algorithms Section
algorithm_label = tk.Label(settings_frame, text='Sıralama Algoritması:', font=('Arial', 12))
algorithm_label.pack()

algorithm_combo = ttk.Combobox(settings_frame, values=['Bubble Sort', 'Quick Sort'], font=('Arial', 12))
algorithm_combo.current(0)
algorithm_combo.pack()

# Graph Types Section
graph_label = tk.Label(settings_frame, text='Grafik Tipi:', font=('Arial', 12))
graph_label.pack()

graph_combo = ttk.Combobox(settings_frame, values=['Scatter', 'Bar', 'Stem'], font=('Arial', 12))
graph_combo.current(0)
graph_combo.pack()

# Create, Start, Stop, Continue, Reset Buttons
create_button = ttk.Button(settings_frame, text='Oluştur', command=create_graph)
create_button.pack()

start_button = ttk.Button(settings_frame, text='Başlat', command=start_animation)
start_button.pack()

stop_button = ttk.Button(settings_frame, text='Durdur', command=stop_animation)
stop_button.pack()

continue_button = ttk.Button(settings_frame, text='Devam Et', command=continue_animation)
continue_button.pack()

reset_button = ttk.Button(settings_frame, text='Sıfırla', command=reset)
reset_button.pack()

window.mainloop()
