from playwright.sync_api import sync_playwright
import json

from playwright.sync_api import sync_playwright, ViewportSize

class PWscreenshort:
    def takeScreenShot(url, dt_str,index: str = '', selector: str = '[data-test-id="post-content"]', is_nsfw: bool = False):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()

            cookie_file = open("get_screenshot/cookie-dark-mode.json", encoding="utf-8")

            cookies = json.load(cookie_file)
            context.add_cookies(cookies)  
            
            page = context.new_page()
            page.goto(url, timeout=0)

            if is_nsfw:
                page.locator('#AppRouter-main-content > div > div:nth-child(1) > div > div > div._3-bzOoWOXVn2xJ3cljz9oC > button').click()
            
            page.set_viewport_size(ViewportSize(width=1920, height=1080))
            page.locator(selector).screenshot(path=f"./assets/files_{dt_str}/{index}_post_{dt_str}.png")
            browser.close()
