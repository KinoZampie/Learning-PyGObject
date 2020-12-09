import gi
gi.require_version("Gtk","3.0")
import os
from gi.repository import Gtk

class Logout_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Logout Options")

        self.box = Gtk.VBox(spacing=0)
        self.add(self.box)

        self.shutdown = Gtk.Button(label="Shutdown", margin=4)
        self.shutdown.connect("clicked",self.shutdown_command)
        self.box.pack_start(self.shutdown,True,True,0)
        
        self.reboot = Gtk.Button(label="Reboot", margin=4)
        self.reboot.connect("clicked",self.reboot_command)
        self.box.pack_start(self.reboot,True,True,0)

        self.logout = Gtk.Button(label="Logout", margin=4)
        self.logout.connect("clicked",self.logout_command)
        self.box.pack_start(self.logout,True,True,0)

    def shutdown_command(self,widget):
        os.system("poweroff")
    def reboot_command(self,widget):
        os.system("reboot")
    def logout_command(self,widget):
        os.system("lxsession-logout --prompt 'Shutdown Options'")

win = Logout_Window()
win.connect("destroy",Gtk.main_quit)
for x in dir(win.box.props):
    print(x)
win.show_all()
win.set_property("width_request",300)
win.set_property("height_request",140)
Gtk.main()