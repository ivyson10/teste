from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.theming import ThemeManager

Builder.load_file('login.kv') 

class Login(Screen):
    theme_cls = ThemeManager()
    pass