from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase


Builder.load_file('principal.kv') 

class Principal(Screen):
    theme_cls = ThemeManager()
    pass
