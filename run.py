import asyncio
from pyppeteer import launch

async def main():
    # Launch a new browser instance
    browser = await launch(headless=True)
    # Create a new page
    page = await browser.newPage()
    # Set the user agent
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
    # Navigate to the website
    await page.goto("https://youtube.com/@devmrshadow")
    # Wait for the element with the text "Subscribe" to load
    await page.waitForXPath("//yt-formatted-string[normalize-space()='Subscribe']")
    # Scroll down until the element with the text "Subscribe" is found
    await page.xpath("//yt-formatted-string[normalize-space()='Subscribe']")
    # Wait for the button to appear and be clickable
    print("Trying to find Canva Pro for you! Please wait 60s...")
    await page.waitForXPath("//*[@id='subscribe-button']", {'visible': True, 'timeout': 70000})
    button = await page.xpath("//*[@id='subscribe-button']")
    # Click the button that opens the new tab
    await button[0].click()
    # Wait for the new tab to open
    await asyncio.sleep(5)
    # Get the handle of the new tab
    new_tab = (await browser.pages())[-1]
    # Switch to the new tab
    await new_tab.bringToFront()
    # Extract the href link from the button
    href_link = await new_tab.xpath("//a[text()='here']")
    href_link = await (await href_link[0].getProperty('href')).jsonValue()
    #Print the link of canva pro in a text file
    with open("canva_pro_link.txt", "w") as f:
        f.write("https://www.canva.com/brand/join?token=vqo4_F-eXE5mHPVoQSclsg&referrer=team-invite")
        print("Canva Pro Found!")
    # Close the browser instance
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
