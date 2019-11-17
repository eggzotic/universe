# first steps with a Python GUI
import tkinter as tk
import universe as com
from typing import List, Set, Dict


class UniverseGui:

    def __init__(self):
        self.__constants_init__()
        # the primary data model
        self.world = com.World(name='Earth',
                               communities_updated_callback=self.__world_detail_dynamic__)
        # real communities and families will always have id > 0
        self.__selected_community_id__ = 0
        self.__selected_family_id__ = 0
        #
        self.main_window = tk.Tk(screenName=None, baseName=None,
                                 className='World', useTk=1)
        self.main_window.geometry('1000x500')
        # the UI setup
        #
        self.__exit_button_setup__()
        self.__world_detail_static__()
        self.__world_detail_dynamic__()
        #
        self.family_removal_buttons: List[tk.Button] = []
        self.family_detail_buttons: List[tk.Button] = []
        #
        self.family_parent_detail_buttons: List[tk.Button] = []
        self.family_parent_remove_buttons: List[tk.Button] = []
        #
        self.family_child_detail_buttons: List[tk.Button] = []
        self.family_child_remove_buttons: List[tk.Button] = []
        #
        self.main_window.mainloop()

    @property
    def selected_community_id(self): return self.__selected_community_id__
    @selected_community_id.setter
    def selected_community_id(self, value: int):
        assert isinstance(value, int), 'value must be an int'
        self.__selected_community_id__ = value

    @property
    def selected_family_id(self): return self.__selected_family_id__
    @selected_family_id.setter
    def selected_family_id(self, value: int):
        assert isinstance(value, int), 'value must be an int'
        self.__selected_family_id__ = value

    @property
    def selected_community(self):
        comms = [
            comm for comm in self.world.all_communities if comm.id == self.selected_community_id]
        if len(comms) > 0:
            return comms[0]
        return None

    @property
    def selected_family(self):
        selected_comm = self.selected_community
        if selected_comm is None:
            return None
        fams = [fam for fam in selected_comm.all_families if fam.id ==
                    self.selected_family_id]
        if len(fams) > 0:
            return fams[0]
        return None

    def create_community(self):
        com_name = self.__new_community_entry__.get()
        text_len = len(com_name)
        self.__new_community_entry__.delete(0, text_len)
        try:
            self.world.new_community(
                # name=com_name, families_updated_callback=self.__community_detail_dynamic__)
                name=com_name, families_updated_callback=self.__community_detail__)
        except AssertionError as error:
            print('Failed to create new community:', str(error.args[0]))
            self.__community_create_error_label__ = tk.Label(master=self.main_window,
                                                             text=error.args)
            self.__community_create_error_label__.grid(row=1, column=2)
            return
        if not hasattr(self, '__community_create_error_label__'):
            self.__community_create_error_label__ = None
        if self.__community_create_error_label__ is not None:
            self.__community_create_error_label__.destroy()

    def create_family(self, community: com.Community):
        assert community is not None and isinstance(
            community, com.Community), 'invalid community'
        fam_name = self.__new_family_entry__.get()
        text_len = len(fam_name)
        self.__new_family_entry__.delete(0, text_len)
        try:
            community.new_family(
                name=fam_name, members_updated_callback=self.__family_detail__)
        except AssertionError as error:
            print('Failed to create new family:', str(error.args[0]))
            self.__family_create_error_label__ = tk.Label(
                master=self.main_window, text=error.args)
            self.__family_create_error_label__.grid(row=3, column=4)
            return
        if not hasattr(self, '__family_create_error_label__'):
            self.__family_create_error_label__ = None
        if self.__family_create_error_label__ is not None:
            self.__family_create_error_label__.destroy()

    def create_family_parent(self, family: com.Family):
        assert family is not None, 'family not provided'
        assert isinstance(family, com.Family), 'invalid family'
        #
        member_name = self.__new_family_parent_entry__.get()
        #
        member_age = self.__new_family_parent_age_entry__.get()
        member_age = int(member_age)
        #
        try:
            family.parent_add(person=com.Person(
                name=member_name, age=member_age))
        except AssertionError as error:
            print('Error:', error.args)

    def create_family_child(self, family: com.Family):
        assert family is not None, 'family not provided'
        assert isinstance(family, com.Family), 'invalid family'
        #
        member_name = self.__new_family_child_entry__.get()
        #
        member_age = self.__new_family_child_age_entry__.get()
        member_age = int(member_age)
        #
        try:
            family.child_add(person=com.Person(
                name=member_name, age=member_age))
        except AssertionError as error:
            print('Error:', error.args)

    #
    # revamped methods below here
    #

    def __constants_init__(self):
        self.__first_community_row__: int = 2
        self.__first_family_row__: int = 4
        self.__family_title_row__: int = 4
        self.__new_family_parent_row__: int = 5
        self.__new_family_child_row__: int = self.__new_family_parent_row__ + 1
        self.__first_family_parent_row__: int = self.__new_family_child_row__ + 1
        self.__first_family_child_row__: int = self.__first_family_parent_row__ + 1

    #
    # the World Detail section
    #
    def __main_title_set__(self):
        if not hasattr(self, 'title'):
            self.title = None
        if self.title is not None:
            self.title.destroy()
        if len(self.world.all_communities) == 1:
            communities = ' community'
        else:
            communities = ' communities'
        self.title = tk.Label(master=self.main_window, text=self.world.name +
                              ': ' + str(len(self.world.all_communities)) + communities)
        self.title.grid(row=0, column=0)

    def __exit_button_setup__(self):
        tk.Button(master=self.main_window,
                  text='Exit',
                  command=self.main_window.destroy,
                  highlightbackground='black',
                  ).grid(row=0, column=1)

    def __world_detail_static__(self):
        tk.Button(master=self.main_window, text='New Community',
                  command=self.create_community,
                  highlightbackground='blue',
                  ).grid(row=1, column=0)
        self.__new_community_entry__ = tk.Entry(master=self.main_window, width=10)
        self.__new_community_entry__.grid(row=1, column=1)
        #

    def __world_detail_dynamic__(self):
        #
        self.__main_title_set__()
        self.__world_detail_clear__()
        self.__world_detail_update__()

    def __world_detail_clear__(self):
        if not hasattr(self, '__community_removal_buttons__') or not hasattr(self, '__community_detail_buttons__'):
            self.__community_removal_buttons__: List[tk.Button] = []
            self.__community_detail_buttons__: List[tk.Button] = []
            return
        for button in self.__community_removal_buttons__:
            button.destroy()
        for button in self.__community_detail_buttons__:
            button.destroy()

    def __world_detail_update__(self):
        row = self.__first_community_row__
        for community in self.world.all_communities:
            self.__community_row__(community=community, row=row)
            row += 1
        self.__community_detail__()

    def __community_row__(self, community: com.Community, row: int):
        assert community is not None, 'community not provided'
        assert isinstance(row, int), 'row should be an int'
        #
        # the remove-community buttons
        community_remove_button = tk.Button(master=self.main_window,
                                            command=lambda: self.world.community_remove(
                                                community),
                                            highlightbackground='red',
                                            text='X')
        self.__community_removal_buttons__.append(community_remove_button)
        community_remove_button.grid(row=row, column=0)
        #
        community_detail_button = tk.Button(master=self.main_window,
                                            command=lambda: self.__community_detail__(
                                                community=community),
                                            highlightbackground='black',
                                            text=str(
                                                community.id) + '. ' + community.name)
        self.__community_detail_buttons__.append(community_detail_button)
        community_detail_button.grid(row=row, column=1)

    #
    # the Community Detail Section
    #
    def __community_detail__(self, community: com.Community = None):
        # this covers the case where this method is called from the data-model callback
        if community is not None:
            assert isinstance(community, com.Community), 'invalid community'
            self.selected_community_id = community.id
        #
        self.__community_detail_static__()
        self.__community_detail_dynamic__()
        self.__family_detail__()

    def __community_detail_static__(self):
        if not hasattr(self, '__new_family_button__'):
            self.__new_family_button__ = None
        if self.__new_family_button__ is not None:
            self.__new_family_button__.destroy()
        #
        if not hasattr(self, '__new_family_entry__'):
            self.__new_family_entry__ = None
        if self.__new_family_entry__ is not None:
            self.__new_family_entry__.destroy()
        #
        community = self.selected_community
        if community is None: return
        #
        self.__new_family_button__ = tk.Button(master=self.main_window,
                                               text='New Family',
                                               command=lambda: self.create_family(
                                                   community),
                                               highlightbackground='blue')
        self.__new_family_button__.grid(row=3, column=2)
        #
        self.__new_family_entry__ = tk.Entry(master=self.main_window, width=10)
        self.__new_family_entry__.grid(row=3, column=3)

    def __community_detail_dynamic__(self):
        self.__community_title_set__()
        self.__community_detail_clear__()
        #
        community = self.selected_community
        if community is None: return
        #
        row = self.__first_family_row__
        for family in community.all_families:
            self.__family_row__(community=community, family=family, row=row)
            row += 1

    def __community_detail_clear__(self):
        if not hasattr(self, '__family_delete_buttons__'):
            self.__family_delete_buttons__: List[tk.Button] = []
            self.__family_detail_buttons__: List[tk.Button] = []
            return
        for button in self.__family_delete_buttons__:
            button.destroy()
        for button in self.__family_detail_buttons__:
            button.destroy()
        self.__family_delete_buttons__: List[tk.Button] = []
        self.__family_detail_buttons__: List[tk.Button] = []

    def __family_row__(self, community: com.Community, family: com.Family, row: int):
        assert row is not None, 'row not provided'
        assert isinstance(row, int), 'row must be an int'
        #
        family_remove_button = tk.Button(master=self.main_window,
                                         command=lambda: community.family_remove(
                                             family),
                                         highlightbackground='red',
                                         text='X')
        family_remove_button.fam_id = family.id
        self.__family_delete_buttons__.append(family_remove_button)
        family_remove_button.grid(row=row, column=2)
        #
        family_detail_button = tk.Button(master=self.main_window,
                                         command=lambda: self.__family_detail__(
                                             family),
                                         highlightbackground='black',
                                         text=str(family.id) + '. ' + family.name)
        family_detail_button.fam_id = family.id
        self.__family_detail_buttons__.append(family_detail_button)
        family_detail_button.grid(row=row, column=3)

    def __community_title_set__(self):
        if not hasattr(self, '__community_summary_label__'):
            self.__community_summary_label__ = None
        if self.__community_summary_label__ is not None:
            self.__community_summary_label__.destroy()
        #
        # ignore if the selected community does not exist
        if self.selected_community_id not in [comm.id for comm in self.world.all_communities]:
            return
        # summary label
        community = self.selected_community
        if community is None: return

        fam_count = len(community.all_families)
        families = ' family' if fam_count == 1 else ' families'

        #
        self.__community_summary_label__ = tk.Label(master=self.main_window,
                                                    text=community.name + ': ' +
                                                    str(fam_count) + families)
        self.__community_summary_label__.grid(row=2, column=2)
    #
    # Family detail section
    #

    def __family_detail__(self, family: com.Family = None):
        if family is not None:
            assert isinstance(family, com.Family), 'invalid family'
            self.selected_family_id = family.id
        #
        self.__family_detail_static__()
        self.__family_detail_dynamic__()

    def __family_detail_dynamic__(self):
        self.__family_title_set__()
        self.__family_detail_clear__()
        #
        family = self.selected_family
        if family is None: return

        row = self.__first_family_parent_row__
        for parent in family.parents:
            self.__parent_row__(family=family, parent=parent, row=row)
            row += 1
        for child in family.children:
            self.__child_row__(family=family, child=child, row=row)
            row += 1

    def __parent_row__(self, family: com.Family, parent: com.Person, row: int):
        parent_remove_button = tk.Button(master=self.main_window,
                                         text='X',
                                         command=lambda: family.parent_remove(
                                             person=parent),
                                         highlightbackground='red')
        self.__family_member_delete_buttons__.append(parent_remove_button)
        parent_remove_button.grid(row=row, column=4)
        #
        parent_detail_button = tk.Button(master=self.main_window,
                                         text='P: ' +
                                         str(parent.id) +
                                         ': ' + parent.name,
                                         command=lambda: print(
                                             family.name, 'detail requested:', parent.name),
                                         highlightbackground='black')
        self.__family_member_detail_buttons__.append(parent_detail_button)
        parent_detail_button.grid(row=row, column=5)

    def __child_row__(self, family: com.Family, child: com.Person, row: int):
        child_remove_button = tk.Button(master=self.main_window,
                                        text='X',
                                        command=lambda: family.child_remove(
                                             person=child),
                                        highlightbackground='red')
        self.__family_member_delete_buttons__.append(child_remove_button)
        child_remove_button.grid(row=row, column=4)
        #
        child_detail_button = tk.Button(master=self.main_window,
                                        text='C: ' +
                                        str(child.id) +
                                        ': ' + child.name,
                                        command=lambda: print(
                                            family.name, 'detail requested:', child.name),
                                        highlightbackground='black')
        self.__family_member_detail_buttons__.append(child_detail_button)
        child_detail_button.grid(row=row, column=5)

    def __family_detail_clear__(self):
        if not hasattr(self, '__family_member_delete_buttons__'):
            self.__family_member_delete_buttons__: List[tk.Button] = []
            self.__family_member_detail_buttons__: List[tk.Button] = []
            return
        for button in self.__family_member_delete_buttons__:
            button.destroy()
        for button in self.__family_member_detail_buttons__:
            button.destroy()
        self.__family_member_delete_buttons__: List[tk.Button] = []
        self.__family_member_detail_buttons__: List[tk.Button] = []

    def __family_title_set__(self):
        if not hasattr(self, '__family_summary_label__'):
            self.__family_summary_label__ = None
        if self.__family_summary_label__ is not None:
            self.__family_summary_label__.destroy()
        #
        family = self.selected_family
        if family is None: return

        member_count = family.population
        self.__family_summary_label__ = tk.Label(master=self.main_window,
                                                 text=family.name + ': ' + str(member_count) + ' members')
        self.__family_summary_label__.grid(
            row=self.__family_title_row__, column=4)

    def __family_detail_static__(self):
        #
        # new parent
        #
        if not hasattr(self, '__new_family_parent_button__'):
            self.__new_family_parent_button__ = None
        if self.__new_family_parent_button__ is not None:
            self.__new_family_parent_button__.destroy()
        #
        if not hasattr(self, '__new_family_parent_hint__'):
            self.__new_family_parent_hint__ = None
        if self.__new_family_parent_hint__ is not None:
            self.__new_family_parent_hint__.destroy()
        #
        if not hasattr(self, '__new_family_parent_entry__'):
            self.__new_family_parent_entry__ = None
        if self.__new_family_parent_entry__ is not None:
            self.__new_family_parent_entry__.destroy()
        #
        if not hasattr(self, '__new_family_parent_age_hint__'):
            self.__new_family_parent_age_hint__ = None
        if self.__new_family_parent_age_hint__ is not None:
            self.__new_family_parent_age_hint__.destroy()
        #
        if not hasattr(self, '__new_family_parent_age_entry__'):
            self.__new_family_parent_age_entry__ = None
        if self.__new_family_parent_age_entry__ is not None:
            self.__new_family_parent_age_entry__.destroy()
        #
        # new child
        #
        if not hasattr(self, '__new_family_child_button__'):
            self.__new_family_child_button__ = None
        if self.__new_family_child_button__ is not None:
            self.__new_family_child_button__.destroy()
        #
        if not hasattr(self, '__new_family_child_hint__'):
            self.__new_family_child_hint__ = None
        if self.__new_family_child_hint__ is not None:
            self.__new_family_child_hint__.destroy()
        #
        if not hasattr(self, '__new_family_child_entry__'):
            self.__new_family_child_entry__ = None
        if self.__new_family_child_entry__ is not None:
            self.__new_family_child_entry__.destroy()
        #
        if not hasattr(self, '__new_family_child_age_hint__'):
            self.__new_family_child_age_hint__ = None
        if self.__new_family_child_age_hint__ is not None:
            self.__new_family_child_age_hint__.destroy()
        #
        if not hasattr(self, '__new_family_child_age_entry__'):
            self.__new_family_child_age_entry__ = None
        if self.__new_family_child_age_entry__ is not None:
            self.__new_family_child_age_entry__.destroy()
        #
        family = self.selected_family
        if family is None: return
        #
        self.__new_family_parent_button__ = tk.Button(master=self.main_window,
                                                      text='New Parent',
                                                      command=lambda: self.create_family_parent(
                                                          family),
                                                      highlightbackground='blue')
        self.__new_family_parent_button__.grid(
            row=self.__new_family_parent_row__, column=4)
        #
        self.__new_family_parent_hint__ = tk.Label(
            master=self.main_window, text='Parent: ')
        self.__new_family_parent_hint__.grid(
            row=self.__new_family_parent_row__, column=5)
        self.__new_family_parent_entry__ = tk.Entry(
            master=self.main_window, width=10)
        self.__new_family_parent_entry__.grid(
            row=self.__new_family_parent_row__, column=6)
        #
        self.__new_family_parent_age_hint__ = tk.Label(
            master=self.main_window, text='Age: ')
        self.__new_family_parent_age_hint__.grid(
            row=self.__new_family_parent_row__, column=7)
        self.__new_family_parent_age_entry__ = tk.Entry(
            master=self.main_window, width=5)
        self.__new_family_parent_age_entry__.grid(
            row=self.__new_family_parent_row__, column=8)
        #
        self.__new_family_child_button__ = tk.Button(master=self.main_window,
                                                     text='New Child',
                                                     command=lambda: self.create_family_child(
                                                          family),
                                                     highlightbackground='blue')
        self.__new_family_child_button__.grid(
            row=self.__new_family_child_row__, column=4)
        self.__new_family_child_hint__ = tk.Label(
            master=self.main_window, text='Child: ')
        self.__new_family_child_hint__.grid(
            row=self.__new_family_child_row__, column=5)
        self.__new_family_child_entry__ = tk.Entry(
            master=self.main_window, width=10)
        self.__new_family_child_entry__.grid(
            row=self.__new_family_child_row__, column=6)
        self.__new_family_child_age_hint__ = tk.Label(
            master=self.main_window, text='Age: ')
        self.__new_family_child_age_hint__.grid(
            row=self.__new_family_child_row__, column=7)
        self.__new_family_child_age_entry__ = tk.Entry(
            master=self.main_window, width=5)
        self.__new_family_child_age_entry__.grid(
            row=self.__new_family_child_row__, column=8)


#
if __name__ == '__main__':
    UniverseGui()
#
# EOF
#
