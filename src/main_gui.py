import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, ttk
import pandas as pd

def read_csv(file_path):
    """Reads a CSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "File is empty.")
    except pd.errors.ParserError:
        messagebox.showerror("Error", "File could not be parsed.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    return None

def open_file():
    """Open file dialog and read the selected CSV file."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = read_csv(file_path)
        if df is not None:
            # Display only the first 5 rows
            df = df.head(5)
            # Clear existing data in the Treeview
            for i in tree.get_children():
                tree.delete(i)
            
            # Set up columns
            columns = list(df.columns)
            tree["columns"] = columns
            tree["show"] = "headings"
            
            # Create column headings
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="w")
            
            # Insert rows into Treeview
            for _, row in df.iterrows():
                tree.insert("", "end", values=list(row))

# Create the main window
root = tk.Tk()
root.title("Utah Jazz Salary Cap")

# Set the desired window size
window_width = 800
window_height = 400

# Get the dimensions of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window geometry
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

icon = PhotoImage(file='./data/jazz_logo.png')
root.iconphoto(False, icon)

# Create and place widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create Treeview widget
tree = ttk.Treeview(frame, columns=(), show="headings", height= 5)
tree.pack(side="left", fill="both", expand=True)

# Create vertical scrollbar
vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")

# Create horizontal scrollbar
hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
hsb.pack(side="bottom", fill="x")

# Configure the Treeview to use the scrollbars
tree.configure(yscrollcommand=vsb)
tree.configure(xscrollcommand=hsb)

# Add a sample button
button = tk.Button(root, text="Open CSV File", command=open_file)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
