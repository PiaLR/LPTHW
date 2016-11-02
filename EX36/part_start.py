# -*- coding: utf-8 -*-
import time

def start_welcome():
    print """
                                                        !_
                                                    |*~=-.,
                                                    |_,-'`
                                                    |
                                                    |
                                                   /^
                     !_                           /   \\
                     |*`~-.,                     /,    \\
                     |.-~^`                     /#"     \\
                     |                        _/##_   _  \_
                _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
               [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
             !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
             |*`--,_- _        |            |*`~-.,= []  |
             |.-'|=     []     |   !_       |_.-"`_-     |
             |   |_=- -        |   |*`~-.,  |  |=_-      |
            /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
        _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
       [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
        |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
       _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
      [ ]_[ ]_[ ]_[ ]=_0~[_ _ _]~0   [ ]_[ ]_[ ]_[ ]=-   | \\
      |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
       | _- =-     |-_   | ((* |      |= _=       | -    |___\\
       |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
       | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
       |-_=- _     |=_   =            |=_= -_     |  =   ||+||
       |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
       |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
       |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
       |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
       | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
       |=_ =       | =_-_| |  | |     |   =_      | -_   |
       |_=-_       |=_=  | |  | |     |=_=        |=-    |
 `^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^

            WELCOME TO THE CASTLE OF PYTHON!
 """
    start_password()


def start_password():
    password = raw_input("\n\tType in the password: ")
    if password == "wise20162016":
        print "\n\tCorrect!"
        setup()
    else:
        print "\n\tPassword not correct. Hint: It's our tumblr password!"
        start_password()


def setup():
    key_found = "no"
    user_name = raw_input("\n\tType a username: ")
    print "\n\tWelcome to the castle, %s!" % user_name
    weapon_list = ['sword', 'shotgun', 'candy']
    weapon_string = ' or '.join(weapon_list)
    user_weapon = raw_input("\n\tChoose your weapon:\n \n\t{} >> ".format(weapon_string)).lower()
    if user_weapon in weapon_list:
        print "\n\tAlright, the %s will be your weapon!" % user_weapon
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        start_room(user_name, user_weapon, key_found)
    else:
        print "\n\t%s?! Please concentrate a little more, in this castle we type everything exactly right! \n\tBy the way, what was your name again?" % user_weapon
        setup()

def start_room(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print """
        %s, you find yourself in the castle's impressive entrance hall.
        Actually, it's not that impressive: All you can see is an old trunk and a door.
        Oh and of course you have your %s with you.
        So, what do you want to do?

        1. Check out the trunk

        2. Go through the door""" % (user_name, user_weapon)
    start_room_choice(user_name, user_weapon, key_found)


def start_room_choice(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    start_room_decision = raw_input("\n\t>> ").lower()
    # print "your name is %s your weapon is %s - the key is found? %s" % (user_name, user_weapon, key_found)
    if "1" in start_room_decision or "check" in start_room_decision or "trunk" in start_room_decision:
        if key_found == "no":
            print "\n\tThe trunk is locked."
            start_room(name, weapon, key)
        elif key_found == "yes":
            print "\n\tYou pick out Shaw's key and put it into the trunk's lock - it fits! \nThe trunk slowly opens up and..."
            #end_win
        else:
            print "WTF SCREEN"
            # WTF SCREEN
    elif "2" in start_room_decision or "go" in start_room_decision or "door" in start_room_decision:
        print "\n\tOk, let's get in there ..."
        #jonathan_office
    else:
        print "\n\tI'm afraid that's not an option!"
        start_room_choice(name, weapon, key)



start_welcome()
