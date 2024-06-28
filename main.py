import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess
import platform
from CTkListbox import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Uruguay - Testing App")
        self.geometry("800x600")
        
        # Configure the customtkinter theme
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        # Create the sidebar
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")
        
        # Create a container for the main content
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(side="right", fill="both", expand=True)
        
        # Create buttons for the sidebar
        self.screenshots_button = ctk.CTkButton(self.sidebar, text="Screenshots", command=self.show_screenshots)
        self.screenshots_button.pack(pady=10, padx=10)
        
        self.reports_button = ctk.CTkButton(self.sidebar, text="Reports", command=self.show_reports)
        self.reports_button.pack(pady=10, padx=10)
        
        self.tests_button = ctk.CTkButton(self.sidebar, text="Tests", command=self.show_tests)
        self.tests_button.pack(pady=10, padx=10)
        
        # Create frames for screenshots, reports, and tests
        self.screenshots_frame = ctk.CTkFrame(self.main_container)
        self.reports_frame = ctk.CTkFrame(self.main_container)
        self.tests_frame = ctk.CTkFrame(self.main_container)
        
        # Initialize the application with screenshots view
        self.show_screenshots()
    
    def show_screenshots(self):
        self.clear_main_container()
        self.screenshots_frame.pack(fill="both", expand=True)
        
        # Display images from the screenshots folder
        screenshots_folder = "static/screenshots"
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)
        
        def refresh_screenshots():
            for widget in self.screenshots_frame.winfo_children():
                widget.destroy()
            
            for image_file in os.listdir(screenshots_folder):
                if image_file.endswith((".png", ".jpg", ".jpeg", ".gif")):
                    image_path = os.path.join(screenshots_folder, image_file)
                    image = Image.open(image_path)
                    image.thumbnail((300, 300))
                    photo = ImageTk.PhotoImage(image)
                    label = ctk.CTkLabel(self.screenshots_frame, image=photo)
                    label.image = photo  # Keep a reference to avoid garbage collection
                    label.pack(pady=5, padx=5)
            
            self.after(5000, refresh_screenshots)  # Refresh every 5 seconds
        
        refresh_screenshots()
    
    def show_reports(self):
        self.clear_main_container()
        self.reports_frame.pack(fill="both", expand=True)
        
        # Display list of files from the reports folder
        reports_folder = "reports"
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)
        
        def refresh_reports():
            for widget in self.reports_frame.winfo_children():
                widget.destroy()
            
            reports_list = CTkListbox(self.reports_frame)
            reports_list.pack(fill="both", expand=True, padx=10, pady=10)
            
            for report_file in os.listdir(reports_folder):
                reports_list.insert(tk.END, report_file)
            
            def open_file(event):
                selected_file = reports_list.get(reports_list.curselection())
                file_path = os.path.join(reports_folder, selected_file)
                if platform.system() == "Windows":
                    os.startfile(file_path)
                else:
                    subprocess.run(["xdg-open", file_path])
            
            reports_list.bind('<Double-1>', open_file)
            
            self.after(5000, refresh_reports)  # Refresh every 5 seconds
        
        refresh_reports()

    
    def show_tests(self):
        self.clear_main_container()
        self.tests_frame.pack(fill="both", expand=True)
        
        # Display list of files from the tests folder
        tests_folder = "tests"
        if not os.path.exists(tests_folder):
            os.makedirs(tests_folder)
        
        def refresh_tests():
            for widget in self.tests_frame.winfo_children():
                widget.destroy()
            
            tests_list = CTkListbox(self.tests_frame)
            tests_list.pack(fill="both", expand=True, padx=10, pady=10)
            
            for test_file in os.listdir(tests_folder):
                tests_list.insert(tk.END, test_file)
            
            run_tests_button = ctk.CTkButton(self.tests_frame, text="Run Tests", command=self.run_tests)
            run_tests_button.pack(pady=10)
             # Refresh every 5 seconds
        
        refresh_tests()
    
    def run_tests(self):
        if platform.system() == "Windows":
            subprocess.run(["start", "cmd", "/k", "pytest -m submit"], shell=True, cwd=os.getcwd())
        else:
            subprocess.run(["gnome-terminal", "--", "bash", "-c", "pytest; exec bash"], cwd=os.getcwd())
    
    def clear_main_container(self):
        for widget in self.main_container.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()
