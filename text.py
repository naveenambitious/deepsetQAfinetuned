"""
import requests

data = {
    'question': 'What is the main cause of fungal infection ?',
    'context': ''' Fungal infections are any disease or condition you get from a fungus. They usually affect your skin, hair, nails or mucous membranes but they can also infect your lungs or other parts of your body. You’re at higher risk for fungal infections if you have a weakened immune system. Antifungal medications are usually used to treat fungal infections.'''

}

response = requests.post("http://172.16.176.120:2020/query", json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

def send_request():
    question = question_entry.get("1.0", tk.END).strip()
    context = context_entry.get("1.0", tk.END).strip()

    if not question or not context:
        messagebox.showerror("Error", "Please enter both question and context.")
        return

    data = {
        'question': question,
        'context': context
    }

    try:
        response = requests.post("http://172.16.176.120:2020/query", json=data)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Status Code: {response.status_code}\n")
        result_text.insert(tk.END, f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}")

# Main window
root = tk.Tk()
root.title("LLM Flask App Tester")
root.geometry("700x600")

# Question input
tk.Label(root, text="Question:").pack(anchor="w", padx=10, pady=(10, 0))
question_entry = scrolledtext.ScrolledText(root, height=3, wrap=tk.WORD)
question_entry.pack(fill="x", padx=10)

# Context input
tk.Label(root, text="Context:").pack(anchor="w", padx=10, pady=(10, 0))
context_entry = scrolledtext.ScrolledText(root, height=8, wrap=tk.WORD)
context_entry.pack(fill="x", padx=10)

# Submit button
tk.Button(root, text="Send Request", command=send_request, bg="blue", fg="white").pack(pady=10)

# Response display
tk.Label(root, text="Response:").pack(anchor="w", padx=10)
result_text = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD)
result_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

root.mainloop()
