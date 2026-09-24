from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://leetcode.com/problems/two-sum/")
login_button = page.get_by_role('link',name="Log in").first
login_button.wait_for()
login_button.highlight()
login_button.hide_highlight()
login_button.click()
username_field = page.get_by_placeholder('Username or E-mail')
password_field = page.get_by_placeholder('Password')
username_field.fill('arjunthedestroyer') # type: ignore
password_field.fill('Rajarani@1910')