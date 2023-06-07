import tkinter as tk
from tkinter import ttk, filedialog
import os

def rename_files():
    # Read the selected file and retrieve the new names
    file_path = file_path_var.get()
    if file_path:
        with open(file_path, 'r') as file:
            new_names = file.read().splitlines()

        # Get the target directory
        target_directory = target_directory_var.get()

        # Get the final file ext
        file_ext = file_ext_entry.get()

        # Rename files in the target directory
        if os.path.isdir(target_directory):
            files = os.listdir(target_directory)
            if len(files) == len(new_names):
                for i, file_name in enumerate(files):
                    old_file_path = os.path.join(target_directory, file_name)
                    new_file_name = new_names[i] + file_ext
                    new_file_path = os.path.join(target_directory, new_file_name)
                    os.rename(old_file_path, new_file_path)
                result_label.config(text="Files renamed successfully!")
            else:
                result_label.config(text="Number of files and new names don't match!")
        else:
            result_label.config(text="Invalid target directory!")
    else:
        result_label.config(text="No file selected!")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    file_path_var.set(file_path)

def browse_directory():
    target_directory = filedialog.askdirectory()
    target_directory_var.set(target_directory)
    target_directory_label.config(text=target_directory)

# Create the Tkinter window
window = tk.Tk()
window.title("Rename Files in Bulk")

# Set window size and position
window.geometry("400x300")
window.resizable(False, False)

# Create a variable to store the file path
file_path_var = tk.StringVar()

# Create a label for the file path
file_path_label = tk.Label(window, textvariable=file_path_var)
file_path_label.pack()

# Create a button to browse for the file
browse_button = ttk.Button(window, text="Browse", command=browse_file, style="RoundedButton.TButton")
browse_button.pack()

# Create a variable to store the target directory
target_directory_var = tk.StringVar()

# Create a label for the target directory
target_directory_label = tk.Label(window, text="Target Directory:")
target_directory_label.pack()

# Create a button to browse for the target directory
browse_directory_button = ttk.Button(window, text="Select Directory", command=browse_directory, style="RoundedButton.TButton")
browse_directory_button.pack()

# Create an entry field for the file ext
file_ext_label = tk.Label(window, text="File extension:")
file_ext_label.pack()
file_ext_entry = ttk.Entry(window, style="RoundedEntry.TEntry")
file_ext_entry.pack()

# Create a button to start the renaming process
rename_button = ttk.Button(window, text="Rename Files", command=rename_files, style="RoundedButton.TButton")
rename_button.pack()

# Create a label for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Create custom styles
style = ttk.Style()
style.configure("RoundedButton.TButton", relief="flat", borderwidth=0, padding=6)
style.configure("RoundedEntry.TEntry", relief="flat", borderwidth=1, padding=6)

# Run the Tkinter event loop
window.mainloop()
