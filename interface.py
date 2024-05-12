import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class ReadMyMailApp(App):
    def build(self):
        def read_mail() -> str:
            read_file = open("mail_archive.txt", "r")
            mail_rows = read_file.read()
            read_file.close()
            return str(mail_rows)

        box1 = BoxLayout(orientation="vertical")
        lbl1 = Label(font_size=18, text=read_mail(), markup=True)
        lbl2 = Label(
            size_hint=(1, 0.1),
            text="Read my Mail by Virtualis Lab",
        )
        box1.add_widget(lbl1)
        box1.add_widget(lbl2)
        return box1


mail_app = ReadMyMailApp()

if __name__ == "__main__":
    mail_app.run()
