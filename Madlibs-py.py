#Mad libs generator
from random import randint
import copy

story = (
    "It was a {}, cold November day. I.\n"+
    "woke up to the {} smell of {}\n"+
    "roasting in the {} downstairs. I\n"+
    "{} down the stairs to see if I could\n"+
    "help {} the dinner. My mom said,\n"+
    "\"See if {} needs a fresh {}.\"So I\n"+
    "carried a tray of glasses full of {} into\n"+
    "the {} room. When I got there, I\n"+
    "couldn't believe my {}! There were\n"+
    "{} {} on the {}!\n"

)

word_dict = {
    'adjective':['freeze','moment','cruel','charming','gentle','perfect'],
    'type_of_bird':['hummingbird','finch','raven','robin','cardinal','sparrow'],
    'room in house':['kitchen','bathroom','bedroom','living room','garden','attic'],
    'verb':['dropped','ran','jumped','made','wrote','read'],
    'relatives_name':['dad','mom','brother','sister','uncle','aunt'],
    'noun':['book','ball','table','piano','keyboard','mouse'],
    'liquid':['water','juice','milk','coffee','tea','soda'],
    'verb_ing':['jumping','running','eating','drinking','sleeping','reading'],
    'part_of_the_body_plural':['eyes','legs','arms','hands','feet','nose'],
    'plural_noun':['birds','geese','fish','frogs','puppies','kittens'],
}

def get_word(type,local_dict):
    words = local_dict[type]
    count = len(words)-1
    index = randint (0,count)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective',local_dict),
        get_word('adjective', local_dict),
        get_word('type_of_bird',local_dict),
        get_word('room in house',local_dict),
        get_word('verb',local_dict),
        get_word('verb', local_dict),
        get_word('relatives_name',local_dict),
        get_word('noun',local_dict),
        get_word('liquid',local_dict),
        get_word('verb_ing',local_dict),
        get_word('part_of_the_body_plural',local_dict),
        get_word('plural_noun',local_dict),
        get_word('verb_ing',local_dict),
        get_word('noun',local_dict)
    )

print("STORY 1: ")
print(create_story())




