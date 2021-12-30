from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json
from datetime import datetime
import glob
from pathlib import Path
from  random import choice

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sing_up(self):
        self.manager.current="signup_screen"
    def login(self,uname,passw):
        with open("users.json","r") as f:
            users=json.load(f)
        if uname in users and passw==users[uname]['password']:
            self.manager.current="login_screen_success"
        else:
            self.ids.login_wrong.text="wrong login"


class SignupScreen(Screen):
    def add_user(self,uname,passw):
        with open("users.json","r") as f:
            users=json.load(f)
        users[uname]={'username':uname,
                      'password':passw,
                      'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print(users)
        with open("users.json","w") as f:
            json.dump(users,f)
        self.manager.current="signup_screen_success"

class SignupScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"

class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"
    def enlight(self,feeling):
        feeling=feeling.lower()
        available_feeling=[Path(f).stem for f in glob.glob("quotes/*txt")]
        if feeling in available_feeling:
            with open("quotes/"+feeling+".txt") as f:
                lines=f.readlines()
            self.ids.quote.text=choice(lines)
        else:
            self.ids.quote.text="Try another!"


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
