#
import datetime
from typing import List, Set
from enum import Enum
import pickle


class Gender(Enum):
    """
    Gender enum - values representing the possible gender-states
    """
    male: str = 'male'
    female: str = 'female'
    undisclosed: str = 'undisclosed gender'


class Movement(Enum):
    """
    Movements enum - crawl, walk, run, etc.
    """
    crawl: str = 'crawl'
    walk: str = 'walk'
    run: str = 'run'


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
    changed_name: str = 'changed name from'
    changed_hair_color: str = 'changed hair color from'
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
    crawled: str = 'crawled'
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


class HairColor(Enum):
    """
    Hair colors - possible hair colors for people
    """
    brunette: str = 'brunette'
    black: str = 'black'
    blonde: str = 'blonde'
    white: str = 'white'
    gray: str = 'gray'
    sandy: str = 'sandy'
    dark: str = 'dark'
    ginger: str = 'ginger'


class Animal:
    """
    Animal class - parent class for all animals
    """

    def __init__(self, age: int = None,
                 dob: datetime.datetime = None,
                 gender: Gender = Gender.undisclosed,
                 type: str = 'Animal',
                 name: str = None,
                 eye_color: str = 'blue',
                 hair_color: HairColor = None,
                 is_healer: bool = False):
        # specify age *or* date-of-birth (but not both) or neither
        assert age is None or dob is None, 'specify age *or* date-of-birth, but *not* both'
        # dob must be a datetime, if present
        assert dob is None or isinstance(
            dob, datetime.datetime), 'invalid date of birth'
        # age must be a positive-int, if present
        assert age is None or (isinstance(
            age, int) and age >= 0), 'invalid age'
        #
        assert name is None or (isinstance(name, str)
                                and name.strip() != ''), 'invalid name'
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
        self.__given_name__: str = name if name is None else name.strip()
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
        self.__crawling_tiredness_distance__: float = 0.1
        self.__walking_tiredness_distance__: float = 5.0
        self.__running_tiredness_distance__: float = 1.0
        self.__is_cold__: bool = False
        self.__is_sweating__: bool = False
        self.__emotions__: Set[Emotion] = set()
        self.__has_healing_touch__: bool = is_healer
        self.__words_spoken_count__: int = 0

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
            message(self.name or self.animal_type,
                    'created without date-of-birth')
    #
    @property
    def name(self) -> str: return self.__given_name__
    @name.setter
    def name(self, name: str):
        assert self.is_alive, 'cannot rename the dead'
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
        old_name = self.__given_name__
        self.__given_name__ = name
        self.notify_container()
        self.add_action(Action.changed_name, old_name, 'to', name)
        self.prop_callback()

    @property
    def is_alive(self) -> bool: return self.__breathes__

    def dies(self):
        assert self.is_alive, (self.name or self.animal_type) + \
            ' is dead already'
        # resurrection not supported - death is final!
        self.__breathes__ = False
        self.add_action(Action.died)
        self.prop_callback()

    @property
    def words_spoken_count(self) -> int:
        try:
            return self.__words_spoken_count__
        except AttributeError:
            self.__words_spoken_count__ = 0
            return self.__words_spoken_count__

    @property
    def is_wild(self) -> bool: return self.__is_wild__
    @property
    def is_tame(self) -> bool: return not self.is_wild
    @property
    def gender(self) -> Gender: return self.__gender__
    # gender-change is a thing, after all
    @gender.setter
    def gender(self, gender: Gender):
        assert isinstance(gender, Gender), 'invalid gender'
        assert self.is_alive, 'the dead cannot change gender'
        self.__gender__ = gender
        self.add_action(Action.changed_gender, gender.value)
        self.prop_callback()

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
        assert self.dob is not None, self.name or self.__animal_type__ + \
            ' has no recorded date-of-birth - cannot get age'
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
    def hair_color(self, new_color: HairColor):
        assert self.is_alive, 'the dead cannot change hair color'
        assert self.can_change_hair_color, self.name or self.animal_type + \
            ' cannot change their hair color'
        assert isinstance(new_color, HairColor), 'invalid hair color'
        old_color = self.__hair_color__
        self.__hair_color__ = new_color
        self.add_action(Action.changed_hair_color,
                        old_color.value, 'to', new_color.value)
        self.prop_callback()

    @property
    def eye_color(self) -> str: return self.__eye_color__

    def set_property_updated_callback(self, callback):
        assert callable(callback), 'callback must be a function/method'
        self.__property_updated_callback__ = callback

    def prop_callback(self):
        if not hasattr(self, '__property_updated_callback__'):
            return
        if self.__property_updated_callback__ is None:
            return
        self.__property_updated_callback__()

    def set_notify_container(self, callback):
        assert callable(callback), 'callback must be a function/method'
        self.__notify_container_callback__ = callback

    def notify_container(self):
        if not hasattr(self, '__notify_container_callback__'):
            return
        if self.__notify_container_callback__ is None:
            return
        self.__notify_container_callback__()

    # this should not really be a public method - should only be called from the
    #  Family.pet_add() etc. methods - to ensure a valid family_id is passed
    def make_pet(self, family_id: int, name: str = None):
        assert not isinstance(self, Person), self.name or self.animal_type + \
            ' is a person - slavery not supported'
        assert not self.is_pet, self.animal_type + \
            ' is already a pet called' + self.name
        assert ((isinstance(name, str) and name.strip() != '')
                or
                (isinstance(self.name, str) and self.name != '')), 'invalid pet name'
        assert isinstance(family_id, int), 'invalid family ID'
        #
        self.__is_wild__ = False
        if name is not None:
            self.name = name
        self.__family_id__ = family_id
        self.add_action(Action.became_a_pet)

    def return_to_wild(self):
        assert not isinstance(
            self, Person), self.animal_type + ' cannot be a pet anyway'
        assert self.is_pet, self.animal_type + ' is not a pet anyway'
        self.__family_id__ = None
        self.__is_wild__ = True
        self.add_action(Action.returned_to_wild)

    def kills(self, victim: 'Animal'):
        assert isinstance(victim, Animal), 'invalid animal (victim)'
        assert self.is_alive, 'the dead cannot kill'
        # victim can be ourself - i.e. suicide
        if self is victim:
            message(self.name or self.animal_type, 'commits suicide')
        elif isinstance(self, Person):
            if isinstance(victim, Person):
                message(self.name, 'murders', victim.name)
                self.__is_criminal__ = True
            else:
                message(self.name, 'kills animal',
                        victim.name or victim.animal_type)
        else:
            message(self.name or self.animal_type, 'kills',
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
        assert isinstance(illness, str), 'invalid illnes'
        illness = illness.strip()
        assert illness != '', 'invalid illness'
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
        assert isinstance(distance, (int, float)
                          ) and distance >= 0, 'invalid distance'
        distance *= 1.0
        self.__distance_travelled__ += distance

    @property
    def last_action(self) -> str:
        if len(self.__action_history__) > 0:
            return self.__action_history__[-1]
        return None

    @property
    def all_actions(self) -> List:
        return self.__action_history__

    def add_action(self, action: Action, *strings):
        assert isinstance(action, Action), 'invalid action'
        for s in strings:
            assert isinstance(s, str), 'invalid string'
        self.__action_history__.append((action, *strings))

    def crawls(self, distance: float):
        assert self.is_alive, self.name or self.animal_type + \
            "'s final crawl (to the grave) already completed"
        assert isinstance(distance, (int, float)), 'invalid distance'
        self.travelled(distance)
        self.add_action(Action.crawled, str(distance) +
                        ' ' + self.__distance_units__)
        if distance >= self.__crawling_tiredness_distance__:
            self.gets_tired()
        self.prop_callback()

    def walks(self, distance: float):
        assert self.is_alive, 'the walking dead - not supported'
        assert isinstance(distance, (int, float)), 'invalid distance'
        self.travelled(distance)
        self.add_action(Action.walked, str(distance) +
                        ' ' + self.__distance_units__)
        if distance >= self.__walking_tiredness_distance__:
            self.gets_tired()
        self.prop_callback()

    def runs(self, distance: float):
        assert self.is_alive, "the dead can't walk - let alone run"
        assert isinstance(distance, (int, float)), 'invalid distance'
        self.travelled(distance)
        self.add_action(Action.ran, str(distance) +
                        ' ' + self.__distance_units__)
        if distance >= self.__running_tiredness_distance__:
            self.gets_warm()
            self.sweats()
            self.gets_tired()
        self.prop_callback()

    @property
    def is_clean(self) -> bool: return self.__is_clean__

    def washes(self):
        self.__is_clean__ = True
        self.__is_wet__ = True
        self.add_action(Action.washed)
        self.prop_callback()

    def went_in_mud(self):
        self.__is_clean__ = False
        self.add_action(Action.was_in_mud)

    @property
    def is_wet(self) -> bool: return self.__is_wet__

    def drys(self):
        assert self.is_wet, (self.name or self.animal_type) + \
            ' is already dry (as a bone!)'
        self.__is_wet__ = False
        self.add_action(Action.dried)
        self.prop_callback()

    @property
    def is_tired(self) -> bool: return self.__is_tired__

    def gets_tired(self):
        self.__is_tired__ = True
        self.add_action(Action.got_tired)

    def rests(self):
        assert self.is_alive, (self.name or self.animal_type) + \
            " is already resting in peace"
        self.__is_tired__ = False
        self.add_action(Action.rested)
        if self.is_sweating:
            self.cools_down()
        self.prop_callback()

    def says(self, words: str):
        assert self.is_alive, (self.name or self.animal_type) + \
            " can no longer speak"
        assert isinstance(words, str), 'invalid words'
        self.add_action(Action.spoke, words)
        word_count = len(words.split())
        self.__words_spoken_count__ += word_count
        self.prop_callback()

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
        self.__is_wet__ = True
        self.add_action(Action.sweated)

    def cools_down(self):
        self.__is_sweating__ = False
        self.add_action(Action.cooled)

    @property
    def emotions(self) -> Set[Emotion]:
        return self.__emotions__

    def add_emotion(self, emotion: Emotion):
        assert isinstance(emotion, Emotion), 'invalid emotion'
        self.__emotions__.add(emotion)

    @property
    def has_healing_touch(self) -> bool: return self.__has_healing_touch__

    def touches(self, other: 'Animal'):
        assert isinstance(other, Animal), 'invalid animal'
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
        assert isinstance(can_fly, bool), 'invalid can-fly value'
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
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
        # specify age *or* date-of-birth, but not both
        assert age is None or dob is None, 'specify age *or* date-of-birth, but not both'
        assert age is not None or dob is not None, 'specify age *or* date-of-birth, but not both'
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
            self.__hair_color__ = HairColor.brunette

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
        assert sinner is not None and isinstance(
            sinner, Person), 'invalid person (sinner)'
        assert self.is_alive, 'the dead cannot forgive'
        #
        sinner.__is_forgiven__ = True

    def is_sibling_of(self, other: 'Person') -> bool:
        return other.family_id == self.family_id

    def is_brother_of(self, other: 'Person') -> bool:
        return self.is_sibling_of(other) and self.gender == Gender.male

    def is_sister_of(self, other: 'Person') -> bool:
        return self.is_sibling_of(other) and self.gender == Gender.female

    def __getstate__(self):
        state = self.__dict__.copy()
        if hasattr(self, '__property_updated_callback__'):
            del state['__property_updated_callback__']
        if hasattr(self, '__notify_container_callback__'):
            del state['__notify_container_callback__']
        return state


class Family:
    """
    Family class - having parents, children
    """
    #
    __family_id__: int = 0

    @classmethod
    def __next_id__(cls) -> int:
        cls.__family_id__ += 1
        return cls.__family_id__

    def __init__(self, name: str, members_updated_callback=None):
        # name must be a non-empty string
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
        #
        self.__family_id__ = Family.__next_id__()
        # the community ID this person currently belongs to
        self.__community_id__: int = None
        #
        self.__family_name__ = name
        self.__parents__: List[Person] = list()
        self.__children__: List[Person] = list()
        self.__pets__: List[Animal] = list()
        message(name, 'family created')
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
        assert isinstance(new_name, str), 'invalid name'
        new_name = new_name.strip()
        assert new_name != '', 'invalid name'
        self.__family_name__ = new_name
        self.notify_container()
        self.prop_callback()

    def prop_callback(self):
        if self.__members_updated_callback__ is not None:
            self.__members_updated_callback__()

    def set_notify_container(self, callback):
        assert callable(callback), 'callback must be a function/method'
        self.__notify_container_callback__ = callback

    def notify_container(self):
        if not hasattr(self, '__notify_container_callback__'):
            return
        if self.__notify_container_callback__ is None:
            return
        self.__notify_container_callback__()

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

    def set_members_updated_callback(self, callback: callable):
        assert callable(
            callback), 'callback must be a callable function/method'
        self.__members_updated_callback__ = callback

    @property
    def alive_parents(self) -> List[Person]:
        return [parent for parent in self.parents if parent.is_alive]

    def gives_birth(self, name: str, gender: Gender = Gender.undisclosed):
        assert isinstance(name, str), 'invalid name'
        #
        baby = Person(name=name, dob=datetime.datetime.now())
        baby.add_action(Action.was_born)
        self.child_add(person=baby)

    def adopts_child(self, person: Person):
        assert isinstance(person, Person), 'invalid person'
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
        assert isinstance(person, Person), 'invalid person'
        return person in self.parents

    def has_child(self, person: Person) -> bool:
        assert isinstance(person, Person), 'invalid person'
        return person in self.children

    def has_pet(self, pet: Animal) -> bool:
        assert isinstance(pet, Animal), 'invalid animal'
        if pet.is_pet:
            return pet in self.pets
        return False

    def pet_add(self, pet: Animal, name: str = None):
        """
        add a pet to this family
        """
        assert isinstance(pet, Animal)
        # cannot add a pet if already a pet
        assert not self.has_pet(pet), 'already has pet' + \
            pet.name + ' - cannot add again'
        #
        assert not isinstance(pet, Person), pet.name + \
            ' is a person - cannot be a pet'
        #
        assert pet.family_id is None, pet.name + \
            ' already belongs to a family, cannot add to another'
        #
        pet.make_pet(family_id=self.id, name=name)
        self.pets.append(pet)
        message(self.name, 'family: added pet', pet.name)

    def pet_remove(self, pet: Animal):
        """
        remove a pet from this family
        """
        assert isinstance(pet, Animal)
        assert pet in self.pets, 'does not have pet ' + pet.name + ' - cannot remove'
        self.pets.remove(pet)
        pet.return_to_wild()
        message(self.name, 'family: removed pet', pet.name)

    def child_add(self, person: Person):
        """
        add a child to this family
        """
        assert isinstance(person, Person), 'invalid person'
        # cannot add as child if already a parent
        assert not self.has_parent(
            person), 'already has parent' + person.name + ' - cannot add as a child'
        # cannot add as child if already a child
        assert not self.has_child(
            person), 'already has child' + person.name + ' - cannot add again'
        # age must be less than parent ages
        for parent in self.parents:
            assert person.dob > parent.dob, person.name + \
                ' is older than (parent)' + parent.name + \
                ' - cannot be their child'

        # now can add as a child
        message(self.name, 'family: added child', person.name)
        self.children.append(person)
        person.__family_id__ = self.__family_id__
        person.add_action(Action.child_added_to_family, self.name)
        self.prop_callback()

    def child_remove(self, person: Person):
        """
        remove a child from this family(!)
        """
        #
        assert person is not None and isinstance(person, Person)
        #
        assert person in self.children, person.name + ' is not a child, cannot remove'
        self.children.remove(person)
        person.__family_id__ = None
        person.add_action(Action.removed_from_family, self.name)
        print(self.name, 'family: removed child', person.name)
        self.prop_callback()

    def parent_add(self, person: Person):
        """
        add a parent to this family
        """
        assert person is not None and isinstance(person, Person)
        # cannot add as parent if already a parent of this family
        assert not self.has_parent(
            person), 'already has parent ' + person.name + ' - cannot add again'
        # cannot add as parent if already a child of this family
        assert not self.has_child(
            person), 'already has child ' + person.name + ' - cannot add as a parent'
        # cannot have more than 2 alive parents
        assert not len(
            self.alive_parents) >= 2, '2 alive parents already - cannot add more'
        # age of parent cannot be less than children
        for child in self.children:
            assert person.dob < child.dob, person.name + \
                ' is younger than (child) ' + child.name + \
                ' - cannot be their parent'
        # no gender-related restrictions on who can be parents(!)
        #
        # now can add the parent
        self.parents.append(person)
        person.__parent_of_families_id__.add(self.__family_id__)
        person.add_action(Action.became_parent, self.name)
        message(self.name, 'family: added parent', person.name)
        self.prop_callback()

    def parent_remove(self, person: Person):
        """
        remove a parent from this family(!)
        """
        #
        assert isinstance(person, Person), 'invalid person'
        assert person in self.parents, person.name + ' is not a parent, cannot remove'
        #
        self.parents.remove(person)
        person.__parent_of_families_id__.remove(self.__family_id__)
        person.add_action(Action.removed_as_parent, self.name)
        message(self.name, 'family: removed parent', person.name)
        self.prop_callback()

    # for pickling
    def __getstate__(self):
        state = self.__dict__.copy()
        if hasattr(self, '__members_updated_callback__'):
            del state['__members_updated_callback__']
        if hasattr(self, '__notify_container_callback__'):
            del state['__notify_container_callback__']
        return state


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
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
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
        assert isinstance(new_name, str), 'invalid name'
        new_name = new_name.strip()
        assert new_name != '', 'invalid name'
        self.__community_name__ = new_name
        self.notify_container()
        self.prop_callback()

    def prop_callback(self):
        if self.__families_updated_callback__ is not None:
            self.__families_updated_callback__()

    def set_notify_container(self, callback):
        assert callable(callback), 'callback must be a function/method'
        self.__notify_container_callback__ = callback

    def notify_container(self):
        if not hasattr(self, '__notify_container_callback__'):
            return
        if self.__notify_container_callback__ is None:
            return
        self.__notify_container_callback__()

    @property
    def all_families(self) -> List[Family]: return self.__all_families__
    @property
    def all_families_names(self) -> List[str]:
        return [f.name for f in self.all_families]

    def set_families_updated_callback(self, callback: callable):
        assert callable(
            callback), 'callback must be a callable function/method'
        self.__families_updated_callback__ = callback

    def new_family(self, name: str, members_updated_callback=None):
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
        fam = Family(
            name=name, members_updated_callback=members_updated_callback)
        self.family_add(fam)

    def family_add(self, family: Family):
        assert isinstance(family, Family), 'invalid family'
        #
        # cannot already be in this community
        assert family.community_id != self.id, 'cannot add ' + \
            family.name + ' family: already in this community'
        # cannot belong to another community already
        assert family.community_id is None, 'cannot add ' + \
            family.name + ' family: is in another community'
        # so we're good to go
        self.all_families.append(family)
        family.__community_id__ = self.__community_id__
        message(self.name, 'community: added', family.name, 'family')
        self.prop_callback()

    def family_remove(self, family: Family):
        assert isinstance(family, Family), 'invalid family'
        #
        assert family in self.all_families, 'cannot remove ' + \
            family.name + ' family: not in this community'
        self.all_families.remove(family)
        family.__community_id__ = None
        message(self.name, 'community: removed', family.name, 'family')
        self.prop_callback()

    @property
    def population(self) -> int:
        ids = set()
        for family in self.all_families:
            ids = ids.union(family.member_ids)
        return len(ids)

    def family_of(self, person_or_pet) -> Family:
        assert isinstance(person_or_pet, Animal), 'invalid person or animal'
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
        assert len(families) > 0, person_or_pet.name + ' has no family'
        return families[0]

    def surname_of(self, person: Person) -> str:
        assert isinstance(person, Person), 'invalid person'
        #
        family = self.family_of(person)
        assert family is not None, person.name + ' has no surname'
        return family.name

    def parents_of(self, person: Person) -> List[Person]:
        assert isinstance(person, Person), 'invalid person'
        #
        family = self.family_of(person)
        assert family is not None, person.name + ' has no parents'
        return family.parents

    def parent_add(self, person: Person, parent: Person):
        """
        add parent as a parent in the family of person
        """
        #
        assert isinstance(person, Person), 'invalid person'
        assert isinstance(parent, Person), 'invalid parent'
        #
        family = self.family_of(person)
        assert family is not None, person.name + ' cannot add parent - no family'
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
        assert family is not None, person.name + ' cannot remove parent - no family'
        family.parent_remove(parent)

    def father_of(self, person: Person) -> Person:
        assert isinstance(person, Person), 'invalid person'
        #
        parents = self.parents_of(person)
        assert len(parents) > 0, person.name + ' has no father'
        for parent in parents:
            if parent.gender == Gender.male:
                return parent
        assert False, person.name + ' has no father'

    def mother_of(self, person: Person) -> Person:
        assert isinstance(person, Person), 'invalid person'
        #
        parents = self.parents_of(person)
        assert len(parents) > 0, person.name + ' has no mother'
        for parent in parents:
            if parent.gender == Gender.female:
                return parent
        assert False, person.name + ' has no mother'

    def siblings_of(self, person: Person) -> List[Person]:
        assert isinstance(person, Person), 'invalid person'
        #
        family = self.family_of(person)
        assert family is not None, person.name + ' has no siblings'
        # so we have a family - but we could be either a child or parent
        # ensure we're a child-only
        assert person in family.children, person.name + ' is not a child here'
        return [sibling for sibling in family.children if sibling is not person]

    def sibling_add(self, person: Person, sibling: Person):
        """
        add sibling as a child in the family of person
        """
        #
        assert isinstance(person, Person), 'invalid person'
        assert isinstance(sibling, Person), 'invalid sibling'
        #
        assert person is not sibling, person.name + \
            ' cannot be added as a sibling of himself/herself'
        family = self.family_of(person)
        assert family is not None, person.name + \
            ' cannot add sibling' + sibling.name + ' - no family'
        family.child_add(sibling)

    def sibling_remove(self, person: Person, sibling: Person):
        """
        remove sibling from the family of person
        """
        #
        assert isinstance(person, Person), 'invalid person'
        assert isinstance(sibling, Person), 'invalid sibling'
        #
        assert person is not sibling, person.name + \
            ' cannot be removed as a sibling of himself/herself'
        family = self.family_of(person)
        assert family is not None, person.name + \
            ' cannot remove sibling' + sibling.name + ' - no family'
        family.child_remove(sibling)

    def pet_add(self, person: Person, pet: Animal, name: str = None):
        """
        add pet into the family of person
        """
        #
        assert isinstance(person, Person), 'invalid person'
        assert isinstance(pet, Animal), 'invalid animal'
        #
        family = self.family_of(person)
        assert family is not None, person.name + \
            ' cannot add pet' + pet.name + ' - no family'
        family.pet_add(pet, name=name)

    def pets_of(self, person: Person) -> List[Animal]:
        """
        return all the pets of the family of person
        """
        assert isinstance(person, Person), 'invalid person'
        #
        family = self.family_of(person)
        assert family is not None, person.name + 'cannot find pets - no family'
        return family.pets

    # for pickling
    def __getstate__(self):
        state = self.__dict__.copy()
        if hasattr(self, '__families_updated_callback__'):
            del state['__families_updated_callback__']
        if hasattr(self, '__notify_container_callback__'):
            del state['__notify_container_callback__']
        return state


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
        assert isinstance(name, str), 'invalid name'
        name = name.strip()
        assert name != '', 'invalid name'
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
        assert isinstance(new_name, str), 'invalid name'
        new_name = new_name.strip()
        assert new_name != '', 'invalid name'
        self.__world_name__ = new_name
        self.prop_callback()

    def set_communities_updated_callback(self, callback):
        assert callable(
            callback), 'callback must be a callable function/method'
        self.__communities_updated_callback__ = callback

    @property
    def all_communities(self) -> List[Community]:
        return self.__all_communities__

    @property
    def all_communities_names(self) -> List[str]:
        return [c.name for c in self.all_communities]

    def new_community(self, name: str, families_updated_callback=None):
        assert isinstance(name, str) and name != '', 'invalid name'
        #
        com = Community(
            name=name, families_updated_callback=families_updated_callback)
        self.community_add(com)

    def prop_callback(self):
        if self.__communities_updated_callback__ is not None:
            self.__communities_updated_callback__()

    def community_add(self, community: Community):
        assert isinstance(community, Community), 'invalid community'
        # cannot already be in this world
        assert community.world_id != self.id, 'cannot add ' + \
            community.name + ' community: already in this world'
        # cannot belong to another world already
        assert community.world_id is None, 'cannot add ' + \
            community.name + ' community: is in another world'
        # so we're good to go
        self.all_communities.append(community)
        community.__world_id__ = self.__world_id__
        message(self.name, 'world: added', community.name, 'community')
        self.prop_callback()

    def community_remove(self, community: Community):
        assert isinstance(community, Community), 'invalid community'
        #
        assert community in self.all_communities, 'cannot remove' + \
            community.name + ' community: not in this world'
        self.all_communities.remove(community)
        community.__world_id__ = None
        message(self.name, 'world: removed', community.name, 'community(!)')
        self.prop_callback()

    def comm_id_of(self, family_id: int) -> int:
        assert isinstance(family_id, int), 'invalid family ID'
        #
        comms = [
            com for com in self.all_communities for fam in com.all_families if fam.id == family_id]
        if len(comms) > 0:
            return comms[0]
        return None

    def community_of(self, family_or_person_or_pet) -> Community:
        assert isinstance(family_or_person_or_pet, (Family, Animal)
                          ), ' invalid family, person or animal'
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
        assert family_id is not None, 'cannot find family ID for person ' + \
            family_or_person_or_pet.name
        com = self.comm_id_of(family_id)
        assert com is not None, 'community for person ' + \
            family_or_person_or_pet.name + ' is not in this world'
        return com

    def family_of(self, person_or_pet) -> Family:
        assert isinstance(person_or_pet, Animal), 'invalid person or animal'
        #
        comm = self.community_of(person_or_pet)
        # assert comm is not None, 'person/pet is not in a community'
        # so we can hand-off this search to the community
        return comm.family_of(person_or_pet)

    @property
    def population(self) -> int:
        pop: int = 0
        for com in self.all_communities:
            pop += com.population
        return pop

    def store_to_file(self, filename: str):
        assert isinstance(filename, str), 'invalid file name'
        filename = filename.strip()
        assert filename != '', 'invalid file name'
        #
        # we need to store:
        # - this "World" object
        # - and the current values of:
        #   - Community.__community_id__
        #   - Family.__family_id__
        #   - Person.__person_id__
        # so that upon successful re-load we can continue generating new instances
        # with unique IDs
        #
        with open(filename, 'wb') as file_to_store:
            pickle.dump([self,
                         Community.__community_id__,
                         Family.__family_id__,
                         Person.__person_id__,
                         ], file_to_store)

    @classmethod
    def load_from_file(cls, filename: str) -> 'World':
        assert isinstance(filename, str), 'invalid file name'
        with open(filename, 'rb') as file_to_load:
            data_list = pickle.load(file_to_load)
        world = data_list[0]
        # set the class ID counters
        Community.__community_id__ = data_list[1]
        Family.__family_id__ = data_list[2]
        Person.__person_id__ = data_list[3]
        return world

    # to help in pickling
    def __getstate__(self):
        state = self.__dict__.copy()
        if hasattr(self, '__communities_updated_callback__'):
            del state['__communities_updated_callback__']
        return state


def message(*messages):
    if __name__ != '__main__':
        return
    print(*messages)


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
