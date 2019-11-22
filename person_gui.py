import tkinter as tk
import universe as com
from typing import List, Set, Dict


class PersonGui:
    def __init__(self, person: com.Person, frame: tk.Frame):
        assert person is None or isinstance(
            person, com.Person), 'either pass a valid person, or None'
        assert isinstance(frame, tk.Frame), 'invalid frame'
        #
        super().__init__()
        #
        self.__frame__ = frame
        self.__person__ = person
        if person is not None:
            person.set_property_updated_callback(self.__person_detail__)
        #
        self.__person_detail__()

    @property
    def frame(self): return self.__frame__

    @property
    def person(self): return self.__person__

    def rename_person(self):
        new_name = self.__name_entry__.get()
        try:
            self.person.name = new_name
        except AssertionError as error:
            tk.Label(master=self.__static_frame__, text=error.args)

    def __person_detail__(self):
        # start by deleting any previous content
        if not hasattr(self, '__person_frame__'):
            self.__person_frame__ = None
        elif self.__person_frame__ is not None:
            self.__person_frame__.destroy()
        #
        if self.person is None:
            return
        #
        # now draw the content from scratch
        self.__person_frame__ = tk.Frame(
            master=self.frame, highlightbackground='black', highlightthickness=1)
        self.__person_frame__.grid(row=0, column=0, sticky='N', padx=(
            5, 2.5), pady=2.5, ipadx=2.5, ipady=2.5)
        #
        self.__person_detail_static__()

    def __person_detail_static__(self):
        if not hasattr(self, '__static_frame__'):
            self.__static_frame__ = None
        elif self.__static_frame__ is not None:
            self.__static_frame__.destroy()
        self.__static_frame__ = tk.Frame(master=self.__person_frame__)
        self.__static_frame__.grid(row=1, column=0, sticky='NW')
        #
        row = 0
        self.__person_title__(row=row)
        # these all go in a separate frame, so don't increment row just yet
        self.__rename_to__(row=row)
        row += 1
        self.__alive_state__(row=row)
        row += 1
        self.__gender_state__(row=row)
        row += 1
        self.__hair_color_state__(row=row)
        row += 1
        self.__move_state__(row=row)
        row += 1
        self.__tiredness_state__(row=row)
        row += 1
        self.__dry_wet_state__(row=row)
        # row += 1
        row += 1
        self.__action_history_state__(row=row)
        row += 1

    def __person_title__(self, row: int):
        #
        text = self.person.name + ': ' + str(self.person.age) + ' years'
        tk.Label(master=self.__person_frame__,
                 text=text).grid(row=row, column=0)

    def __rename_to__(self, row: int):
        tk.Button(master=self.__static_frame__,
                  text='Rename to',
                  highlightbackground='blue',
                  command=lambda: self.rename_person()
                  ).grid(row=row, column=0, sticky='NW')
        self.__name_entry__ = tk.Entry(master=self.__static_frame__,
                                       width=10)
        self.__name_entry__.grid(row=row, column=1)

    def __alive_state__(self, row: int):
        alive = 'alive' if self.person.is_alive else 'dead'
        tk.Label(master=self.__static_frame__, text=self.person.name +
                 ' is ' + alive).grid(row=row, column=0, sticky='W')
        bg = 'red' if self.person.is_alive else 'gray'
        tk.Button(master=self.__static_frame__,
                  text='Kill ' + self.person.name,
                  highlightbackground=bg,
                  command=lambda: self.__kill_person__()).grid(row=row, column=1, sticky='W')

    def __kill_person__(self):
        if self.person.is_alive:
            self.person.dies()

    def __gender_state__(self, row: int):
        text = self.person.name + ' is ' + self.person.gender.value
        tk.Label(master=self.__static_frame__, text=text).grid(
            row=row, column=0, sticky='W')
        #
        tk.Button(master=self.__static_frame__,
                  text='Sex change',
                  highlightbackground='black',
                  command=lambda: self.__sex_change__(row)).grid(row=row, column=1, sticky='W')
        #
        gender_values = [gender.value for gender in com.Gender]
        self.__new_gender_var__ = tk.StringVar(
            master=self.__static_frame__, value=self.person.gender.value)
        gender_change_menu = tk.OptionMenu(
            self.__static_frame__, self.__new_gender_var__, *gender_values)
        gender_change_menu.config(width=20, bg='black')
        gender_change_menu.grid(row=row, column=2, sticky='W')

    def __sex_change__(self, row: int):
        if not hasattr(self, '__gender_change_error__'):
            self.__gender_change_error__ = None
        elif self.__gender_change_error__ is not None:
            self.__gender_change_error__.destroy()
        #
        gender_name = self.__new_gender_var__.get()
        new_gender = com.Gender(gender_name)
        try:
            self.person.gender = new_gender
        except AssertionError as error:
            self.__gender_change_error__ = tk.Label(
                master=self.__static_frame__, text=error.args)
            self.__gender_change_error__.grid(row=row, column=3, sticky='W')
            return

    def __hair_color_state__(self, row: int):
        text = self.person.name + ' has ' + self.person.hair_color.value + ' hair'
        tk.Label(master=self.__static_frame__, text=text).grid(
            row=row, column=0, sticky='W')
        #
        tk.Button(master=self.__static_frame__,
                  text='Dye hair',
                  highlightbackground='black',
                  command=lambda: self.__hair_color_change__(row)).grid(row=row, column=1, sticky='W')
        hair_color_values = [color.value for color in com.HairColor]
        self.__new_hair_color_var__ = tk.StringVar(
            master=self.__static_frame__, value=self.person.hair_color.value)
        hair_color_change_menu = tk.OptionMenu(
            self.__static_frame__, self.__new_hair_color_var__, *hair_color_values)
        hair_color_change_menu.config(width=10, bg='black')
        hair_color_change_menu.grid(row=row, column=2, sticky='W')

    def __hair_color_change__(self, row: int):
        if not hasattr(self, '__hair_color_change_error__'):
            self.__hair_color_change_error__ = None
        elif self.__hair_color_change_error__ is not None:
            self.__hair_color_change_error__.destroy()
        #
        hair_color_text = self.__new_hair_color_var__.get()
        hair_color = com.HairColor(hair_color_text)
        try:
            self.person.hair_color = hair_color
        except AssertionError as error:
            self.__hair_color_change_error__ = tk.Label(
                master=self.__static_frame__, text=error.args)
            self.__hair_color_change_error__.grid(
                row=row, column=3, sticky='W')
            return

    def __dry_wet_state__(self, row: int):
        state = 'wet' if self.person.is_wet else 'dry'
        text = self.person.name + ' is ' + state
        tk.Label(master=self.__static_frame__, text=text).grid(
            row=row, column=0, sticky='W')
        #
        tk.Button(master=self.__static_frame__,
                  text='Drys',
                  highlightbackground='black',
                  command=lambda: self.person.drys(),
                  ).grid(row=row,column=1,sticky='W')

    def __move_state__(self, row: int):
        distance = self.person.distance_travelled
        text = self.person.name + ' has travelled ' + \
            str(distance) + ' ' + self.person.__distance_units__
        tk.Label(master=self.__static_frame__, text=text).grid(
            row=row, column=0, sticky='W')
        #
        movement_values = [move.value for move in com.Movement]
        self.new_move_var = tk.StringVar(
            master=self.__static_frame__, value=com.Movement.walk.value)
        movement_menu = tk.OptionMenu(
            self.__static_frame__, self.new_move_var, *movement_values)
        movement_menu.config(width=10, bg='black')
        movement_menu.grid(row=row, column=2, sticky='W')
        tk.Button(master=self.__static_frame__,
                  text='Move!',
                  highlightbackground='black',
                  command=lambda: self.__travels__(row=row)).grid(row=row, column=1, sticky='W')
        self.__distance_to_move__ = tk.Entry(
            master=self.__static_frame__, width=5)
        self.__distance_to_move__.grid(row=row, column=3, sticky='W')
        tk.Label(master=self.__static_frame__, text=self.person.__distance_units__).grid(
            row=row, column=4, sticky='W')

    def __tiredness_state__(self, row: int):
        tired = 'tired' if self.person.is_tired else 'not tired'
        text = self.person.name + ' is ' + tired
        tk.Label(master=self.__static_frame__, text=text).grid(
            row=row, column=0, sticky='W')
        #
        tk.Button(master=self.__static_frame__,
                  text='Rests',
                  command=lambda: self.person.rests(),
                  highlightbackground='black',
                  ).grid(row=row, column=1, sticky='W')

    def __travels__(self, row: int):
        distance_text = self.__distance_to_move__.get()
        try:
            distance = float(distance_text)
        except ValueError:
            self.__distance_error__ = tk.Label(
                master=self.__static_frame__, text='{invalid number}')
            self.__distance_error__.grid(row=row, column=5, sticky='W')
            return
        if not hasattr(self, '__distance_error__'):
            self.__distance_error__ = None
        elif self.__distance_error__ is not None:
            self.__distance_error__.destroy()
        movement_text = self.new_move_var.get()
        movement = com.Movement(movement_text)
        try:
            if movement is com.Movement.crawl:
                self.person.crawls(distance=distance)
            elif movement is com.Movement.walk:
                self.person.walks(distance=distance)
            elif movement is com.Movement.run:
                self.person.runs(distance=distance)
        except AssertionError as error:
            self.__distance_error__ = tk.Label(
                master=self.__static_frame__, text=error.args)
            self.__distance_error__.grid(row=row, column=5, sticky='W')
            return

    def __action_history_state__(self, row: int):
        if not hasattr(self, '__action_history_frame__'):
            self.__action_history_frame__ = None
        elif self.__action_history_frame__ is not None:
            self.__action_history_frame__.destroy()
        self.__action_history_frame__ = tk.Frame(master=self.__static_frame__)
        self.__action_history_frame__.grid(
            row=row, column=0, columnspan=3, sticky='W')
        #
        arow = 0
        if len(self.person.all_actions) == 0:
            return
        tk.Label(master=self.__action_history_frame__,
                 text='Action History:').grid(row=arow, column=0, sticky='W')
        arow += 1
        for action in self.person.all_actions:
            pre_text = self.person.name + ' ' + action[0].value
            values = action[1:] if len(action) > 1 else ()
            post_text = ' '.join(values)
            text = pre_text + ' ' + post_text
            tk.Label(master=self.__action_history_frame__,
                     text=text).grid(row=arow, sticky='W', padx=5)
            arow += 1
