import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import requests
from bs4 import BeautifulSoup
import threading

def scrape_website(url, result_text, status_label):
    """
    Performs the web scraping in a separate thread to keep the UI responsive.
    Updates the UI with the scraped data or an error message.
    """
    try:
        status_label.config(text="Status: Scraping...")
        
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        
        results = []

        results.append("--- LINKS ---\n")
        for link in soup.find_all("a", href=True):
            results.append(link["href"] + "\n")

        results.append("\n--- HEADINGS ---\n")
        for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            results.append(heading.get_text(strip=True) + "\n")

        results.append("\n--- PARAGRAPHS ---\n")
        for p in soup.find_all("p"):
            results.append(p.get_text(strip=True) + "\n")
            
        result_text.after(0, lambda: update_text_widget(result_text, "".join(results)))
        status_label.after(0, lambda: status_label.config(text="Status: Done!"))

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve page:\n{e}")
        status_label.after(0, lambda: status_label.config(text="Status: Error!"))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
        status_label.after(0, lambda: status_label.config(text="Status: Error!"))

def update_text_widget(widget, text):
    """Helper function to update the text widget from any thread."""
    widget.config(state=tk.NORMAL)
    widget.delete(1.0, tk.END)
    widget.insert(tk.END, text)
    widget.config(state=tk.DISABLED)

def start_scraping(url_entry, result_text, status_label):
    """
    Starts the scraping process when the button is clicked.
    """
    url = url_entry.get()
    if not url.startswith(('http://', 'https://')):
        messagebox.showwarning("Invalid URL", "Please enter a valid URL starting with http:// or https://")
        return
        
    update_text_widget(result_text, "Scraping in progress...")
    
    thread = threading.Thread(target=scrape_website, args=(url, result_text, status_label))
    thread.daemon = True
    thread.start()

def export_results(result_text):
    """
    Saves the content of the results text widget to a .txt file.
    """
    content = result_text.get("1.0", tk.END)
    if not content.strip():
        messagebox.showwarning("No Content", "There is no content to export.")
        return

    try:
        # Open a "save as" dialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        # If the user cancels the dialog, file_path will be empty
        if not file_path:
            return

        # Write the content to the selected file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        
        messagebox.showinfo("Success", f"Results successfully exported to\n{file_path}")

    except Exception as e:
        messagebox.showerror("Export Error", f"An error occurred while exporting the file:\n{e}")


def create_gui():
    """
    Creates and sets up the main application window and its widgets.
    """
    app = tk.Tk()
    app.title("HeXyScraper")
    app.geometry("800x600")
    app.configure(bg="#f0f0f0")

    main_frame = tk.Frame(app, padx=10, pady=10, bg="#f0f0f0")
    main_frame.pack(fill=tk.BOTH, expand=True)

    url_frame = tk.Frame(main_frame, bg="#f0f0f0")
    url_frame.pack(fill=tk.X, pady=5)

    url_label = tk.Label(url_frame, text="Enter URL:", font=("Helvetica", 12), bg="#f0f0f0")
    url_label.pack(side=tk.LEFT, padx=(0, 10))

    url_entry = tk.Entry(url_frame, font=("Helvetica", 12), relief=tk.SOLID, borderwidth=1)
    url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    url_entry.insert(0, "https://example.com")

    # --- Frame for buttons ---
    button_frame = tk.Frame(main_frame, bg="#f0f0f0")
    button_frame.pack(fill=tk.X, pady=(10, 5))
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    # --- Scrape Button ---
    scrape_button = tk.Button(
        button_frame,
        text="Scrape Website",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief=tk.FLAT,
        command=lambda: start_scraping(url_entry, result_text, status_label)
    )
    scrape_button.grid(row=0, column=0, sticky="ew", padx=(0, 5))

    # --- Export Button ---
    export_button = tk.Button(
        button_frame,
        text="Export to TXT",
        font=("Helvetica", 12, "bold"),
        bg="#008CBA",
        fg="white",
        relief=tk.FLAT,
        command=lambda: export_results(result_text)
    )
    export_button.grid(row=0, column=1, sticky="ew", padx=(5, 0))

    # --- Results Display ---
    result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, font=("Courier New", 10), state=tk.DISABLED)
    result_text.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # --- Status Bar ---
    status_label = tk.Label(main_frame, text="Status: Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#f0f0f0")
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    return app

if __name__ == "__main__":
    gui_app = create_gui()
    gui_app.mainloop()
