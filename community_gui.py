import tkinter as tk
import universe as com
from family_gui import FamilyGui
from typing import List, Set, Dict


class CommunityGui:
    def __init__(self, community: com.Community, frame: tk.Frame):
        assert community is None or isinstance(
            community, com.Community), 'either pass a valid community, or None'
        assert frame is not None, 'frame not provided'
        assert isinstance(frame, tk.Frame), 'invalid frame'
        #
        super().__init__()
        #
        self.__frame__ = frame
        self.__community__ = community
        if community is not None:
            community.set_families_updated_callback(self.__community_detail__)
        self.__selected_family_id__ = 0
        #
        self.__community_detail__()

    @property
    def community(self): return self.__community__
    @property
    def frame(self): return self.__frame__
    #
    @property
    def selected_family_id(self): return self.__selected_family_id__
    @selected_family_id.setter
    def selected_family_id(self, value: int):
        assert isinstance(value, int), 'value must be an int'
        self.__selected_family_id__ = value

    @property
    def selected_family(self):
        if self.community is None:
            return None
        fams = [fam for fam in self.community.all_families if fam.id ==
                self.selected_family_id]
        if len(fams) > 0:
            return fams[0]
        return None

    #
    def select_family_id(self, id: int = 0):
        assert isinstance(id, int), 'family ID must be an int'
        self.selected_family_id = id
        self.__family_detail__()

    # a wrapper method to clear the previous frame before re-displaying the selected community
    def __family_detail__(self):
        if not hasattr(self, '__family_frame__'):
            self.__family_frame__ = None
        elif self.__family_frame__ is not None:
            self.__family_frame__.destroy()
        #
        self.__family_frame__ = tk.Frame(master=self.frame)
        self.__family_frame__.grid(row=0, column=3, sticky="N")
        #
        if self.selected_family is not None:
            self.selected_family.set_notify_container(self.__community_detail__)
        FamilyGui(family=self.selected_family,
                  frame=self.__family_frame__)
    #
    # actions for this class
    #

    def create_family(self, community: com.Community):
        assert isinstance(community, com.Community), 'invalid community'
        fam_name = self.__new_family_entry__.get()
        try:
            fam = com.Family(name=fam_name)
            community.family_add(family=fam)
        except AssertionError as error:
            tk.Label(master=self.__static_frame__,
                     text=error.args).grid(row=1, column=2)

    #
    # the Community Detail Section
    #
    def __community_detail__(self):
        # start by deleting any previous content
        if not hasattr(self, '__community_frame__'):
            self.__community_frame__ = None
        elif self.__community_frame__ is not None:
            self.__community_frame__.destroy()
        #
        self.__community_frame__ = tk.Frame(
            master=self.frame, highlightbackground='black', highlightthickness=1)
        self.__community_frame__.grid(row=0, column=0, sticky='N', padx=(
            5, 2.5), pady=2.5, ipadx=2.5, ipady=2.5)
        #
        # now draw the content from scratch
        self.__community_detail_static__()
        self.__community_detail_dynamic__()
        self.__family_detail__()

    def __community_detail_static__(self):
        if self.community is None:
            return
        #
        if not hasattr(self, '__static_frame__'):
            self.__static_frame__ = None
        elif self.__static_frame__ is not None:
            self.__static_frame__.destroy()
        self.__static_frame__ = tk.Frame(master=self.__community_frame__)
        self.__static_frame__.grid(row=1, column=0, sticky='NW')
        #
        tk.Button(master=self.__static_frame__,
                  text='Rename to',
                  highlightbackground='blue',
                  command=lambda: self.rename_community()
                  ).grid(row=0, column=0, sticky='NW')
        self.__name_entry__ = tk.Entry(master=self.__static_frame__,
                                       width=10)
        self.__name_entry__.grid(row=0, column=1)
        #
        tk.Button(master=self.__static_frame__,
                  text='New Family',
                  command=lambda: self.create_family(self.community),
                  highlightbackground='blue').grid(row=1, column=0, sticky='NW')
        #
        self.__new_family_entry__ = tk.Entry(
            master=self.__static_frame__, width=10)
        self.__new_family_entry__.grid(row=1, column=1)

    def rename_community(self):
        new_name = self.__name_entry__.get()
        try:
            self.community.name = new_name
        except AssertionError as error:
            tk.Label(master=self.__static_frame__,
                     text=error.args).grid(row=0, column=2)

    def __community_detail_dynamic__(self):
        self.__community_title_set__()
        #
        if self.community is None:
            return
        #
        if not hasattr(self, '__dynamic_frame__'):
            self.__dynamic_frame__ = None
        elif self.__dynamic_frame__ is not None:
            self.__dynamic_frame__.destroy()
        self.__dynamic_frame__ = tk.Frame(master=self.__community_frame__)
        self.__dynamic_frame__.grid(row=2, column=0, sticky='NW')
        #
        row = 0
        for family in self.community.all_families:
            self.__family_row__(family=family, row=row)
            row += 1

    def __family_row__(self, family: com.Family, row: int):
        assert isinstance(family, com.Family)
        assert isinstance(row, int), 'row must be an int'
        #
        tk.Button(master=self.__dynamic_frame__,
                  command=lambda: self.community.family_remove(family),
                  highlightbackground='red',
                  text='X').grid(row=row, column=0, sticky='NW')
        #
        text = str(family.id) + '. ' + family.name
        highlightbackground = 'purple' if family.id == self.selected_family_id else 'black'
        tk.Button(master=self.__dynamic_frame__,
                  command=lambda: self.__select_family__(family),
                  highlightbackground=highlightbackground,
                  text=text).grid(row=row, column=1, sticky='NW')

    def __select_family__(self, family):
        assert isinstance(family, com.Family), 'invalid family'
        self.select_family_id(family.id)
        # this is to re-display the rows with the correct button colors
        self.__community_detail__()

    def __community_title_set__(self):
        if self.community is None:
            return
        fam_count = len(self.community.all_families)
        families = ' family' if fam_count == 1 else ' families'
        #
        tk.Label(master=self.__community_frame__,
                 text=self.community.name +' community: ' +
                 str(fam_count) + families).grid(row=0, column=0)
