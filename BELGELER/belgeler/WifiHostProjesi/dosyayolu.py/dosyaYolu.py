
#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import os

# Seçilen dosyanın tam yolunu alma
try:
    selected_file_path = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS')
    if not selected_file_path:
        raise ValueError("Dosya yolu bulunamadı.")
except Exception as e:
    messagebox.showerror("Hata", f"Dosya yolu alınamadı: {e}")
    exit(1)

# Tkinter ile basit bir pencere oluşturma
def show_selected_file_path():
    root = tk.Tk()
    label = tk.Label(root, text=f"Seçilen Dosya: {selected_file_path}")
    label.pack()
    root.mainloop()

show_selected_file_path()
