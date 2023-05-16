import random
import time
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sıralama işlemlerini başlatma
# Sıralama işlemlerini başlatma
def start_sorting():
    # Kullanıcının seçtiği değerleri al
    size = int(entry_size.get())
    manual = checkbox_manual_var.get()
    algorithm = algorithm_var.get()  # Retrieve the selected algorithm
    graph_type = graph_type_var.get()
    speed = float(entry_speed.get())

    # Sıralama işlemlerini başlat
    lst = create_list(size, manual)
    animate_sorting(lst, algorithm, graph_type, speed)


# Liste oluşturma
def create_list(size, manual=False):
    if manual:
        # Manual giriş yapılıyorsa, kullanıcıdan liste elemanlarını alınır
        input_window = tk.Toplevel()
        input_window.title("Liste Girişi")

        elements_label = tk.Label(input_window, text="Liste Elemanlarını Virgülle Ayırarak Girin:")
        elements_label.pack()
        elements_entry = tk.Entry(input_window)
        elements_entry.pack()

        confirm_button = tk.Button(input_window, text="Onayla", command=lambda: input_window.destroy())
        confirm_button.pack()

        input_window.wait_window(input_window)
        elements = elements_entry.get().split(",")
        lst = [int(element.strip()) for element in elements]
    else:
        # Rastgele liste oluşturulur
        lst = [random.randint(1, 100) for _ in range(size)]
    return lst


# Sıralama animasyonunu gerçekleştirme
def animate_sorting(lst, algorithm, graph_type, speed):
    # Grafik arayüzünü oluşturma
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=tk.Toplevel())
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    ax = fig.add_subplot(111)

    # Sıralama işlemini başlatma
    if algorithm == "Selection Sort":
        selection_sort(lst, ax, speed, canvas)
    elif algorithm == "Bubble Sort":
        bubble_sort(lst, ax, speed, canvas)
    elif algorithm == "Insertion Sort":
        insertion_sort(lst, ax, speed, canvas)
    elif algorithm == "Merge Sort":
        merge_sort(lst, ax, speed, canvas)
    elif algorithm == "Quick Sort":
        quick_sort(lst, ax, speed, canvas)

    # Sıralanmış liste ve karşılaştırma sayısı yazdırma
    print("Sıralanmış Liste: ", lst)
    print("Karşılaştırma Sayısı: ", len(lst) * (len(lst) - 1) // 2)

# Seçme Sıralaması (Selection Sort)
def selection_sort(lst, ax, speed, canvas):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        ax.clear()
        ax.bar(range(len(lst)), lst, color='b')
        canvas.draw_idle()
        time.sleep(speed)
# Kabarcık Sıralaması (Bubble Sort)
def bubble_sort(lst, ax, speed, canvas):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                ax.clear()
                ax.bar(range(len(lst)), lst, color='b')
                canvas.draw_idle()
                time.sleep(speed)

# Ekleme Sıralaması (Insertion Sort)
def insertion_sort(lst, ax, speed, canvas):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        ax.clear()
        ax.bar(range(len(lst)), lst, color='b')
        canvas.draw_idle()
        time.sleep(speed)

# Birleştirme Sıralaması (Merge Sort)
def merge_sort(lst, ax, speed, canvas):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half, ax, speed, canvas)
        merge_sort(right_half, ax, speed, canvas)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
        ax.clear()
        ax.bar(range(len(lst)), lst, color='b')
        canvas.draw_idle()
        time.sleep(speed)

# Hızlı Sıralama (Quick Sort)
def quick_sort(lst, ax, speed, canvas):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1, len(lst)):
            if lst[i] < pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
        ax.clear()
        ax.bar(range(len(left)), left, color='r')
        ax.bar(len(left), pivot, color='g')
        ax.bar(range(len(left) + 1, len(lst)), right, color='r')
        canvas.draw_idle()
        time.sleep(speed)
        return quick_sort(left, ax, speed, canvas) + [pivot] + quick_sort(right, ax, speed, canvas)

# Tkinter penceresini oluştur
window = tk.Tk()

# Kullanıcı seçimlerini yapabileceği bileşenler
label_size = tk.Label(window, text="Liste Boyutu:")
entry_size = tk.Entry(window)

checkbox_manual_var = tk.BooleanVar()  # Define the checkbox_manual_var variable
checkbox_manual = tk.Checkbutton(window, text="Manuel Giriş", variable=checkbox_manual_var)

algorithm_var = tk.StringVar()  # Create a StringVar for the algorithm selection
algorithm_var.set("Selection Sort")  # Varsayılan olarak Seçme Sıralaması seçili
label_algorithm = tk.Label(window, text="Sıralama Algoritması:")
dropdown_algorithm = tk.OptionMenu(window, algorithm_var, "Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort")

label_graph_type = tk.Label(window, text="Grafik Türü:")
graph_type_var = tk.StringVar()
graph_type_var.set("Bar") # Varsayılan olarak Bar grafiği seçili
dropdown_graph_type = tk.OptionMenu(window, graph_type_var, "Bar", "Line", "Scatter")

label_speed = tk.Label(window, text="Hız (saniye):")
entry_speed = tk.Entry(window)
entry_speed.insert(tk.END, "0.5") # Varsayılan olarak 0.5 saniye

start_button = tk.Button(window, text="Sıralamayı Başlat", command=start_sorting)

# Bileşenleri pencereye yerleştirme
label_size.pack()
entry_size.pack()

checkbox_manual.pack()

label_algorithm.pack()
dropdown_algorithm.pack()

label_graph_type.pack()
dropdown_graph_type.pack()

label_speed.pack()
entry_speed.pack()

start_button.pack()

# Pencereyi çalıştırma
window.mainloop()


