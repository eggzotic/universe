#
import datetime
from typing import List, Set
from enum import Enum


class Gender(Enum):
    """
    Gender enum - values representing the possible gender-states
    """
    male: str = 'male'
    female: str = 'female'
    undisclosed: str = 'undisclosed gender'


class Emotion(Enum):
    """
    Emotions enum - each representing something we can feel
    """
    happy: str = 'happy'
    sad: str = 'sad'
    anger: str = 'anger'
    love: str = 'love'
    hate: str = 'hate'
    frustration: str = 'frustration'
    bitterness: str = 'bitterness'
    peace: str = 'peace'
    wonder: str = 'wonder'
    amazed: str = 'amazed'
    confused: str = 'confused'
    thrilled: str = 'thrilled'
    devastated: str = 'devastated'
    jubilent: str = 'jubilent'
    stunned: str = 'stunned'
    frightened: str = 'frightened'
    brave: str = 'brave'


class Action(Enum):
    """
    Actions enum - each representing something we can do or that happens to us
    """
    changed_hair_color: str = 'changed hair color to'
    became_a_pet: str = 'became a pet'
    returned_to_wild: str = 'returned to wild'
    died: str = 'died'
    changed_gender: str = 'changed gender to'
    killed: str = 'killed'
    got_injured: str = 'suffered injury'
    healed_from_injury: str = 'healed from injury'
    fell_down: str = 'fell down'
    got_shot: str = 'got shot'
    contracted_illness: str = 'contracted illness'
    recovered_from_illness: str = 'recovered from illness'
    walked: str = 'walked'
    ran: str = 'ran'
    washed: str = 'washed'
    was_in_mud: str = 'was in mud'
    dried: str = 'dried off'
    got_tired: str = 'got tired'
    rested: str = 'rested'
    spoke: str = 'said:'
    got_warm: str = 'got warm'
    got_cold: str = 'got cold'
    sweated: str = 'sweated'
    cooled: str = 'cooled down, stopped sweating'
    was_adopted: str = 'was adopted'
    was_born: str = 'was born'
    removed_from_family: str = 'was removed from family'
    became_parent: str = 'became parent in family'
    removed_as_parent: str = 'was removed as a parent in family'
    child_added_to_family: str = 'was added to family'
    touched: str = 'touched'
    touched_by: str = 'was touched by'


class Animal:
    """
    Animal class - parent class for all animals
    """

    def __init__(self, age: int = None, dob: datetime.datetime = None, gender: Gender = Gender.undisclosed, type: str = 'Animal', name: str = None, eye_color: str = 'blue', hair_color: str = None, is_healer: bool = False):
        # specify age *or* date-of-birth (but not both) or neither
        assert age is None or dob is None
        # dob must be a datetime, if present
        assert dob is None or isinstance(dob, datetime.datetime)
        # age must be a positive-int, if present
        assert age is None or (isinstance(age, int) and age >= 0)
        #
        assert name is None or (isinstance(name, str) and name != '')
        #
        self.__breathes__: bool = True
        self.__is_wild__: bool = True
        self.__gender__: Gender = gender
        self.__leg_count__: int = 0
        self.__has_tail__: bool = False
        self.__is_fluffy__: bool = False
        self.__wags_tail__: bool = False
        self.__has_scales__: bool = False
        self.__has_gills__: bool = False
        self.__is_mammal__: bool = False
        self.__animal_type__ = type
        self.__has_paws__: bool = False
        self.__has_feathers__: bool = False
        self.__can_fly__: bool = False
        self.__makes_sound__: str = 'silence'
        self.__can_lay_eggs__: bool = False
        self.__given_name__: str = name
        self.__family_id__: int = None
        self.__has_hair__: bool = False
        self.__can_change_hair_color__: bool = False
        self.__hair_color__: str = hair_color
        self.__eye_color__: str = eye_color
        self.__is_injured__: bool = False
        self.__injury__: str = None
        self.__is_ill__: bool = False
        self.__illness__: str = None
        self.__distance_travelled__: float = 0.0
        self.__action_history__: List[(Action, *str)] = []
        self.__is_clean__: bool = True
        self.__is_wet__: bool = False
        self.__is_tired__: bool = False
        self.__distance_units__: str = 'km'
        self.__walking_tiredness_distance__: float = 5.0
        self.__running_tiredness_distance__: float = 1.0
        self.__is_cold__: bool = False
        self.__is_sweating__: bool = False
        self.__emotions__: Set[Emotion] = set()
        self.__has_healing_touch__: bool = is_healer

        #
        if dob != None:
            self.__dob__ = dob
        elif isinstance(age, int) and age >= 0:
            now = datetime.datetime.now()
            birth_year: int = now.year - age
            self.__dob__: datetime.datetime = datetime.datetime(
                year=birth_year, month=now.month, day=now.day, hour=now.hour, minute=now.minute)
        else:
            self.__dob__ = None
            print(self.name or self.animal_type,
                  'created without date-of-birth')
    #
    @property
    def name(self) -> str: return self.__given_name__
    @name.setter
    def name(self, name: str):
        assert name is not None and isinstance(name, str)
        self.__given_name__ = name

    @property
    def is_alive(self) -> bool: return self.__breathes__

    def dies(self):
        # resurrection not supported - death is final!
        self.__breathes__ = False
        self.add_action(Action.died)

    @property
    def is_wild(self) -> bool: return self.__is_wild__
    @property
    def is_tame(self) -> bool: return not self.is_wild
    @property
    def gender(self) -> Gender: return self.__gender__
    # gender-change is a thing, after all
    @gender.setter
    def gender(self, gender: Gender):
        assert gender is not None and isinstance(gender, Gender)
        self.__gender__ = gender
        self.add_action(Action.changed_gender, gender.value)

    @property
    def leg_count(self) -> int: return self.__leg_count__
    @property
    def has_tail(self) -> bool: return self.__has_tail__
    @property
    def is_fluffy(self) -> bool: return self.__is_fluffy__
    @property
    def wags_tail(self) -> bool: return self.__wags_tail__
    @property
    def has_scales(self) -> bool: return self.__has_scales__
    @property
    def has_gills(self) -> bool: return self.__has_gills__
    @property
    def is_mammal(self) -> bool: return self.__is_mammal__
    @property
    def animal_type(self) -> str: return self.__animal_type__
    @property
    def dob(self) -> datetime.datetime: return self.__dob__
    @property
    def age(self) -> int:
        if self.dob is None:
            print(self.name or self.__animal_type__,
                  'has no recorded date-of-birth - cannot get age')
            return None
        now = datetime.datetime.now()
        years_diff = now.year - self.dob.year
        if now.month < self.dob.month or now.day < self.dob.day:
            return years_diff - 1
        return years_diff

    @property
    def has_paws(self) -> bool: return self.__has_paws__
    @property
    def makes_sound(self) -> str: return self.__makes_sound__
    @property
    def has_feathers(self) -> bool: return self.__has_feathers__
    @property
    def can_fly(self) -> bool: return self.__can_fly__
    @property
    def can_lay_eggs(self) -> bool: return self.__can_lay_eggs__
    @property
    def is_pet(self) -> bool:
        return (not isinstance(self, Person)
                and self.is_tame
                and self.name is not None
                and self.name != ''
                and self.family_id is not None
                and isinstance(self.family_id, int))
    # the family this animal belongs to (as a child, not parent)
    @property
    def family_id(self) -> int: return self.__family_id__
    #
    @property
    def has_hair(self) -> bool: return self.__has_hair__
    @property
    def can_change_hair_color(
        self) -> bool: return self.__can_change_hair_color__

    @property
    def hair_color(self) -> str: return self.__hair_color__
    @hair_color.setter
    def hair_color(self, new_color: str):
        if not self.can_change_hair_color:
            print(self.name or self.animal_type,
                  'cannot change their hair color')
            return
        assert new_color is not None and isinstance(new_color, str)
        self.__hair_color__ = new_color
        self.add_action(Action.changed_hair_color, new_color)

    @property
    def eye_color(self) -> str: return self.__eye_color__

    # this should not really be a public method - should only be called from the
    #  Family.pet_add() etc. methods - to ensure a valid family_id is passed
    def make_pet(self, family_id: int, name: str = None):
        if isinstance(self, Person):
            print(self.name or self.animal_type,
                  'cannot me made a pet - slavery not supported')
            return
        if self.is_pet:
            print(self.animal_type, 'is already a pet called',
                  self.name, 'so cannot make a pet')
            return
        assert ((name is not None and isinstance(name, str) and name != '')
                or
                (self.name is not None and isinstance(self.name, str) and self.name != ''))
        assert family_id is not None and isinstance(family_id, int)
        #
        self.__is_wild__ = False
        if name is not None:
            self.name = name
        self.__family_id__ = family_id
        self.add_action(Action.became_a_pet)

    def return_to_wild(self):
        if isinstance(self, Person):
            print(self.animal_type, 'cannot be a pet anyway')
            return
        if not self.is_pet:
            print(self.animal_type, 'is not a pet anyway')
            return
        self.__family_id__ = None
        self.__is_wild__ = True
        self.add_action(Action.returned_to_wild)

    def kills(self, victim):
        assert victim is not None and isinstance(victim, Animal)
        if not self.is_alive:
            print(self.name, 'kills: the dead cannot kill')
            return
        # victim can be ourself - i.e. suicide
        if self is victim:
            print(self.name or self.animal_type, 'commits suicide')
        elif isinstance(self, Person):
            if isinstance(victim, Person):
                print(self.name, 'murders', victim.name)
                self.__is_criminal__ = True
            else:
                print(self.name, 'kills animal',
                      victim.name or victim.animal_type)
        else:
            print(self.name or self.animal_type, 'kills',
                  victim.name or victim.animal_type)
        victim.dies()
        self.add_action(Action.killed,
                        (victim.name or victim.animal_type))

    @property
    def is_injured(self) -> bool: return self.__is_injured__
    @property
    def injury(self) -> str: return self.__injury__

    def heals_from_injury(self):
        self.__injury__ = None
        self.__is_injured__ = False
        self.add_action(Action.healed_from_injury)

    def gets_injured(self):
        self.__is_injured__ = True
        self.add_action(Action.got_injured)

    def falls_down(self):
        self.gets_injured()
        self.__injury__ = 'bruising from Fall'
        self.__is_clean__ = False
        self.add_action(Action.fell_down)

    def gets_shot(self):
        self.gets_injured()
        self.__injury__ = 'gunshot wounds'
        self.add_action(Action.got_shot)

    @property
    def is_ill(self) -> bool: return self.__is_ill__
    @property
    def illness(self) -> str: return self.__illness__
    def gets_ill(self): self.__is_ill__ = True

    def contracted_illness(self, illness: str):
        assert illness is not None and isinstance(illness, str)
        self.gets_ill()
        self.__illness__ = illness
        self.add_action(Action.contracted_illness, illness)

    def recovers_from_illness(self):
        self.__illness__ = None
        self.__is_ill__ = False
        self.add_action(Action.recovered_from_illness)

    @property
    def distance_travelled(self) -> int: return self.__distance_travelled__

    def travelled(self, distance: float):
        assert distance is not None and isinstance(
            distance, (int, float)) and distance >= 0
        distance *= 1.0
        self.__distance_travelled__ += distance

    @property
    def last_action(self) -> str:
        if len(self.__action_history__) > 0:
            return self.__action_history__[-1]
        return None

    @property
    def all_actions(self) -> List[str]:
        return self.__action_history__

    def add_action(self, action: Action, *strings):
        assert action is not None and isinstance(action, Action)
        for s in strings:
            assert isinstance(s, str)
        self.__action_history__.append((action, *strings))

    def walks(self, distance: float):
        assert distance is not None and isinstance(distance, (int, float))
        self.travelled(distance)
        if distance >= self.__walking_tiredness_distance__:
            self.__is_tired__ = True
        self.add_action(Action.walked, str(distance) +
                        ' ' + self.__distance_units__)

    def runs(self, distance: float):
        assert distance is not None and isinstance(distance, (int, float))
        self.travelled(distance)
        self.add_action(Action.ran, str(distance) +
                        ' ' + self.__distance_units__)
        if distance >= self.__running_tiredness_distance__:
            self.gets_warm()
            self.sweats()
            self.gets_tired()

    @property
    def is_clean(self) -> bool: return self.__is_clean__

    def washes(self):
        self.__is_clean__ = True
        self.__is_wet__ = True
        self.add_action(Action.washed)

    def went_in_mud(self):
        self.__is_clean__ = False
        self.add_action(Action.was_in_mud)

    @property
    def is_wet(self) -> bool: return self.__is_wet__

    def drys(self):
        self.__is_wet__ = False
        self.add_action(Action.dried)

    @property
    def is_tired(self) -> bool: return self.__is_tired__

    def gets_tired(self):
        self.__is_tired__ = True
        self.add_action(Action.got_tired)

    def rests(self):
        self.__is_tired__ = False
        self.add_action(Action.rested)
        if self.is_sweating:
            self.cools_down()

    def says(self, words: str):
        assert words is not None and isinstance(words, str)
        self.add_action(Action.spoke, words)

    @property
    def is_cold(self) -> bool: return self.__is_cold__

    def gets_warm(self):
        self.__is_cold__ = False
        self.add_action(Action.got_warm)

    def gets_cold(self):
        self.__is_cold__ = True
        self.add_action(Action.got_cold)

    @property
    def is_sweating(self) -> bool: return self.__is_sweating__

    def sweats(self):
        self.__is_sweating__ = True
        self.add_action(Action.sweated)

    def cools_down(self):
        self.__is_sweating__ = False
        self.add_action(Action.cooled)

    @property
    def emotions(self) -> Set[Emotion]:
        return self.__emotions__

    def add_emotion(self, emotion: Emotion):
        assert emotion is not None and isinstance(emotion, Emotion)
        self.__emotions__.add(emotion)

    @property
    def has_healing_touch(self) -> bool: return self.__has_healing_touch__

    def touches(self, other: 'Animal'):
        assert other is not None and isinstance(other, Animal)
        self.add_action(Action.touched, other.name or other.animal_type)
        other.add_action(Action.touched_by, self.name or self.animal_type)
        if self.has_healing_touch:
            if other.is_injured:
                other.heals_from_injury()
            if other.is_ill:
                other.recovers_from_illness()


class Bird(Animal):
    """
    Bird class - for all our feathered friends
    """

    def __init__(self, can_fly: bool = True, *args, **kwargs):
        assert can_fly is not None and isinstance(can_fly, bool)
        #
        super().__init__(*args, type='Bird', **kwargs)
        # overrides - bird-specific attributes
        self.__has_tail__ = True
        self.__has_feathers__ = True
        self.__can_fly__ = can_fly
        self.__can_lay_eggs__ = True


class Fish(Animal):
    """
    Fish class - for all our swimming, swishy friends
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, type='Fish', **kwargs)
        # overrides - fish-specific attributes
        self.__has_scales__: bool = True
        self.__has_tail__ = True
        self.__has_gills__: bool = True


class Mammal(Animal):
    """
    Mammal class - parent class for all mammals
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # overrides - mammal-specific attributes
        self.__is_mammal__: bool = True
        self.__type__: str = 'Mammal'


class Cat(Mammal):
    """
    Cat class - for all our furry friends
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, type='Cat', **kwargs)
        # overrides - cat-specific attributes
        self.__leg_count__ = 4
        self.__has_tail__ = True
        self.__is_fluffy__ = True
        self.__has_paws__ = True
        self.__makes_sound__: str = 'meow'
        self.__has_hair__: bool = True


class Dog(Mammal):
    """
    Dog class - for our best friends
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, type='Dog', **kwargs)
        # overrides - dog-specific attributes
        self.__leg_count__ = 4
        self.__has_tail__ = True
        self.__wags_tail__: bool = True
        self.__has_paws__: bool = True
        self.__makes_sound__: str = 'woof'
        self.__has_hair__: bool = True


class Person(Mammal):
    """
    Person class - for us (people)
    """
    __person_id__: int = 0

    @classmethod
    def next_person_id(cls) -> int:
        cls.__person_id__ += 1
        return cls.__person_id__

    def __init__(self, name: str, age: int = None, dob: datetime.datetime = None, *args, **kwargs):
        # person must have a name
        assert name is not None and (isinstance(name, str) and name != '')
        # specify age *or* date-of-birth, but not both
        assert age is None or dob is None
        assert age is not None or dob is not None
        #
        super().__init__(age=age, dob=dob, type='Person', name=name, *args, **kwargs)
        # overrides - human-specific attributes
        self.__is_wild__: bool = False
        self.__makes_sound__ = 'bla bla bla'
        self.__leg_count__ = 2
        self.__is_wild__ = False
        self.__is_criminal__ = False
        self.__is_forgiven__ = False

        self.__person_id__ = Person.next_person_id()
        self.__parent_of_families_id__: Set[int] = set()
        self.__has_hair__: bool = True
        self.__can_change_hair_color__: bool = True
        if self.__hair_color__ is None:
            self.__hair_color__ = 'brunette'

    @property
    def id(self) -> int: return self.__person_id__

    # the families this person is a parent of
    @property
    def parent_of_families_id(self) -> Set[int]:
        return self.__parent_of_families_id__

    @property
    def is_criminal(self) -> bool: return self.__is_criminal__

    @property
    def is_forgiven(self) -> bool: return self.__is_forgiven__

    def forgives(self, sinner: 'Person'):
        assert sinner is not None and isinstance(sinner, Person)
        if not self.is_alive:
            print(self.name, 'forgives: the dead cannot forgive')
            return
        #
        sinner.__is_forgiven__ = True

    def is_sibling_of(self, other: 'Person') -> bool:
        return other.family_id == self.family_id

    def is_brother_of(self, other: 'Person') -> bool:
        return self.is_sibling_of(other) and self.gender == Gender.male

    def is_sister_of(self, other: 'Person') -> bool:
        return self.is_sibling_of(other) and self.gender == Gender.female


class Family:
    __family_id__: int = 0

    @classmethod
    def __next_id__(cls) -> int:
        cls.__family_id__ += 1
        return cls.__family_id__

    def __init__(self, name: str, members_updated_callback=None):
        # name must be a non-empty string
        assert name is not None, 'name required'
        assert isinstance(name, str), 'name must be a string'
        name = name.strip()
        assert name != '', 'name cannot be blank'
        #
        self.__family_id__ = Family.__next_id__()
        # the community ID this person currently belongs to
        self.__community_id__: int = None
        #
        self.__family_name__ = name
        self.__parents__: List[Person] = list()
        self.__children__: List[Person] = list()
        self.__pets__: List[Animal] = list()
        print(name, 'family created')
        self.__members_updated_callback__ = members_updated_callback

    @property
    def id(self) -> int: return self.__family_id__

    # the community of which this person is a member
    @property
    def community_id(self) -> int: return self.__community_id__
    @property
    def member_ids(self) -> Set[int]:
        return set([person.id for person in self.members])

    @property
    def member_names(self) -> List[str]:
        return [p.name for p in self.members]

    @property
    def name(self) -> str: return self.__family_name__
    @name.setter
    def name(self, new_name: str):
        assert new_name is not None and isinstance(new_name, str)
        self.__family_name__ = new_name

    @property
    def parents(self) -> List[Person]: return self.__parents__
    @property
    def children(self) -> List[Person]: return self.__children__
    @property
    def pets(self) -> List[Animal]: return self.__pets__

    @property
    def members(self) -> List[Person]: return set(self.children + self.parents)

    @property
    def population(self) -> int:
        # note that since a person can be a parent across multiple families,
        #  it's not safe to add the populations of families (you may be double-counting!)
        return len(self.members)

    @property
    def alive_parents(self) -> List[Person]:
        return [parent for parent in self.parents if parent.is_alive]

    def gives_birth(self, name: str, gender: Gender = Gender.undisclosed):
        assert name is not None and isinstance(name, str)
        #
        baby = Person(name=name, dob=datetime.datetime.now())
        baby.add_action(Action.was_born)
        self.child_add(person=baby)

    def adopts_child(self, person: Person):
        assert person is not None and isinstance(person, Person)
        #
        person.add_action(Action.was_adopted)
        self.child_add(person)

    @property
    def child_names(self) -> List[str]:
        return [child.name for child in self.children]

    @property
    def child_ages(self) -> List[int]:
        return [child.age for child in self.children]

    @property
    def parent_names(self) -> List[str]:
        return [parent.name for parent in self.parents]

    @property
    def parent_ages(self) -> List[int]:
        return [parent.age for parent in self.parents]

    def has_parent(self, person: Person) -> bool:
        assert person is not None and isinstance(person, Person)
        #
        return person in self.parents

    def has_child(self, person: Person) -> bool:
        assert person is not None and isinstance(person, Person)
        return person in self.children

    def has_pet(self, pet: Animal) -> bool:
        assert pet is not None and isinstance(pet, Animal)
        if pet.is_pet:
            return pet in self.pets
        return False

    def pet_add(self, pet: Animal, name: str = None):
        """
        add a pet to this family
        """
        assert pet is not None and isinstance(pet, Animal)
        # cannot add a pet if already a pet
        if self.has_pet(pet):
            print(self.name, 'family: already has pet',
                  pet.name, '- cannot add again')
            return
        #
        if isinstance(pet, Person):
            print(pet.name, 'is a person - cannot be a pet')
            return
        #
        if pet.family_id is not None:
            print(pet.name, 'already belongs to a family, cannot add to another')
            return
        #
        pet.make_pet(family_id=self.id, name=name)
        self.pets.append(pet)
        print(self.name, 'family: added pet', pet.name)

    def pet_remove(self, pet: Animal):
        """
        remove a pet from this family
        """
        assert pet is not None and isinstance(pet, Animal)
        if pet in self.pets:
            self.pets.remove(pet)
            pet.return_to_wild()
            print(self.name, 'family: removed pet', pet.name)
            return
        print(self.name, 'family: does not have pet',
              pet.name, '- cannot remove')

    def child_add(self, person: Person):
        """
        add a child to this family
        """
        assert person is not None and isinstance(person, Person)
        # cannot add as child if already a parent
        if self.has_parent(person):
            print(self.name, 'family: already has parent',
                  person.name, '- cannot add as a child')
            return
        # cannot add as child if already a child
        if self.has_child(person):
            print(self.name, 'family: already has child', person.name,
                  '- cannot add again')
            return
        # age must be less than parent ages
        for parent in self.parents:
            if person.dob <= parent.dob:
                print(self.name, 'family:', person.name, 'is older than (parent)',
                      parent.name, '- so cannot be their child')
                return

        # now can add as a child
        print(self.name, 'family: added child', person.name)
        self.children.append(person)
        person.__family_id__ = self.__family_id__
        person.add_action(Action.child_added_to_family, self.name)
        if self.__members_updated_callback__ is not None:
            self.__members_updated_callback__()

    def child_remove(self, person: Person):
        """
        remove a child from this family(!)
        """
        #
        assert person is not None and isinstance(person, Person)
        #
        if person in self.children:
            self.children.remove(person)
            person.__family_id__ = None
            person.add_action(Action.removed_from_family, self.name)
            print(self.name, 'family: removed child', person.name)
            if self.__members_updated_callback__ is not None:
                self.__members_updated_callback__()
            return
        print(self.name, 'family: does not have child',
              person.name, '- cannot remove')

    def parent_add(self, person: Person):
        """
        add a parent to this family
        """
        assert person is not None and isinstance(person, Person)
        # cannot add as parent if already a parent of this family
        if self.has_parent(person):
            print(self.name, 'family: already has parent',
                  person.name, '- cannot add again')
            return
        # cannot add as parent if already a child of this family
        if self.has_child(person):
            print(self.name, 'family: already has child', person.name,
                  '- cannot add as a parent')
            return
        # cannot have more than 2 alive parents
        if len(self.alive_parents) >= 2:
            print(self.name, 'family: already 2 alive parents - cannot add more')
            return
        # age of parent cannot be less than children
        for child in self.children:
            if person.dob > child.dob:
                print(self.name, 'family:', person.name, 'is younger than (child)',
                      child.name, '- cannot add as their parent')
                return
        # no gender-related restrictions on who can be parents(!)
        #
        # now can add the parent
        self.parents.append(person)
        person.__parent_of_families_id__.add(self.__family_id__)
        person.add_action(Action.became_parent, self.name)
        print(self.name, 'family: added parent', person.name)
        if self.__members_updated_callback__ is not None:
            self.__members_updated_callback__()

    def parent_remove(self, person: Person):
        """
        remove a parent from this family(!)
        """
        #
        assert person is not None and isinstance(person, Person)
        #
        if person in self.parents:
            self.parents.remove(person)
            person.__parent_of_families_id__.remove(self.__family_id__)
            person.add_action(Action.removed_as_parent, self.name)
            print(self.name, 'family: removed parent', person.name)
            if self.__members_updated_callback__ is not None:
                self.__members_updated_callback__()
            return
        print(self.name, 'family: does not have parent',
              person.name, '- cannot remove')


class Community:
    """
    Community class - container of families
    """
    #
    __community_id__: int = 0

    @classmethod
    def __next_id__(cls) -> int:
        cls.__community_id__ += 1
        return cls.__community_id__

    def __init__(self, name: str, families_updated_callback=None):
        assert name is not None, 'name required'
        assert isinstance(name, str), 'name must be a string'
        name = name.strip()
        assert name != '', 'name cannot be blank'
        #
        self.__community_id__ = Community.__next_id__()
        self.__community_name__ = name
        self.__world_id__: int = None
        self.__all_families__: List[Family] = []
        self.__families_updated_callback__ = families_updated_callback

    @property
    def id(self) -> int: return self.__community_id__
    @property
    def world_id(self) -> int: return self.__world_id__
    @property
    def name(self) -> str: return self.__community_name__
    @name.setter
    def name(self, new_name: str):
        assert new_name is not None and isinstance(
            new_name, str) and new_name != ''
        self.__community_name__ = new_name

    @property
    def all_families(self) -> List[Family]: return self.__all_families__
    @property
    def all_families_names(self) -> List[str]:
        return [f.name for f in self.all_families]

    def new_family(self, name: str, members_updated_callback=None):
        assert name is not None and isinstance(
            name, str) and name != '', 'name cannot be blank'
        fam = Family(
            name=name, members_updated_callback=members_updated_callback)
        self.family_add(fam)

    def family_add(self, family: Family):
        assert family is not None and isinstance(
            family, Family), 'name cannot be blank'
        #
        # cannot already be in this community
        if family.community_id == self.id:
            print(self.name, 'community: cannot add', family.name,
                  'family: already in this community')
            return
        # cannot belong to another community already
        if family.community_id is not None:
            print(self.name, 'community: cannot add', family.name,
                  'family: is in another community')
            return
        # so we're good to go
        self.all_families.append(family)
        family.__community_id__ = self.__community_id__
        print(self.name, 'community: added', family.name, 'family')
        if self.__families_updated_callback__ is not None:
            self.__families_updated_callback__()

    def family_remove(self, family: Family):
        assert family is not None and isinstance(family, Family)
        #
        if family in self.all_families:
            self.all_families.remove(family)
            family.__community_id__ = None
            print(self.name, 'community: removed', family.name, 'family')
            if self.__families_updated_callback__ is not None:
                self.__families_updated_callback__()
            return
        print(self.name, 'community: cannot remove',
              family.name, 'family: not in this community')

    @property
    def population(self) -> int:
        ids = set()
        for family in self.all_families:
            ids = ids.union(family.member_ids)
        return len(ids)

    def family_of(self, person_or_pet) -> Family:
        assert person_or_pet is not None and (isinstance(
            person_or_pet, Animal))
        family_id = None
        if not isinstance(person_or_pet, Person):
            family_id = person_or_pet.family_id
        elif isinstance(person_or_pet, Person):
            family_id = person_or_pet.family_id
            if family_id is None:
                # or maybe they're a parent in a family?
                family_ids = person_or_pet.parent_of_families_id
                if len(family_ids) > 0:
                    # just pick any family they're a parent of...
                    family_id = next(iter(family_ids))
        families = [fam for fam in self.all_families if fam.id == family_id]
        if len(families) > 0:
            return families[0]
        print(person_or_pet.name, 'has no family')
        return None

    def surname_of(self, person: Person) -> str:
        assert person is not None and isinstance(person, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'has no surname')
            return None
        return family.name

    def parents_of(self, person: Person) -> List[Person]:
        assert person is not None and isinstance(person, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'has no parents')
            return []
        return family.parents

    def parent_add(self, person: Person, parent: Person):
        """
        add parent as a parent in the family of person
        """
        #
        assert person is not None and isinstance(person, Person)
        assert parent is not None and isinstance(parent, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot add parent')
            return None
        family.parent_add(parent)

    def parent_remove(self, person: Person, parent: Person):
        """
        remove parent from the parents of the family of person
        """
        #
        assert person is not None and isinstance(person, Person)
        assert parent is not None and isinstance(parent, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot remove parent')
            return None
        family.parent_remove(parent)

    def father_of(self, person: Person) -> Person:
        assert person is not None and isinstance(person, Person)
        #
        parents = self.parents_of(person)
        if len(parents) == 0:
            print(person.name, 'has no father')
            return None
        for parent in parents:
            if parent.gender == Gender.male:
                return parent
        print(person.name, 'has no father')
        return None

    def mother_of(self, person: Person) -> Person:
        assert person is not None and isinstance(person, Person)
        #
        parents = self.parents_of(person)
        if len(parents) == 0:
            print(person.name, 'has no mother')
            return None
        for parent in parents:
            if parent.gender == Gender.female:
                return parent
        print(person.name, 'has no mother')
        return None

    def siblings_of(self, person: Person) -> List[Person]:
        assert person is not None and isinstance(person, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(self.name, 'family:', person.name, 'has no siblings')
            return []
        # so we have a family - but we could be either a child or parent
        # ensure we're a child-only
        if person not in family.children:
            print(family.name, 'family:', person.name, 'is not a child here')
            return []
        return [sibling for sibling in family.children if sibling is not person]

    def sibling_add(self, person: Person, sibling: Person):
        """
        add sibling as a child in the family of person
        """
        #
        assert person is not None and isinstance(person, Person)
        assert sibling is not None and isinstance(sibling, Person)
        #
        if person is sibling:
            print(person.name, 'cannot be added as a sibling of himself/herself')
            return
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot add sibling', sibling.name)
            return
        family.child_add(sibling)

    def sibling_remove(self, person: Person, sibling: Person):
        """
        remove sibling from the family of person
        """
        #
        assert person is not None and isinstance(person, Person)
        assert sibling is not None and isinstance(sibling, Person)
        #
        if person is sibling:
            print(person.name, 'cannot be removed as a sibling of himself/herself')
            return
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot remove sibling', sibling.name)
            return
        family.child_remove(sibling)

    def pet_add(self, person: Person, pet: Animal, name: str = None):
        """
        add pet into the family of person
        """
        #
        assert person is not None and isinstance(person, Person)
        assert pet is not None and isinstance(pet, Animal)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot add pet', pet.name)
            return
        family.pet_add(pet, name=name)

    def pets_of(self, person: Person) -> List[Animal]:
        """
        return all the pets of the family of person
        """
        assert person is not None and isinstance(person, Person)
        #
        family = self.family_of(person)
        if family is None:
            print(person.name, 'cannot find pets')
            return []
        return family.pets


class World:
    """
    World class - container of communities
    """
    #
    __world_id__: int = 0
    #
    @classmethod
    def __next_id__(cls) -> int:
        cls.__world_id__ += 1
        return cls.__world_id__

    def __init__(self, name: str, communities_updated_callback=None):
        assert name is not None and isinstance(name, str) and name != ''
        #
        self.__world_id__ = World.__next_id__()
        self.__world_name__ = name
        self.__all_communities__: List[Community] = []
        self.__communities_updated_callback__ = communities_updated_callback

    @property
    def id(self) -> int: return self.__world_id__
    @property
    def name(self) -> str: return self.__world_name__
    @name.setter
    def name(self, new_name: str):
        assert new_name is not None and isinstance(
            new_name, str) and new_name != ''
        self.__world_name__ = new_name

    @property
    def all_communities(self) -> List[Community]:
        return self.__all_communities__

    @property
    def all_communities_names(self) -> List[str]:
        return [c.name for c in self.all_communities]

    def new_community(self, name: str, families_updated_callback=None):
        assert name is not None and isinstance(name, str)
        #
        com = Community(
            name=name, families_updated_callback=families_updated_callback)
        self.community_add(com)

    def community_add(self, community: Community):
        assert community is not None and isinstance(community, Community)
        # cannot already be in this world
        if community.world_id == self.id:
            print(self.name, 'world: cannot add', community.name,
                  'community: already in this world')
            return
        # cannot belong to another world already
        if community.world_id is not None:
            print(self.name, 'world: cannot add', community.name,
                  'community: is in another world')
            return
        # so we're good to go
        self.all_communities.append(community)
        community.__world_id__ = self.__world_id__
        print(self.name, 'world: added', community.name, 'community')
        if self.__communities_updated_callback__ is not None:
            self.__communities_updated_callback__()

    def community_remove(self, community: Community):
        assert community is not None and isinstance(community, Community)
        #
        if community in self.all_communities:
            self.all_communities.remove(community)
            community.__world_id__ = None
            print(self.name, 'world: removed', community.name, 'community(!)')
            if self.__communities_updated_callback__ is not None:
                self.__communities_updated_callback__()
            return
        print(self.name, 'world: cannot remove',
              community.name, 'community: not in this world')

    def comm_id_of(self, family_id: int) -> int:
        assert family_id is not None and isinstance(family_id, int)
        #
        comms = [
            com for com in self.all_communities for fam in com.all_families if fam.id == family_id]
        if len(comms) > 0:
            return comms[0]
        return None

    def community_of(self, family_or_person_or_pet) -> Community:
        assert family_or_person_or_pet is not None and isinstance(
            family_or_person_or_pet, (Family, Animal))
        # community must be in this world
        family_id = None
        if isinstance(family_or_person_or_pet, Animal) and not isinstance(family_or_person_or_pet, Person):
            family_id = family_or_person_or_pet.family_id
        elif isinstance(family_or_person_or_pet, Person):
            # family_id, if this person is a child in a family
            family_id = family_or_person_or_pet.family_id
            if family_id is None:
                # or maybe they're a parent in a family?
                family_ids = family_or_person_or_pet.parent_of_families_id
                if len(family_ids) > 0:
                    # just pick any family they're a parent of...
                    family_id = next(iter(family_ids))
        elif isinstance(family_or_person_or_pet, Family):
            family_id = family_or_person_or_pet.id
        if family_id is None:
            print(self.name, 'world: cannot find family ID for person',
                  family_or_person_or_pet.name)
            return None
        com = self.comm_id_of(family_id)
        if com is None:
            print(self.name, 'world: community for person',
                  family_or_person_or_pet.name, 'is not in this world')
        return com

    def family_of(self, person_or_pet) -> Family:
        assert person_or_pet is not None and isinstance(
            person_or_pet, Animal)
        #
        comm = self.community_of(person_or_pet)
        if comm is None:
            return None
        # so we can hand-off this search to the community
        return comm.family_of(person_or_pet)

    @property
    def population(self) -> int:
        pop: int = 0
        for com in self.all_communities:
            pop += com.population
        return pop


if __name__ == "__main__":
    fish = Fish(dob=datetime.datetime(2016, 7, 24))
    fish_legs = fish.leg_count
    dog = Dog()
    dog_legs = dog.leg_count
    cat = Cat()
    bird = Bird()
    #
    bob = Person(name='Bobby', age=23)
    bill = Person(name='Bill', age=56)
    jane = Person(name='Jane', age=7, gender=Gender.female, is_healer=True)
    junior = Person(name='Junior', age=2, gender=Gender.male)
    ann = Person(name='Ann', age=38, gender=Gender.female)
    ed = Person(name='Ed', age=43)
    #
    pierre = Person(name='Pierre', age=41, hair_color='dark', eye_color='aqua')
    renee = Person(name='Renee', age=47)
    vera = Person(name='Vera', gender=Gender.female,
                  age=11, hair_color='blonde')
    duboir_family = Family(name='Duboir')
    duboir_family.parent_add(pierre)
    duboir_family.parent_add(renee)
    duboir_family.child_add(vera)
    #
    fluffy = Cat(name='Fluffy')
    rover = Dog(name='Rover')

    earth = World(name='Earth')
    earth.new_community(name='The English')
    the_english = earth.all_communities[0]
    the_english.new_family(name='Jones')
    jones_family = the_english.all_families[0]
    jones_family.parent_add(ann)
    jones_family.child_add(jane)
    jones_family.parent_add(junior)
    jones_family.child_add(ed)
    jones_family.parent_add(bill)
    jane_family = the_english.family_of(jane)
    the_english.sibling_add(jane, bob)
    the_english.pet_add(bob, fluffy)
    #
    the_french = Community(name='The French')
    the_french.family_add(duboir_family)
    earth.community_add(the_french)

    #
    the_english.new_family(name='Smith')
    smith_family = the_english.all_families[1]
    smith_family.parent_add(ed)
    smith_family.child_add(junior)
    #
    # com2 = Community(name='com2')

    print('Sibling Summary:')
    [print(person.name, 'is the sibling of', sibling.name)
     for person in (bob, bill, jane) for sibling in the_english.siblings_of(person)]
