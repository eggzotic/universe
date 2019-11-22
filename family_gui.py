import tkinter as tk
import universe as com
from person_gui import PersonGui
from typing import List, Set, Dict


class FamilyGui:
    def __init__(self, family: com.Family, frame: tk.Frame):
        assert family is None or isinstance(
            family, com.Family), 'either pass a valid family, or None'
        assert isinstance(frame, tk.Frame), 'invalid frame'
        #
        super().__init__()
        #
        self.__frame__ = frame
        self.__family__ = family
        if family is not None:
            family.set_members_updated_callback(self.__family_detail__)
        self.__selected_member_id__ = 0
        #
        self.__family_detail__()

    @property
    def family(self): return self.__family__
    @property
    def frame(self): return self.__frame__

    @property
    def selected_person_id(self): return self.__selected_member_id__
    @selected_person_id.setter
    def selected_person_id(self, value: int):
        assert isinstance(value, int), 'value must be an int'
        self.__selected_member_id__ = value

    @property
    def selected_person(self):
        if self.family is None:
            return None
        peeps = [person for person in self.family.members if person.id ==
                 self.selected_person_id]
        if len(peeps) > 0:
            return peeps[0]
        return None

    #
    def select_person_id(self, id: int = 0):
        assert isinstance(id, int), 'person ID must be an int'
        self.selected_person_id = id
        self.__person_detail__()

    def create_family_parent(self):
        member_name = self.__new_family_parent_entry__.get()
        member_age = self.__new_family_parent_age_entry__.get()
        try:
            member_age = int(member_age)
        except ValueError:
            self.__error_label__ = tk.Label(
                master=self.__static_frame__, text='{invalid age}')
            self.__error_label__.grid(row=1, column=6)
            return
        #
        if not hasattr(self, '__error_label__'):
            pass
        elif self.__error_label__ is not None:
            self.__error_label__.destroy()
        gender_name = self.new_parent_gender_var.get()
        gender = com.Gender(gender_name)
        try:
            person = com.Person(
                name=member_name, age=member_age, gender=gender)
            self.family.parent_add(person=person)
        except AssertionError as error:
            self.__error_label__ = tk.Label(master=self.__static_frame__,
                                            text=error.args)
            self.__error_label__.grid(row=1, column=6)

    def create_family_child(self):
        member_name = self.__new_family_child_entry__.get()
        member_age = self.__new_family_child_age_entry__.get()
        try:
            member_age = int(member_age)
        except ValueError:
            self.__error_label__ = tk.Label(
                master=self.__static_frame__, text='{invalid age}')
            self.__error_label__.grid(row=2, column=6)
            return
        if not hasattr(self, '__error_label__'):
            pass
        elif self.__error_label__ is not None:
            self.__error_label__.destroy()
        gender_name = self.new_child_gender_var.get()
        gender = com.Gender(gender_name)        #
        try:
            person = com.Person(name=member_name, age=member_age, gender=gender)
            self.family.child_add(person=person)
        except AssertionError as error:
            self.__error_label__ = tk.Label(master=self.__static_frame__,
                                            text=error.args)
            self.__error_label__.grid(row=2, column=6)

    def __family_detail__(self):
        # start by deleting any previous content
        if not hasattr(self, '__family_frame__'):
            self.__family_frame__ = None
        elif self.__family_frame__ is not None:
            self.__family_frame__.destroy()
        #
        # now draw the content from scratch
        self.__family_frame__ = tk.Frame(master=self.frame, highlightbackground='black', highlightthickness=1)
        self.__family_frame__.grid(row=0, column=0, sticky='N', padx=(
            5, 2.5), pady=2.5, ipadx=2.5, ipady=2.5)
        #
        self.__family_detail_static__()
        self.__family_detail_dynamic__()

    def __family_detail_dynamic__(self):
        self.__family_title_set__()
        #
        if self.family is None:
            return
        #
        if not hasattr(self, '__dynamic_frame__'):
            self.__dynamic_frame__ = None
        elif self.__dynamic_frame__ is not None:
            self.__dynamic_frame__.destroy()
        self.__dynamic_frame__ = tk.Frame(master=self.__family_frame__)
        self.__dynamic_frame__.grid(row=2, column=0, sticky='NW')
        #
        row = 0
        for parent in self.family.parents:
            self.__parent_row__(parent=parent, row=row)
            row += 1
        for child in self.family.children:
            self.__child_row__(child=child, row=row)
            row += 1

    def __parent_row__(self, parent: com.Person, row: int):
        assert isinstance(parent, com.Person), 'invalid person'
        assert isinstance(row, int), 'row must be an int'
        #
        tk.Button(master=self.__dynamic_frame__,
                  text='X',
                  command=lambda: self.family.parent_remove(person=parent),
                  highlightbackground='red').grid(row=row, column=0, sticky='NW')
        #
        text = 'P: ' + str(parent.id) + ': ' + parent.name
        highlightbackground = 'purple' if parent.id == self.selected_person_id else 'black'
        tk.Button(master=self.__dynamic_frame__,
                  text=text,
                  command=lambda: self.__select_person__(parent),
                  highlightbackground=highlightbackground).grid(row=row, column=1, sticky='NW')

    def __select_person__(self, person):
        assert isinstance(person, com.Person), 'invalid person'
        self.select_person_id(id=person.id)
        # this is to re-display the rows with the correct button colors
        self.__family_detail__()

    def __child_row__(self, child: com.Person, row: int):
        assert isinstance(child, com.Person), 'invalid person'
        assert isinstance(row, int), 'row must be an int'
        tk.Button(master=self.__dynamic_frame__,
                  text='X',
                  command=lambda: self.family.child_remove(person=child),
                  highlightbackground='red').grid(row=row, column=0, sticky='NW')
        #
        text = 'C: ' + str(child.id) + ': ' + child.name
        highlightbackground = 'purple' if child.id == self.selected_person_id else 'black'
        tk.Button(master=self.__dynamic_frame__,
                  text=text,
                  command=lambda: self.__select_person__(child),
                  highlightbackground=highlightbackground).grid(row=row, column=1, sticky='NW')

    def __person_detail__(self):
        if not hasattr(self, '__person_frame__'):
            self.__person_frame__ = None
        elif self.__person_frame__ is not None:
            self.__person_frame__.destroy()
        #
        self.__person_frame__ = tk.Frame(master=self.frame)
        self.__person_frame__.grid(row=0, column=5, sticky='N')
        #
        if self.selected_person is not None:
            self.selected_person.set_notify_container(self.__family_detail__)
        PersonGui(person=self.selected_person, frame=self.__person_frame__)

    def __family_title_set__(self):
        if self.family is None:
            return
        member_count = self.family.population
        members = ' member' if member_count == 1 else ' members'
        label_text = self.family.name + ' family: ' + str(member_count) + members
        tk.Label(master=self.__family_frame__,
                 text=label_text).grid(row=0, column=0)

    def __family_detail_static__(self):
        #
        if self.family is None:
            return
        #
        if not hasattr(self, '__static_frame__'):
            self.__static_frame__ = None
        elif self.__static_frame__ is not None:
            self.__static_frame__.destroy()
        self.__static_frame__ = tk.Frame(master=self.__family_frame__)
        self.__static_frame__.grid(row=1, column=0, sticky='NW')
        #
        # parent section
        #
        column: int = 0
        row: int = 0
        #
        tk.Button(master=self.__static_frame__,
                  text='Rename to',
                  highlightbackground='blue',
                  command=lambda: self.rename_family()
                  ).grid(row=row, column=column, sticky='NW')
        column += 1
        tk.Label(master=self.__static_frame__, text='').grid(
            row=row, column=column)
        column += 1
        self.__name_entry__ = tk.Entry(master=self.__static_frame__, width=10)
        self.__name_entry__.grid(row=row, column=column)
        column = 0
        row += 1
        tk.Button(master=self.__static_frame__,
                  text='New Parent',
                  command=lambda: self.create_family_parent(),
                  highlightbackground='blue').grid(row=row, column=column, sticky='NW')
        column += 1
        #
        tk.Label(master=self.__static_frame__, text='Parent: ').grid(
            row=row, column=column, sticky='E')
        column += 1
        self.__new_family_parent_entry__ = tk.Entry(
            master=self.__static_frame__,
            width=10)
        self.__new_family_parent_entry__.grid(row=row, column=column)
        column += 1
        #
        tk.Label(master=self.__static_frame__, text='Age: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_parent_age_entry__ = tk.Entry(
            master=self.__static_frame__, width=5)
        self.__new_family_parent_age_entry__.grid(row=row, column=column)
        column += 1
        #
        gender_values = [gender.value for gender in com.Gender]
        self.new_parent_gender_var = tk.StringVar(
            master=self.__static_frame__, value=com.Gender.undisclosed.value)
        parent_gender_menu = tk.OptionMenu(
            self.__static_frame__, self.new_parent_gender_var, *gender_values)
        parent_gender_menu.config(width=20, bg='black')
        parent_gender_menu.grid(row=row, column=column)
        #
        # child section
        #
        column = 0
        row += 1

        tk.Button(master=self.__static_frame__,
                  text='New Child',
                  command=lambda: self.create_family_child(),
                  highlightbackground='blue').grid(
            row=row, column=column, sticky='NW')
        column += 1
        tk.Label(master=self.__static_frame__, text='Child: ').grid(
            row=row, column=column, sticky='E')
        column += 1
        self.__new_family_child_entry__ = tk.Entry(
            master=self.__static_frame__,
            width=10)
        self.__new_family_child_entry__.grid(row=row, column=column)
        column += 1
        tk.Label(master=self.__static_frame__, text='Age: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_child_age_entry__ = tk.Entry(
            master=self.__static_frame__, width=5)
        self.__new_family_child_age_entry__.grid(row=row, column=column)
        column += 1
        self.new_child_gender_var = tk.StringVar(
            master=self.__static_frame__, value=com.Gender.undisclosed.value)
        child_gender_menu = tk.OptionMenu(
            self.__static_frame__, self.new_child_gender_var, *gender_values)
        child_gender_menu.config(width=20, bg='black')
        child_gender_menu.grid(row=row, column=column)

    def rename_family(self):
        new_name = self.__name_entry__.get()
        try:
            self.family.name = new_name
        except AssertionError as error:
            tk.Label(master=self.__static_frame__,
                     text=error.args).grid(row=0, column=3)
