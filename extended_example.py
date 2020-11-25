import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello world")
        self.button = Gtk.Button(label="I am a button")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
    
    def on_button_clicked(self,widget):
        print("Hello world!!!")

win = MainWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()

win2 = MainWindow()
win2.connect("destroy",Gtk.main_quit)
win2.show_all()
Gtk.main()