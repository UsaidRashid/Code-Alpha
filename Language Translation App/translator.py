import tkinter as tk
from googletrans import Translator

def translate_text():
    input_text = text_input.get()
    target_language = language_var.get()
    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language).text    
    translated_label.config(text=translated_text)

root = tk.Tk()
root.title("Language Translation App")
instruction_label = tk.Label(root, text="Enter the text you want to translate:")
instruction_label.pack()
text_input = tk.Entry(root, width=40)
text_input.pack()
language_label = tk.Label(root, text="Select target language:")
language_label.pack()
languages = ["English", "Spanish", "French","Hindi"]
language_var = tk.StringVar()
language_dropdown = tk.OptionMenu(root, language_var, *languages)
language_dropdown.pack()
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()
translated_label = tk.Label(root, text="")
translated_label.pack()
root.mainloop()