import tkinter as tk
from tkinter import ttk, messagebox
import random

# Create Main Window
root = tk.Tk()
root.title("Belagavi Mitra - Travel & Learn Buddy")
root.geometry("480x560")
root.configure(bg="#f0f2f5")

# App Header
title_label = tk.Label(root, text="🚩 Belagavi Mitra", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#1f2937")
title_label.pack(pady=5)
subtitle = tk.Label(root, text="Your 4-Language Local Friend & Language Tutor in Belagavi", font=("Arial", 9), bg="#f0f2f5", fg="#4b5563")
subtitle.pack(pady=2)

# Notebook (Tabs)
notebook = ttk.Notebook(root)
notebook.pack(pady=5, fill="both", expand=True)

# ==========================================
# TAB 1: LOCAL TRANSLATOR
# ==========================================
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="🗣️ Translator")

tk.Label(tab1, text="Select Tourist Phrase:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
phrase_var = tk.StringVar(value="How much for Gokak Falls?")
phrases = [
    "How much for Gokak Falls?",
    "Where is the bus stand?",
    "Give me 1 kg Kunda",
    "Please turn on the auto meter"
]
phrase_box = ttk.Combobox(tab1, textvariable=phrase_var, values=phrases, width=38, state="readonly")
phrase_box.pack(padx=20, pady=5)

tk.Label(tab1, text="Translate to:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
lang_var = tk.StringVar(value="Kannada")
tk.Radiobutton(tab1, text="Kannada", variable=lang_var, value="Kannada").pack(anchor="w", padx=30)
tk.Radiobutton(tab1, text="Marathi", variable=lang_var, value="Marathi").pack(anchor="w", padx=30)

result_label = tk.Label(tab1, text="", font=("Arial", 11, "bold"), fg="#1d4ed8", wraplength=400, justify="left")
result_label.pack(padx=20, pady=10)

translations = {
    ("How much for Gokak Falls?", "Kannada"): "Gokak Falls ge eshtu charge?",
    ("How much for Gokak Falls?", "Marathi"): "Gokak Falls sathi kiti hoil?",
    ("Where is the bus stand?", "Kannada"): "Bus stand yelli ide?",
    ("Where is the bus stand?", "Marathi"): "Bus stand kuthe ahe?",
    ("Give me 1 kg Kunda", "Kannada"): "Ondu kg Kunda kodi",
    ("Give me 1 kg Kunda", "Marathi"): "Ek kg Kunda dya",
    ("Please turn on the auto meter", "Kannada"): "Meter haaki bari",
    ("Please turn on the auto meter", "Marathi"): "Meter chalu kara"
}

def translate_phrase():
    p = phrase_var.get()
    l = lang_var.get()
    res = translations.get((p, l), "Translation not available")
    result_label.config(text=f"{l}: {res}")

tk.Button(tab1, text="Translate Phrase", command=translate_phrase, bg="#2563eb", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ==========================================
# TAB 2: AUTO FARE CALCULATOR
# ==========================================
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="🛺 Auto Fare")

tk.Label(tab2, text="Select Destination:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
dest_var = tk.StringVar(value="Gokak Falls")
dests = {
    "Gokak Falls": 62,
    "Belagavi Fort & Kamal Basti": 3,
    "Rajhansgad Yellur Fort": 15,
    "Kapileshwar Temple": 2,
    "Shahapur Kunda Market": 4
}
dest_box = ttk.Combobox(tab2, textvariable=dest_var, values=list(dests.keys()), width=38, state="readonly")
dest_box.pack(padx=20, pady=5)

fare_result = tk.Label(tab2, text="", font=("Arial", 10, "bold"), fg="#15803d", justify="left")
fare_result.pack(padx=20, pady=10)

def calculate_fare():
    d = dest_var.get()
    dist = dests[d]
    fare = 30 + max(0, dist - 2) * 15
    fare_result.config(text=f"Distance: {dist} km\nEstimated Fair Fare: ₹{fare}\n\n💡 Show this screen to negotiate fairly!")

tk.Button(tab2, text="Calculate Fare", command=calculate_fare, bg="#16a34a", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ==========================================
# NEW FEATURE TAB 3: BELAGAVI FOOD GUIDE
# ==========================================
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="🍲 Local Food")

tk.Label(tab3, text="Select Belagavi Special Food:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
food_var = tk.StringVar(value="Kunda (Sweet)")
food_items = {
    "Kunda (Sweet)": "Kannada: Kunda nanna priyavadaddu (ಕುಂದ ಬೇಕು)\nMarathi: Kunda masta ahe (कुंदा मस्त आहे)",
    "Maha Raja Veg Thali": "Kannada: Veg Oota ideya? (ವೆಜ್ ಊಟ ಇದೆಯಾ?)\nMarathi: Veg Jevan ahe ka? (व्हेज जेवण आहे का?)",
    "Shenga Chutney Pudi": "Kannada: Chutney pudi kodi (ಚಟ್ನಿ ಪುಡಿ ಕೊಡಿ)\nMarathi: Chutney powder dya (चटणी पावडर द्या)"
}
food_box = ttk.Combobox(tab3, textvariable=food_var, values=list(food_items.keys()), width=38, state="readonly")
food_box.pack(padx=20, pady=5)

food_info = tk.Label(tab3, text="", font=("Arial", 10), fg="#b45309", justify="left")
food_info.pack(padx=20, pady=10)

def show_food_details():
    f = food_var.get()
    food_info.config(text=food_items[f])

tk.Button(tab3, text="How to Order in Local Script", command=show_food_details, bg="#d97706", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ==========================================
# TAB 4: SOS EMERGENCY HELP
# ==========================================
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="🚨 SOS Help")

tk.Label(tab4, text="Emergency Flashcards (Show to locals):", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=10)

def show_sos(e_type):
    if e_type == "medical":
        msg = "MEDICAL EMERGENCY:\nKannada: ನನಗೆ ಚಿಕಿತ್ಸೆ ಬೇಕು\nMarathi: मला हॉस्पिटल पाहिजे"
    elif e_type == "police":
        msg = "POLICE ASSISTANCE:\nKannada: ಪೋಲೀಸ್‌ಗೆ ಕರೆ ಮಾಡಿ (Call 112)\nMarathi: पोलिसांना बोलवा"
    else:
        msg = "LOST LOCATION:\nKannada: ನಾನು ದಾರಿ ತಪ್ಪಿದ್ದೇನೆ\nMarathi: मी रस्ता चुकलोय"
    messagebox.showwarning("Emergency Card", msg)

tk.Button(tab4, text="🏥 Medical Help / Hospital", command=lambda: show_sos("medical"), width=32, bg="#dc2626", fg="white").pack(pady=8)
tk.Button(tab4, text="👮 Police Assistance", command=lambda: show_sos("police"), width=32, bg="#dc2626", fg="white").pack(pady=8)
tk.Button(tab4, text="🗺️ Lost Location", command=lambda: show_sos("lost"), width=32, bg="#dc2626", fg="white").pack(pady=8)

# ==========================================
# UPGRADE: SMART EXIT LEARNING POPUP
# ==========================================
learn_words = [
    {"word": "Hello / Respectful Greeting", "kn": "Namaskara (ನಮಸ್ಕಾರ)", "mr": "Namaskar (नमस्कार)"},
    {"word": "Thank You", "kn": "Dhanyavada (ಧನ್ಯವಾದ)", "mr": "Dhanyavaad (धन्यवाद)"},
    {"word": "How much?", "kn": "Eshtu? (ಎಷ್ಟು?)", "mr": "Kiti? (किती?)"},
    {"word": "Yes", "kn": "Houdhu (ಹೌದು)", "mr": "Hoy (होय)"},
    {"word": "Water", "kn": "Neeru (ನೀರು)", "mr": "Paani (पाणी)"}
]

def on_closing():
    # Pick a random word when user exits
    item = random.choice(learn_words)
    exit_msg = (
        f"🌟 Learn Before You Leave!\n\n"
        f"English: {item['word']}\n"
        f"👉 Kannada: {item['kn']}\n"
        f"👉 Marathi: {item['mr']}\n\n"
        f"Thanks for using Belagavi Mitra!"
    )
    messagebox.showinfo("Belagavi Daily Micro-Lesson 🎓", exit_msg)
    root.destroy()

# Attach exit popup to window close button
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run Application
root.mainloop()

