from BookClass import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    bookname = ObjectProperty()
    authorname = ObjectProperty()
    shortsinopse = ObjectProperty()
    publishingcompany = ObjectProperty()
    publicationyear = ObjectProperty()
    genre = ObjectProperty()
    volume = ObjectProperty()
    rating = ObjectProperty()

    def press(self):
        newbook = Book(
            self.bookname.text,
            self.authorname.text,
            self.shortsinopse.text,
            self.publishingcompany.text,
            self.publicationyear.text,
            self.genre.text,
            self.volume.text,
            self.rating.text
        )
        newbook.add_book_func()

        self.bookname.text = ""
        self.authorname.text = ""
        self.shortsinopse.text = ""
        self.publishingcompany.text = ""
        self.publicationyear.text = ""
        self.genre.text = ""
        self.volume.text = ""
        self.rating.text = ""


class MyLibApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyLibApp().run()
