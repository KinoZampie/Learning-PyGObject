## YOO, I did this with my own brain, so happy :))

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class My_Label(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Hello there")
        self.label = Gtk.Label(label="Hello pals",angle=25)
        # Setting prop independantly (just add "set_ before prop name")
        # self.label.set_label("Hello everyone")
        self.add(self.label)


win = My_Label()

# How to see all the props for an object
print(dir(win.label.props))
# How to get the value of a property
print(win.label.get_property("label"))
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()
