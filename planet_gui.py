# first steps with a Python GUI
import tkinter as tk
import universe as com
from community_gui import CommunityGui
from typing import List


class PlanetGui:

    def __init__(self, world: com.World):
        assert world is not None, 'world not provided'
        assert isinstance(world, com.World), 'invalid world'
        #
        self.__world__ = world
        world.set_communities_updated_callback(self.__world_detail__)
        # real communities and families will always have id > 0
        self.__selected_community_id__ = 0
        #
        self.__main_window__ = tk.Tk()
        self.__main_window__.title('World')
        self.__main_window__.geometry('1000x500')
        #
        self.__frame__ = tk.Frame(master=self.__main_window__)
        self.__frame__.grid(row=1, column=0, sticky='N')
        # the UI setup
        self.__exit_button_setup__()
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
        self.__world_frame__ = tk.Frame(master=self.frame)
        self.__world_frame__.grid(row=0, column=0, sticky='N')
        #
        self.__world_detail_static__()
        self.__world_detail_dynamic__()

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
        CommunityGui(community=self.selected_community,
                     frame=self.__community_frame__)

    def create_community(self):
        com_name = self.__new_community_entry__.get()
        try:
            self.world.new_community(name=com_name)
        except AssertionError as error:
            print('Failed to create new community:', str(error.args[0]))
            tk.Label(master=self.__world_frame__,
                     text=error.args).grid(row=1, column=2)

    def __exit_button_setup__(self):
        tk.Button(master=self.__main_window__,
                  text='Exit',
                  command=lambda: self.__main_window__.destroy(),
                  highlightbackground='black',
                  ).grid(row=0, column=0, sticky='NW')

    #
    # the World Detail section
    #
    def __world_detail_static__(self):
        tk.Button(master=self.__world_frame__, text='New Community',
                  command=self.create_community,
                  highlightbackground='blue',
                  ).grid(row=1, column=0)
        self.__new_community_entry__ = tk.Entry(
            master=self.__world_frame__, width=10)
        self.__new_community_entry__.grid(row=1, column=1)

    def __world_detail_dynamic__(self):
        self.__main_title_set__()
        row = 2
        for community in self.world.all_communities:
            self.__community_row__(community=community, row=row)
            row += 1
        self.__community_detail__()

    def __main_title_set__(self):
        if len(self.world.all_communities) == 1:
            communities = ' community'
        else:
            communities = ' communities'
        text = self.world.name + ': ' + \
            str(len(self.world.all_communities)) + communities
        tk.Label(master=self.__world_frame__, text=text).grid(row=0, column=0)

    def __community_row__(self, community: com.Community, row: int):
        assert community is not None, 'community not provided'
        assert isinstance(row, int), 'row should be an int'
        #
        tk.Button(master=self.__world_frame__,
                  command=lambda: self.world.community_remove(community),
                  highlightbackground='red',
                  text='X').grid(row=row, column=0)
        #
        text = str(community.id) + '. ' + community.name
        tk.Button(master=self.__world_frame__,
                  command=lambda: self.select_community_id(community.id),
                  highlightbackground='black',
                  text=text).grid(row=row, column=1)

if __name__ == '__main__':
    PlanetGui(world=com.World(name='Earth'))

