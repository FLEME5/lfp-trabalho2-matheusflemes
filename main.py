import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import re

root = tk.Tk()
root.title('LFP Regex Check')
root.geometry('400x100')

def check_string(event):
    input_dialog = simpledialog.askstring(title="LFP Regex Check",
        prompt="Digite o texto que deseja checar.")
    #print(f'{regex_list[regex_combobox.current()]}, {input_dialog}')
    check = re.search(regex_list[regex_combobox.current()], input_dialog)
    if check:
        msg = f'{input_dialog} coincide!'
    else:
        msg = f'{input_dialog} não coincide!'
    messagebox.showinfo(title='Resultado', message=msg)

regex_options = ('com número par de 1s e 0s', 'com pelo menos duas ocorrências do padrão 101', 
        'as cadeias 0110 e 1001', 'todas as cadeias que começam com 01 e terminamcom 10', 'a cadeia nula e 001')

regex_list = ['^([01]{2})*$', '^(?=([01]*101){2})[01]*$', '^0110$|^1001$', '^01[01]*10$', '^$|^001$']

label = ttk.Label(text="Selecione um regex:")
label.pack(fill='x', padx=5, pady=5)

selected_regex = tk.StringVar()
regex_combobox = ttk.Combobox(root, textvariable=selected_regex)
regex_combobox['values'] = regex_options
regex_combobox['state'] = 'readonly'
regex_combobox.pack(fill='x', padx=5, pady=5)

regex_combobox.bind('<<ComboboxSelected>>', check_string)

root.mainloop()