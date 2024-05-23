import base64
import os
import tkinter as tk

def print_stylish(text):
    print(text)

def create_file():
    try:
        encoded_link = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20veERnUDl5cEM='
        decoded_link = base64.urlsafe_b64decode(encoded_link).decode('utf-8')
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f'Script directory: {script_dir}')
        
        canva_pro_dir = os.path.join(script_dir, 'CanvaPro')
        os.makedirs(canva_pro_dir, exist_ok=True)
        
        file_path = os.path.join(canva_pro_dir, 'canva_pro_link.txt')
        
        with open(file_path, 'w') as f:
            f.write(decoded_link)
        
        print('File created successfully.')
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f'Error creating the file: {e}')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text='Canva Pro Lifetime Free using Python', font=('Arial', 16))
        self.title_label.pack(pady=10)

        self.start_button = tk.Button(self, text='Create File', font=('Arial', 12), command=self.start_program)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self, text='Quit', font=('Arial', 12), command=self.master.destroy)
        self.quit_button.pack(pady=10)

    def start_program(self):
        self.start_button.config(state='disabled')
        create_file()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Canva Pro Lifetime Free using Python')
    app = Application(master=root)
    app.mainloop()

print_stylish('Powered by MrSh4dow')
