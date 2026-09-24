from playwright.sync_api import Page
from dotenv import load_dotenv
import os,time

load_dotenv()

def test_leet(page:Page):
    page.goto("https://leetcode.com/problems/two-sum/")
    login_button = page.get_by_role('link',name="Log in").first
    login_button.wait_for()
    login_button.highlight()
    login_button.hide_highlight()
    login_button.click()
    username_field = page.get_by_placeholder('Username or E-mail')
    password_field = page.get_by_placeholder('Password')
    print('Konnichuwa')
    username_field.fill(os.getenv('USERNAME_')) # type: ignore
    password_field.fill(os.getenv('PASSWORD')) # type: ignore
    # page.wait_for_timeout(5000)
    

