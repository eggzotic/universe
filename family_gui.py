import tkinter as tk
import universe as com
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

    def __family_detail__(self):
        # start by deleting any previous content
        if not hasattr(self, '__family_frame__'):
            self.__family_frame__ = None
        elif self.__family_frame__ is not None:
            self.__family_frame__.destroy()
        #
        # now draw the content from scratch
        self.__family_frame__ = tk.Frame(master=self.frame)
        self.__family_frame__.grid(row=0, column=0, sticky='N')
        #
        self.__family_detail_static__()
        self.__family_detail_dynamic__()

    def __family_detail_dynamic__(self):
        self.__family_title_set__()
        #
        if self.family is None:
            return
        row = 3
        for parent in self.family.parents:
            self.__parent_row__(family=self.family, parent=parent, row=row)
            row += 1
        for child in self.family.children:
            self.__child_row__(family=self.family, child=child, row=row)
            row += 1

    def __parent_row__(self, family: com.Family, parent: com.Person, row: int):
        tk.Button(master=self.__family_frame__,
                  text='X',
                  command=lambda: family.parent_remove(person=parent),
                  highlightbackground='red').grid(row=row, column=0)
        #
        tk.Button(master=self.__family_frame__,
                  text='P: ' + str(parent.id) + ': ' + parent.name,
                  command=lambda: print(
                      family.name, 'detail requested:', parent.name),
                  highlightbackground='black').grid(row=row, column=1)

    def __child_row__(self, family: com.Family, child: com.Person, row: int):
        tk.Button(master=self.__family_frame__,
                  text='X',
                  command=lambda: family.child_remove(person=child),
                  highlightbackground='red').grid(row=row, column=0)
        #
        tk.Button(master=self.__family_frame__,
                  text='C: ' + str(child.id) + ': ' + child.name,
                  command=lambda: print(
                      family.name, 'detail requested:', child.name),
                  highlightbackground='black').grid(row=row, column=1)

    def __family_title_set__(self):
        if self.family is None:
            return
        member_count = self.family.population
        members = ' member' if member_count == 1 else ' members'
        label_text = self.family.name + ': ' + str(member_count) + members
        tk.Label(master=self.__family_frame__,
                 text=label_text).grid(row=0, column=0)

    def __family_detail_static__(self):
        #
        if self.family is None:
            return
        #
        column: int = 0
        row = 1

        tk.Button(master=self.__family_frame__,
                  text='New Parent',
                  command=lambda: self.create_family_parent(self.family),
                  highlightbackground='blue').grid(row=row, column=column)
        column += 1
        #
        tk.Label(master=self.__family_frame__, text='Parent: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_parent_entry__ = tk.Entry(
            master=self.__family_frame__,
            width=10)
        self.__new_family_parent_entry__.grid(row=row, column=column)
        column += 1
        #
        tk.Label(master=self.__family_frame__, text='Age: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_parent_age_entry__ = tk.Entry(
            master=self.__family_frame__, width=5)
        self.__new_family_parent_age_entry__.grid(row=row, column=column)
        column += 1
        #
        column = 0
        row = 2

        tk.Button(master=self.__family_frame__,
                  text='New Child',
                  command=lambda: self.create_family_child(
                      self.family),
                  highlightbackground='blue').grid(
            row=row, column=column)
        column += 1
        tk.Label(master=self.__family_frame__, text='Child: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_child_entry__ = tk.Entry(
            master=self.__family_frame__,
            width=10)
        self.__new_family_child_entry__.grid(row=row, column=column)
        column += 1
        tk.Label(master=self.__family_frame__, text='Age: ').grid(
            row=row, column=column)
        column += 1
        self.__new_family_child_age_entry__ = tk.Entry(
            master=self.__family_frame__, width=5)
        self.__new_family_child_age_entry__.grid(row=row, column=column)
        column += 1
