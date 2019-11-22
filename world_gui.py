# first steps with a Python GUI
from tkinter import filedialog
import tkinter as tk
import universe as com
from community_gui import CommunityGui
from typing import List
import os


class WorldGui:

    def __init__(self, world: com.World):
        assert world is not None, 'world not provided'
        assert isinstance(world, com.World), 'invalid world'
        #
        self.__world__ = world
        if world is not None:
            world.set_communities_updated_callback(self.__world_detail__)
        # real communities and families will always have id > 0
        self.__selected_community_id__ = 0
        #
        self.__main_window__ = tk.Tk()
        self.__main_window__.title('World')
        self.__main_window__.geometry('1000x500')
        #
        self.__frame__ = tk.Frame(master=self.__main_window__)
        self.__frame__.grid(row=1, column=0, sticky='NW')
        # the UI setup
        self.__exit_save_load_world__()
        self.__world_detail__()
        #
        self.__main_window__.mainloop()

    def __world_detail__(self):
        # start by deleting any previous content
        if not hasattr(self, '__world_frame__'):
            self.__world_frame__ = None
        elif self.__world_frame__ is not None:
            self.__world_frame__.destroy()
        # now draw the content from scratch
        self.__world_frame__ = tk.Frame(
            master=self.frame, highlightbackground='black', highlightthickness=1)
        # this gives us padding on the right-side and bottom, but the top & left-side
        #  still have the widgets crammed without any padding against the border, hmmmm?
        self.__world_frame__.grid(row=0, column=0, sticky='NW', padx=(
            5, 2.5), pady=2.5, ipadx=2.5, ipady=2.5)
        #
        self.__world_detail_static__()
        self.__world_detail_dynamic__()

    def __exit_save_load_world__(self):
        if not hasattr(self, '__load_save_frame__'):
            self.__load_save_frame__ = None
        elif self.__load_save_frame__ is not None:
            self.__load_save_frame__.destroy()
        #
        self.__load_save_frame__ = tk.Frame(master=self.__main_window__)
        self.__load_save_frame__.grid(
            row=0, column=0, sticky='W', padx=(5, 2.5), pady=(5, 2.5))
        #
        tk.Button(master=self.__load_save_frame__,
                  text='Exit',
                  command=lambda: self.__main_window__.destroy(),
                  highlightbackground='black',
                  ).grid(row=0, column=0, sticky='W')
        tk.Label(master=self.__load_save_frame__, width=3).grid(
            row=0, column=1, sticky='W')
        tk.Button(master=self.__load_save_frame__,
                  text='Load world',
                  highlightbackground='blue',
                  command=lambda: self.__load_world__(),
                  ).grid(row=0, column=2, sticky='W')
        tk.Button(master=self.__load_save_frame__,
                  text='Save world',
                  highlightbackground='blue',
                  command=lambda: self.__save_world__(),).grid(row=0, column=3, sticky='W')
        tk.Button(master=self.__load_save_frame__,
                  text='Save world as...',
                  highlightbackground='blue',
                  command=lambda: self.__save_world__(save_as=True),).grid(row=0, column=4, sticky='W')

    def __load_world__(self):
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(), title='Load a World, from...')
        if not filename:
            return
        self.filename = filename
        #
        if not hasattr(self, '__load_save_error__'):
            self.__load_save_error__ = None
        elif self.__load_save_error__ is not None:
            self.__load_save_error__.destroy()
        #
        try:
            self.__world__ = com.World.load_from_file(self.filename)
            # re-instate the callback
            self.world.set_communities_updated_callback(self.__world_detail__)
            #
            self.__world_detail__()
        except BaseException as error:
            self.__load_save_error__ = tk.Label(
                master=self.__load_save_frame__, text=error.args)
            self.__load_save_error__.grid(row=0, column=5, sticky='W')
            return
        self.__load_save_error__ = tk.Label(
            master=self.__load_save_frame__, text='Success! (loaded from ' + self.filename + ')')
        self.__load_save_error__.grid(row=0, column=5, sticky='W')

    @property
    def filename_not_set(self):
        if not hasattr(self, 'filename'):
            self.filename = None
            return True
        if not self.filename:
            return True
        return False

    def __save_world__(self, save_as: bool = False):
        if save_as or self.filename_not_set:
            filename = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), title='Save the World, to...')
            if not filename:
                return
            self.filename = filename
        #
        if not hasattr(self, '__load_save_error__'):
            self.__load_save_error__ = None
        elif self.__load_save_error__ is not None:
            self.__load_save_error__.destroy()
        #
        try:
            self.world.store_to_file(self.filename)
        except BaseException as error:
            self.__load_save_error__ = tk.Label(
                master=self.__load_save_frame__, text=error.args)
            self.__load_save_error__.grid(row=0, column=5, sticky='W')
            return
        self.__load_save_error__ = tk.Label(
            master=self.__load_save_frame__, text='You saved the world! (to ' + self.filename + ')')
        self.__load_save_error__.grid(row=0, column=5, sticky='W')

    @property
    def world(self): return self.__world__

    @property
    def frame(self): return self.__frame__

    @property
    def selected_community_id(self): return self.__selected_community_id__
    @selected_community_id.setter
    def selected_community_id(self, value: int):
        assert isinstance(value, int), 'value must be an int'
        self.__selected_community_id__ = value

    @property
    def selected_community(self):
        comms = [
            comm for comm in self.world.all_communities if comm.id == self.selected_community_id]
        if len(comms) > 0:
            return comms[0]
        return None

    def select_community_id(self, id: int = 0):
        assert isinstance(id, int), 'community ID must be an int'
        self.selected_community_id = id
        self.__community_detail__()

    # a wrapper method to clear the previous frame before re-displaying the selected community
    def __community_detail__(self):
        if not hasattr(self, '__community_frame__'):
            self.__community_frame__ = None
        elif self.__community_frame__ is not None:
            self.__community_frame__.destroy()
        self.__community_frame__ = tk.Frame(master=self.frame)
        self.__community_frame__.grid(row=0, column=1, sticky='N')
        #
        if self.selected_community is not None:
            self.selected_community.set_notify_container(self.__world_detail__)
        CommunityGui(community=self.selected_community,
                     frame=self.__community_frame__)

    def create_community(self):
        com_name = self.__new_community_entry__.get()
        try:
            comm = com.Community(name=com_name)
            self.world.community_add(community=comm)
            comm.set_notify_container(self.__world_detail__)
        except AssertionError as error:
            tk.Label(master=self.__static_frame__,
                     text=error.args).grid(row=1, column=2)

    #
    # the World Detail section
    #
    def __world_detail_static__(self):
        if not hasattr(self, '__static_frame__'):
            self.__static_frame__ = None
        elif self.__static_frame__ is not None:
            self.__static_frame__.destroy()
        self.__static_frame__ = tk.Frame(master=self.__world_frame__)
        self.__static_frame__.grid(row=1, column=0, sticky='NW')
        #
        tk.Button(master=self.__static_frame__,
                  text='Rename to',
                  highlightbackground='blue',
                  command=lambda: self.rename_world()
                  ).grid(row=0, column=0, sticky='NW')
        self.__name_entry__ = tk.Entry(master=self.__static_frame__,
                                       width=10)
        self.__name_entry__.grid(row=0, column=1)
        #
        tk.Button(master=self.__static_frame__, text='New Community',
                  command=self.create_community,
                  highlightbackground='blue',
                  ).grid(row=1, column=0, sticky='NW')
        self.__new_community_entry__ = tk.Entry(
            master=self.__static_frame__, width=10)
        self.__new_community_entry__.grid(row=1, column=1)

    def rename_world(self):
        new_name = self.__name_entry__.get()
        try:
            self.world.name = new_name
        except AssertionError as error:
            tk.Label(master=self.__static_frame__,
                     text=error.args).grid(row=0, column=2)

    def __world_detail_dynamic__(self):
        if not hasattr(self, '__dynamic_frame__'):
            self.__dynamic_frame__ = None
        elif self.__dynamic_frame__ is not None:
            self.__dynamic_frame__.destroy()
        self.__dynamic_frame__ = tk.Frame(master=self.__world_frame__)
        self.__dynamic_frame__.grid(row=2, column=0, sticky='NW')
        #
        self.__main_title_set__()
        row = 0
        for community in self.world.all_communities:
            self.__community_row__(community=community, row=row)
            row += 1
        self.__community_detail__()

    def __main_title_set__(self):
        communities = ' communities' if len(
            self.world.all_communities) != 1 else ' community'
        text = self.world.name + ': ' + \
            str(len(self.world.all_communities)) + communities
        tk.Label(master=self.__world_frame__, text=text).grid(
            row=0, column=0)

    def __community_row__(self, community: com.Community, row: int):
        assert community is not None, 'community not provided'
        assert isinstance(row, int), 'row should be an int'
        #
        tk.Button(master=self.__dynamic_frame__,
                  command=lambda: self.world.community_remove(community),
                  highlightbackground='red',
                  text='X').grid(row=row, column=0, sticky='NW')
        #
        text = str(community.id) + '. ' + community.name
        highlightbackground = 'purple' if community.id == self.selected_community_id else 'black'
        tk.Button(master=self.__dynamic_frame__,
                  command=lambda: self.__select_community__(community),
                  highlightbackground=highlightbackground,
                  text=text).grid(row=row, column=1, sticky='NW')

    def __select_community__(self, community):
        assert isinstance(community, com.Community)
        self.select_community_id(community.id)
        # this is to re-display the rows with the correct button colors
        self.__world_detail__()


if __name__ == '__main__':
    WorldGui(world=com.World(name='Earth'))
