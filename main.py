import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from deep_translator import GoogleTranslator
import subprocess
import os
import textwrap
from tkinter import ttk

def select_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        pdf_path.set(filepath)
        extract_text(filepath)

def extract_text(path):
    try:
        temp_txt = "/tmp/temp_gui_pdf_text.txt"
        subprocess.run(["pdftotext", path, temp_txt], check=True)
        with open(temp_txt, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.strip():
            messagebox.showerror("Hata", "PDF içeriği alınamadı (metin bulunamıyor).")
            return
        original_text.delete(1.0, tk.END)
        original_text.insert(tk.END, text)
    except Exception as e:
        messagebox.showerror("Hata", str(e))

def translate_text():
    content = original_text.get(1.0, tk.END).strip()
    if not content:
        messagebox.showwarning("Uyarı", "Çevrilecek metin yok.")
        return
    
    # Sayfa sayısı bulma (her 4500 karakterde bir sayfa kabul ediyorum)
    page_texts = textwrap.wrap(content, width=4500, break_long_words=False, break_on_hyphens=False)
    total_pages = len(page_texts)
    
    # İlerleme barı başlat
    progress_bar["maximum"] = total_pages
    progress_bar["value"] = 0

    translated_text.delete(1.0, tk.END)

    for i, page in enumerate(page_texts):
        try:
            # Her sayfayı parçalara ayırarak çevir
            chunks = textwrap.wrap(page, width=1500, break_long_words=False, break_on_hyphens=False)
            translated_page = ""
            for j, chunk in enumerate(chunks):
                translated = GoogleTranslator(source='auto', target='tr').translate(chunk)
                translated_page += f"[Bölüm {j+1}]\n{translated}\n\n"
            
            # Sayfa metnini birleştir
            translated_text.insert(tk.END, f"[Sayfa {i+1}]\n{translated_page}\n\n")
            translated_text.update_idletasks()

            # İlerleme barını güncelle
            progress_bar["value"] = i + 1
            progress_bar.update_idletasks()
        except Exception as e:
            translated_text.insert(tk.END, f"[!] Hata (Sayfa {i+1}): {e}\n")
            translated_text.update_idletasks()

# Arayüz başlat
root = tk.Tk()
root.title("PDF Çevirici - İngilizce'den Türkçe'ye")
root.geometry("1000x600")

pdf_path = tk.StringVar()

tk.Button(root, text="📄 PDF Seç", command=select_pdf).pack(pady=5)
tk.Entry(root, textvariable=pdf_path, width=100).pack()

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

original_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50)
original_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

translated_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50)
translated_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# İlerleme barı
progress_bar = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
progress_bar.pack(pady=10)

tk.Button(root, text="🌍 ÇEVİR (İngilizce ➜ Türkçe)", command=translate_text, bg="lightblue").pack(pady=10)

root.mainloop()
