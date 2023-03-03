import asyncio
import base64
import os
import shutil
import sys
import time
import webbrowser


def print_stylish(text):
    line = '═' * (len(text) + 2)
    print(f'╔{line}╗')
    print(f'║ {text} ║')
    print(f'╚{line}╝')


async def create_file():
    # Wait for 15 seconds before creating the file
    await asyncio.sleep(15)
    # Decode the link and write it to the file
    encoded_link = 'aHR0cHM6Ly93d3cuY2FudmEuY29tL2JyYW5kL2pvaW4_dG9rZW49dnEwNF9mLWVYRTVtSFBWb1FTY2xzZz9yZWZyZXNoPXRlYW0taW52aXRl'
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


if __name__ == '__main__':
    # Set the command prompt window size to 100x30
    os.system('mode con: cols=100 lines=30')

    # Change the text color to blue
    os.system('color 09')

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Run the main coroutine
    asyncio.run(main())
