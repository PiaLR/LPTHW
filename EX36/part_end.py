import time
from sys import exit


def end_loose(reason):
    print reason,
    print "\n\n\tGAME OVER"
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print """
        NOOB!

_____________$$$$$$$$$$$$$$$$$$$
___________$$$$$$$$$$$$$$$$$$$$$$$
________$$$$___$$$$$$$$$$$$$$$___$$$
______$$$$______$$$$$$$$$$$$______$$$$
____$$$$$________$$$$$$$$$$________$$$$
___$$$$$__________$$$$$$$$___________$$$$
__$$$$$____________$$$$$$____________$$$$$
_$$$$$$____________$$$$$$$____________$$$$ $
_$$$$$$___________$$$$$$$$$___________$$$$ $$
_$$$$$$$_________$$$_$$$_$$$_________$$$$$ $$
_$$$$$$$$______$$$$___$___$$$$______$$$$$$ $$
_$$$$$$$$$$$$$$$$$___$$$___$$$$$$$$$$$$$$$ $$
_$$$_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_o $$
_$$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__$ $$
__$$$__$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__o$ $$
__'$$o__$$__$$'$$$$$$$$$$$$$$'$$__$$_____o $$
____$$o$____$$__'$$'$$'$$'__$$______$___o$ $
_____$$$o$__$____$$___$$___$$_____$$__o$
______'$$$$O$____$$____$$___$$ ____o$$$
_________'$$o$$___$$___$$___$$___o$$$
___________'$$$$o$o$o$o$o$o$o$o$$$$'
______________'$$$$$$$$$$$$$$$$$$$ """
    exit(0)


def end_wtf():
    print"""
    I have no idea what just happened. But as a good programmer I have to say:

    That was probably my fault...

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ____     | || |  _______     | || |  _______     | || |  ____  ____  | |
| |   /  ___  |  | || |   .'    `.   | || | |_   __ \    | || | |_   __ \    | || | |_  _||_  _| | |
| |  |  (__ \_|  | || |  /  .--.  \  | || |   | |__) |   | || |   | |__) |   | || |   \ \  / /   | |
| |   '.___`-.   | || |  | |    | |  | || |   |  __ /    | || |   |  __ /    | || |    \ \/ /    | |
| |  |`\____) |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |  \ \_  | || |    _|  |_    | |
| |  |_______.'  | || |   `.____.'   | || | |____| |___| | || | |____| |___| | || |   |______|   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

    Maybe you could just start from the beginning again...?"""
    exit(0)

def end_win(name):
    user_name = name
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print"""
    You found the holy grail of Python!

             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`

    %s, you are truly a worthy student of Shaw.
    
  _____ ____   _  __ _____ ___   ___  ______ ____
 / ___// __ \ / |/ // ___// _ \ / _ |/_  __// __/
/ /__ / /_/ //    // (_ // , _// __ | / /  _\ )
\___/ \____//_/|_/ \___//_/|_|/_/ |_|/_/ /___/""" % user_name
    exit(0)

end_win("idiot")