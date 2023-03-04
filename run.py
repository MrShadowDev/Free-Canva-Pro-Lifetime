import asyncio
import base64
import os
import shutil
import sys
import time
import webbrowser
import tkinter as tk


def print_stylish(text):
    line = '═' * (len(text) + 2)
    print(f'╔{line}╗')
    print(f'║ {text} ║')
    print(f'╚{line}╝')


async def create_file():
    # Wait for 15 seconds before creating the file
    await asyncio.sleep(15)
    # Decode the link and write it to the file
    encoded_link = 'aHR0cHM6Ly9iaXQubHkvT25oYXhwa19uZXRfQ2FudmFfRmViMjE='
    decoded_link = base64.urlsafe_b64decode(encoded_link).decode('utf-8')
    with open('canva_pro_link.txt', 'w') as f:
        f.write(decoded_link)
    print('File created')


async def open_browser(url):
    # Wait for 5 seconds before opening the browser
    await asyncio.sleep(5)
    webbrowser.open(url)


async def main():
    # Start the file creation task
    create_file_task = asyncio.create_task(create_file())

    # Open YouTube channel in the background
    youtube_channel_url = 'https://www.youtube.com/channel/UCvRdOYm32iVZ4lHLKpELPUg'
    open_browser_task = asyncio.create_task(open_browser(youtube_channel_url))

    # Print program information in a stylish way
    program_title = 'Canva Pro Lifetime Free using Python'
    print_stylish('MrShadowDev presents')
    print_stylish(program_title)

    # Wait for the tasks to finish
    await create_file_task
    await open_browser_task

    # Clear the screen and print final message
    os.system('cls' if os.name == 'nt' else 'clear')
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

        self.start_button = tk.Button(self, text='Start', font=('Arial', 12), command=self.start_program)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self, text='Quit', font=('Arial', 12), command=self.master.destroy)
        self.quit_button.pack(pady=10)

    def start_program(self):
        # Start the main coroutine in a new thread
        asyncio_thread = threading.Thread(target=asyncio.run, args=(main(),))
        asyncio_thread.start()
        # Disable the start button to prevent multiple program runs
        self.start_button.config(state='disabled')


if __name__ == '__main__':
    # Set the command prompt window size to 100x30
    os.system('mode con: cols=100 lines=30')

    # Change the text color to blue
    os.system('color 09')

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create the GUI window
    root = tk.Tk()
    root.title('Canva Pro Lifetime Free using Python')
    app = Application(master=root)

    # Run the GUI loop
    asyncio.run(main())
