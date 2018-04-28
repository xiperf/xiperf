#!/usr/bin/env python3
""" Host an iperf3 server in a dedicated vte session
"""

import gi.repository.Gtk as Gtk
import gi.repository.Vte as Vte
import gi.repository.GLib as GLib

RUN_ARGV = ['iperf3', '-s']

def main():
    """ initialize gtk window, vte, and iperf3 -s
    """
    win = Gtk.Window()
    vte = Vte.Terminal()
    win.add(vte)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    vte.spawn_sync(
        pty_flags=Vte.PtyFlags.DEFAULT,
        working_directory=None,
        argv=RUN_ARGV,
        envv=None,
        spawn_flags=GLib.SpawnFlags.SEARCH_PATH_FROM_ENVP,
        child_setup=None,
        child_setup_data=None,
        cancellable=None,
    )
    Gtk.main()

if __name__ == '__main__':
    main()
