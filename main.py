import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

is_animation_running = False

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not is_animation_running:
                return
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            update_display(arr)
            time.sleep(speed_slider.get())
            window.update()

    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if not is_animation_running:
                return
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        update_display(arr)
        time.sleep(speed_slider.get())
        window.update()

    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            if not is_animation_running:
                return
            arr[j + 1] = arr[j]
            j -= 1
            update_display(arr)
            time.sleep(speed_slider.get())
            window.update()

        arr[j + 1] = key

    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if not is_animation_running:
                return
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            if not is_animation_running:
                return
            arr[k] = left_half[i]
            i += 1
            k += 1
            update_display(arr)
            time.sleep(speed_slider.get())
            window.update()

        while j < len(right_half):
            if not is_animation_running:
                return
            arr[k] = right_half[j]
            j += 1
            k += 1
            update_display(arr)
            time.sleep(speed_slider.get())
            window.update()

        update_display(arr)
        time.sleep(speed_slider.get())
        window.update()

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        update_display(arr)
        time.sleep(speed_slider.get())
        window.update()

    elif low == 0 and high == len(arr) - 1:
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
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def update_display(arr):
    canvas.delete(tk.ALL)
    bar_width = canvas_width // len(arr)
    bar_height_ratio = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='sky blue', outline='white')
    canvas.update_idletasks()

def create_array():
    size = int(size_spinbox.get())
    if size < 3:
        messagebox.showinfo("Bilgi", "En az 3 elemanlı bir liste oluşturun.")
        return None

    list_values = list_text.get("1.0", tk.END).strip().split()
    if len(list_values) != size:
        messagebox.showinfo("Bilgi", "Lütfen listede belirtilen boyuta uygun sayıda eleman girin.")
        return None

    try:
        array = [int(value) for value in list_values]
        return array
    except ValueError:
        messagebox.showinfo("Bilgi", "Geçersiz elemanlar girdiniz. Lütfen sadece tam sayıları kullanın.")
        return None

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
    selected_algorithm = algorithm_combo.get()
    array = create_array()
    if array is None:
        return

    global is_animation_running
    is_animation_running = True

    if selected_algorithm == 'Bubble Sort':
        bubble_sort(array)
    elif selected_algorithm == 'Selection Sort':
        selection_sort(array)
    elif selected_algorithm == 'Insertion Sort':
        insertion_sort(array)
    elif selected_algorithm == 'Merge Sort':
        merge_sort(array)
    elif selected_algorithm == 'Quick Sort':
        quick_sort(array, 0, len(array) - 1)

    is_animation_running = False

def stop_animation():
    global is_animation_running
    is_animation_running = False

window = tk.Tk()
window.title("Sıralama Animasyonu")
window.geometry("800x600")
window.resizable(False, False)

# Sol panel
left_panel = tk.Frame(window, width=200, bg='white')
left_panel.pack(side=tk.LEFT, fill=tk.Y)

# Boyut seçimi
size_label = tk.Label(left_panel, text="Dizi Boyutu:")
size_label.pack(pady=10)
size_spinbox = tk.Spinbox(left_panel, from_=3, to=10, width=10)
size_spinbox.pack()

# Liste girişi
list_label = tk.Label(left_panel, text="Dizi Elemanları:")
list_label.pack(pady=10)
list_text = tk.Text(left_panel, height=5, width=20)
list_text.pack()

# Grafik tipi seçimi
graph_label = tk.Label(left_panel, text="Grafik Tipi:")
graph_label.pack(pady=10)
graph_combo = ttk.Combobox(left_panel, values=["Scatter", "Bar", "Stem"])
graph_combo.pack()

# Grafik oluşturma butonu
graph_button = tk.Button(left_panel, text="Grafik Oluştur", command=create_graph)
graph_button.pack(pady=10)

# Hız ayarı
speed_label = tk.Label(left_panel, text="Animasyon Hızı:")
speed_label.pack(pady=10)
speed_slider = tk.Scale(left_panel, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, length=150)
speed_slider.set(0.5)
speed_slider.pack()

# Sıralama algoritması seçimi
algorithm_label = tk.Label(left_panel, text="Sıralama Algoritması:")
algorithm_label.pack(pady=10)
algorithm_combo = ttk.Combobox(left_panel, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"])
algorithm_combo.pack()

# Animasyon butonları
button_frame = tk.Frame(left_panel, bg='white')
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Başlat", width=10, command=start_animation)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Durdur", width=10, command=stop_animation)
stop_button.pack(side=tk.LEFT, padx=5)

# Sağ panel
right_panel = tk.Frame(window, bg='white')
right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Çizim alanı
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(right_panel, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(pady=20)

window.mainloop()
