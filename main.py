import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

is_animation_running = False
comparison_label = None  # Karşılaştırma sayısı etiketi
def bubble_sort(arr):
    global comparison_label  # Global olarak tanımlanan etiket değişkeni
    global compx_label
    n = len(arr)
    comparison_count = 0

    compx_label.config(text="Karmaşıklık Analizi: O(n^2)")

    if comparison_label is None:
        bottom_panel = tk.Frame(left_panel, bg='gray')
        bottom_panel.pack(pady=10)
        comparison_label = tk.Label(bottom_panel, text="Karşılaştırma Sayısı: 0")
        comparison_label.pack(side=tk.LEFT, padx=5)

    else:
        comparison_label.config(text="Karşılaştırma Sayısı: 0")  # Etiketin metnini sıfırla


    def update_comparison_label(count):
        comparison_label.config(text=f"Karşılaştırma Sayısı: {count}")
        comparison_label.update()

    update_comparison_label(0)  # İlk fonksiyon başlangıcında etiketi güncelle

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not is_animation_running:
                return
            comparison_count += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            update_display2(arr, ["gray" if x == j or x == j + 1 else "red" for x in range(len(arr))])
            time.sleep(speed_slider.get())
            window.update()

            # Adım adım karşılaştırma sayısını güncelle ve ekrana yazdır
            update_comparison_label(comparison_count)

    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

    print("Karşılaştırma Sayısı (bubble_sort):", comparison_count)

def selection_sort(arr):
    global comparison_label  # Global olarak tanımlanan etiket değişkeni
    global compx_label

    compx_label.config(text="Karmaşıklık Analizi: O(n^2)")

    if comparison_label is None:
        bottom_panel = tk.Frame(left_panel, bg='gray')
        bottom_panel.pack(pady=10)
        comparison_label = tk.Label(bottom_panel, text="Karşılaştırma Sayısı: 0")
        comparison_label.pack(side=tk.LEFT, padx=5)

    else:
        comparison_label.config(text="Karşılaştırma Sayısı: 0")  # Etiketin metnini sıfırla


    n = len(arr)
    comparison_count = 0

    def update_comparison_label(count):
        comparison_label.config(text=f"Karşılaştırma Sayısı: {count}")
        comparison_label.update()

    update_comparison_label(0)  # İlk fonksiyon başlangıcında etiketi güncelle

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if not is_animation_running:
                return
            comparison_count += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        update_display2(arr, ["gray" if x == i or x == min_idx else "red" for x in range(len(arr))])
        time.sleep(speed_slider.get())
        window.update()

        # Adım adım karşılaştırma sayısını güncelle ve ekrana yazdır
        update_comparison_label(comparison_count)


    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

    print("Karşılaştırma Sayısı (selection_sort):", comparison_count)

def insertion_sort(arr):
    global comparison_label  # Global olarak tanımlanan etiket değişkeni
    global compx_label

    compx_label.config(text="Karmaşıklık Analizi: O(n^2)")

    if comparison_label is None:
        bottom_panel = tk.Frame(left_panel, bg='gray')
        bottom_panel.pack(pady=10)
        comparison_label = tk.Label(bottom_panel, text="Karşılaştırma Sayısı: 0")
        comparison_label.pack(side=tk.LEFT, padx=5)

    else:
        comparison_label.config(text="Karşılaştırma Sayısı: 0")  # Etiketin metnini sıfırla



    def update_comparison_label(count):
        comparison_label.config(text=f"Karşılaştırma Sayısı: {count}")
        comparison_label.update()

    update_comparison_label(0)  # İlk fonksiyon başlangıcında etiketi güncelle

    n = len(arr)
    comparison_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            if not is_animation_running:
                return
            comparison_count += 1

            arr[j + 1] = arr[j]
            j -= 1
            update_display2(arr, ["gray" if x == j or x == j+1 else "red" for x in range(len(arr))])
            time.sleep(speed_slider.get())
            window.update()
            # Adım adım karşılaştırma sayısını güncelle ve ekrana yazdır
            update_comparison_label(comparison_count)
        arr[j + 1] = key

    update_display(arr)
    time.sleep(speed_slider.get())
    window.update()

    print("Karşılaştırma Sayısı (insertion_sort):", comparison_count)

def merge_sort(arr):
    comparison_count = [0]

    global comparison_label
    global compxlabel

    compx_label.config(text="Karmaşıklık Analizi: O(n log(n))")


    if comparison_label is None:
        bottom_panel = tk.Frame(left_panel, bg='gray')
        bottom_panel.pack(pady=10)
        comparison_label = tk.Label(bottom_panel, text="Karşılaştırma Sayısı: 0")
        comparison_label.pack(side=tk.LEFT, padx=5)

    else:
        comparison_label.config(text="Karşılaştırma Sayısı: 0")


    def update_comparison_label(count):
        comparison_label.config(text=f"Karşılaştırma Sayısı: {count}")
        comparison_label.update()

    update_comparison_label(0)

    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort_helper(left_half)
            merge_sort_helper(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if not is_animation_running:
                    return
                comparison_count[0] += 1
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
                comparison_count[0] += 1
            while j < len(right_half):
                if not is_animation_running:
                    return
                arr[k] = right_half[j]
                j += 1
                k += 1
                comparison_count[0] += 1

            update_display2(arr, ["gray" if x == j else "red" for x in range(len(arr))])
            time.sleep(speed_slider.get())
            window.update()

            # Adım adım karşılaştırma sayısını günceller ve ekrana yazdırır
            update_comparison_label(comparison_count)

    merge_sort_helper(arr)

    print("Toplam Karşılaştırma Sayısı: (merge_sort)", comparison_count[0])

    update_display(arr)

def quick_sort(arr, low, high):
    comparison_count = 0

    global comparison_label
    global compxlabel

    compx_label.config(text="Karmaşıklık Analizi: O(n^2)")

    if comparison_label is None:
        bottom_panel = tk.Frame(left_panel, bg='gray')
        bottom_panel.pack(pady=10)
        comparison_label = tk.Label(bottom_panel, text="Karşılaştırma Sayısı: 0")
        comparison_label.pack(side=tk.LEFT, padx=5)
    else:
        comparison_label.config(text="Karşılaştırma Sayısı: 0")



    def update_comparison_label(count):
        comparison_label.config(text=f"Karşılaştırma Sayısı: {count}")
        comparison_label.update()

    update_comparison_label(0)

    def _quick_sort(arr, low, high):
        nonlocal comparison_count

        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
            update_display2(arr, ["gray" if x == low else "red" for x in range(len(arr))])
            time.sleep(speed_slider.get())
            window.update()
            comparison_count += (high - low)  # Her bir bölme işlemi için (high - low) kadar karşılaştırma yapılır

            # Adım adım karşılaştırma sayısını güncelle ve ekrana yazdır
            update_comparison_label(comparison_count)

        elif low == 0 and high == len(arr) - 1:
            update_display2(arr, ["gray" if x == low else "red" for x in range(len(arr))])
            time.sleep(speed_slider.get())
            window.update()

    _quick_sort(arr, low, high)
    print("Karşılaştırma Sayısı (quick_sort)", comparison_count)

    update_display(arr)

def partition(arr, low, high):  # quick sort için parçalama işlemi kullanılan adımları gerçekleştirir.
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update_display2(arr, ["gray" if x == low else "red" for x in range(len(arr))])  # diziye yapılan değişiklikleri görsel olarak güncellemek için.
            time.sleep(speed_slider.get())  # güncellemelerin belirli bir hızda gerçekleştirilmesi için.
            window.update()   # GUI penceresinin güncellenmesini sağlar
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def update_display_qs(arr, low, high):
    colorArray=[]
    for i in range(arr):

        if i >= low and i <= high:
            colorArray.append("red")
        else:
            colorArray.append("gray")

        if i == high:
            colorArray[i] == 'orange'
    return colorArray

def update_display(arr):
    bar_width = canvas_width // len(arr)
    bar_height_ratio = canvas_height / max(arr)
    canvas.delete(tk.ALL)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='light green', outline='white')
        canvas.create_text(x0 + bar_width // 2, y0 - 10, text=str(value), fill='black')  # Yeni satır
    canvas.update_idletasks()

def update_display2(arr, colorArray):
    bar_width = canvas_width // len(arr)
    bar_height_ratio = canvas_height / max(arr)
    canvas.delete(tk.ALL)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i], outline = 'white')
        canvas.create_text(x0 + bar_width // 2, y0 - 10, text = str(value), fill = 'black')  # Yeni satır
    canvas.update_idletasks()

def create_array():
    size = int(size_spinbox.get())
    list_values = list_text.get("1.0", tk.END).strip().split()

    if not any(list_values):
        array = random.sample(range(1, 100), size)
    else:
        if len(list_values) != size:
            messagebox.showinfo("Bilgi", "Lütfen listede belirtilen boyuta uygun sayıda eleman girin.")
            return None

        try:
            array = [int(value) for value in list_values]
        except ValueError:
            messagebox.showinfo("Bilgi", "Geçersiz elemanlar girdiniz. Lütfen sadece tam sayıları kullanın.")
            return None

    return array


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
    y_ratio = canvas_height / max(arr)
    fixed_radius = 12  # Sabit yarıçap değeri
    for i, value in enumerate(arr):
        x = i * x_interval + x_interval / 2
        y = canvas_height - value * y_ratio / 2
        canvas.create_oval(x - fixed_radius, y - fixed_radius, x + fixed_radius, y + fixed_radius, fill='sky blue')
        canvas.create_text(x, y, text=str(value), fill='black')
    window.update_idletasks()



def bar_graph(arr):
    canvas.delete("all")
    max_value = max(arr)
    canvas_height_new = canvas_height + 100  # Y ekseni boyutunu sabit bir değer olarak ayarla
    bar_width = canvas_width // len(arr)
    bar_height_ratio = (canvas_height_new - 20) / max_value  # Y ekseni boyutunu 20 piksel kadar azalt
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height_new - value * bar_height_ratio
        x1 = (i + 1) * bar_width
        y1 = canvas_height_new
        canvas.create_rectangle(x0, y0, x1, y1, fill='sky blue', outline='white')
        canvas.create_text(x0 + bar_width/2, y0 - 10, text=str(value), anchor=tk.N)
    canvas.config(height=canvas_height_new)  # Canvas yüksekliğini güncelle
    window.update_idletasks()


def stem_graph(arr):
    canvas.delete("all")
    x_interval = canvas_width / len(arr)
    y_ratio = canvas_height / max(arr)
    for i, value in enumerate(arr):
        x = i * x_interval + x_interval / 2
        y = canvas_height - value * y_ratio / 2
        canvas.create_line(x, canvas_height, x, y, fill='sky blue', width=2)
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='sky blue', outline='sky blue')
        canvas.create_text(x, y - 10, text=str(value), fill='black')
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

def reset():
    canvas.delete(tk.ALL)
    list_text.delete("1.0", tk.END)
    size_spinbox.delete(0, tk.END)
    size_spinbox.insert(0, "1")
    is_animation_running = False

window = tk.Tk()
window.title("Sıralama Animasyonu")
window.geometry("800x600")
window.resizable(False, False)

# Sol panel
left_panel = tk.Frame(window, width=200, bg='gray')
left_panel.pack(side=tk.LEFT, fill=tk.Y)

# Boyut seçimi
size_label = tk.Label(left_panel, text="Dizi Boyutu:")
size_label.pack(pady=10)
size_spinbox = tk.Spinbox(left_panel, from_=1, to=30)
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
graph_combo.set("Bar")  # Başlangıçta "Bar" seçili olarak gelmesi için
graph_combo.pack()

# Grafik oluşturma butonu
graph_button = tk.Button(left_panel, text="Grafik Oluştur", command=create_graph)
graph_button.pack(pady=10)

# Hız ayarı
speed_label = tk.Label(left_panel, text="Animasyon Hızı:")
speed_label.pack(pady=10)
speed_slider = tk.Scale(left_panel, from_=1.0, to=0.1, resolution=0.1, orient=tk.HORIZONTAL, length=150,showvalue=False)
speed_slider.set(0.5)
speed_slider.pack()

# Sıralama algoritması seçimi
algorithm_label = tk.Label(left_panel, text="Sıralama Algoritması:")
algorithm_label.pack(pady=10)
algorithm_combo = ttk.Combobox(left_panel, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"])
algorithm_combo.set("Bubble Sort")  # Başlangıçta "Bubble Sort" seçili olarak gelmesi için
algorithm_combo.pack()

# Animasyon butonları
button_frame = tk.Frame(left_panel, bg='gray')
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Başlat", width=10, command=start_animation)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Durdur", width=10, command=stop_animation)
stop_button.pack(side=tk.LEFT, padx=5)

# Yeni panel
bottom_panel = tk.Frame(left_panel, bg='gray')
bottom_panel.pack(pady=10)


reset_button = ttk.Button(bottom_panel, text='Sıfırla', command=reset)
reset_button.pack(side=tk.LEFT, padx=5)

# Karmaşıklık Analizi
bottom_panel2 = tk.Frame(left_panel, bg='gray')
bottom_panel2.pack(pady=10)
compx_label = tk.Label(bottom_panel2, text="Karmaşıklık Analizi: ")
compx_label.pack(side=tk.LEFT, padx=5)

# Sağ panel
right_panel = tk.Frame(window, bg='white')
right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Çizim alanı
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(right_panel, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(pady=20)

window.mainloop()
