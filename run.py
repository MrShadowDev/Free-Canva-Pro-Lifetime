import asyncio
import base64
import os
import tkinter as tk

def create_file():
    try:
        # Decode the link
        encoded_link = 'aHR0cHM6Ly9saW5rLWh1Yi5uZXQvOTkwMjExL3dvcmtpbmctY2FudmEtcHJvLWludml0ZQ=='
        decoded_link = base64.urlsafe_b64decode(encoded_link).decode('utf-8')
        
        # Get the user's home directory
        user_home = os.path.expanduser("~")
        
        # Create the 'CanvaPro' directory in the user's home directory
        canva_pro_dir = os.path.join(user_home, 'CanvaPro')
        os.makedirs(canva_pro_dir, exist_ok=True)
        
        # Create the 'canva_pro_link.txt' file in the 'CanvaPro' directory
        file_path = os.path.join(canva_pro_dir, 'canva_pro_link.txt')
        
        # Write the decoded link to the file
        with open(file_path, 'w') as f:
            f.write(decoded_link)
        
        print('File created successfully.')
    except Exception as e:
        print(f'Error creating the file: {e}')

async def main():
    # Print program information
    program_title = 'Canva Pro Lifetime Free using Python'
    print_stylish('MrShadowDev presents')
    print_stylish(program_title)
    
    # Call the create_file function
    create_file()
    
    print(f'{program_title} completed successfully!')

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
        # Disable the 'Create File' button to prevent multiple file creation
        self.start_button.config(state='disabled')
        # Call the create_file function
        create_file()

if __name__ == '__main':
    # Create the GUI window
    root = tk.Tk()
    root.title('Canva Pro Lifetime Free using Python')
    app = Application(master=root)

    # Run the GUI loop
    app.mainloop()
