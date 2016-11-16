import time
import sys
from sys import exit

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

from windows import UnsolvedWindow
from windows import SolvedWindow


class Scene(object):

    def enter(self): # just in case an unintended scene is entered
        print "How did you get here? Get out."
        exit(1)


class Crime(Scene):

    def enter(self):
        # using print instead of """ for a more appealing look (and Shaw did it)
        print "It is Sunday, January 1st 2017 and your year is not"
        print "starting well. Not only are you hungover, you are also on"
        print "the way to a horrible crime scene. The victim, Mr. Boddy, had"
        print "invited three of his best friends to his mansion, to celebrate"
        print "new year's eve. These four men were passionate riddle solvers."
        print "Apparently, two of them got into a fight over a logical paradox"
        print "- and one of them didn't survive that. Mr. Boddy was found dead"
        print "in the early morning. His three friends, all of them suspects"
        print "or at least witnesses, are waiting for you in the mansion."
        # delays and blank lines shall give user a better reading flow
        time.sleep(2)
        print "\n"
        print "When you arrive at the mansion a young officer is already"
        print "awaiting you: 'Detective Grey! Detective Grey!', he shouts from"
        print "a distance, beckoning you. 'Good morning, what do we have"
        print "here?', you ask, while you enter the hallway. Mr. Boddy's body"
        print "is lying right in the entrance hall. 'Sir, detective Grey, Sir,"
        print "I have never experienced something this ... disturbing', the"
        print "officer replies. You are trying to take a closer look at the"
        print "body but he stops you: 'No Sir, the body is not what I meant."
        print "I\'m talking about the men who are awaiting you. They all have"
        # escape probably not needed, but you never know, right?
        print "seen who murdered Mr. Boddy. However, they insist on sticking"
        print "to the rules of their stupid 'riddle club'.' "
        print "- 'What do you mean?', you ask, already confused. 'They are only"
        print "giving us hints about who's done it by telling us riddles. Only"
        print "if we solve those, we will be able to find out who of them is"
        print "the murderer', the officer explains. 'Interesting ... Let me"
        print "see if I can solve this case. Where can I find the men?', you"
        print "ask. This story met your interest. 'The first one is awaiting"
        print "you right behind that door...', the officer guides you into the"
        print "first room."

        return 'library_scene'

class Library(Scene):

    def enter(self):
        time.sleep(2)
        print "\n"
        print "You find yourself in the mansion's library. An impressive amount"
        print "of books, most of them looking old and expensive, fills almost"
        print "every inch of this room. Only in one corner someone has left"
        print "space - for an old wing chair. A man sits in it. What do you want"
        print "to do now, detective?"
        print "1. Talk to the man."
        print "2. Go to the next room."

        action = raw_input(">> ").lower()
        # 'lower' important in case user didn't type in lowercase

        if "1" in action or "talk" in action or "man" in action:
        # trying to guess different answers; making game more logic & enjoyable
            time.sleep(2)
            print "\n"
            print "You decided to talk to the man."
            print "What do you want to ask him about?"
            print "1. Ask him for his name."
            print "2. Ask him for his age."
            print "3. Ask him for his profession."
            print "4. Ask him for a clue."

            question = raw_input(">> ").lower()

            if "1" in question or "name" in question:
                time.sleep(2)
                print "\n"
                print "'Well son,' the man says with an impressive deep voice"
                print "'most people know me as Reverend Mr. Green.'"
                return 'library_scene'

            elif "2" in question or "age" in question:
                time.sleep(2)
                print "\n"
                print "'Let me answer this question with Psalm 71:18', the man"
                print "says, taking a deep breath '- just kidding, I\'m 52. But"
                print "don\'t tell anyone.'"
                return 'library_scene'

            elif "3" in question or "profession" in question:
                time.sleep(2)
                print "\n"
                print "'The Lord is my shepherd... and my profession', the man"
                print "replies smiling. 'I\'m a priest!'"
                return 'library_scene'

            elif "4" in question or "clue" in question:
                time.sleep(2)
                print "\n"
                print "'Alright, son, let me give you a hint: The day before"
                print "yesterday the murderer was 25 years old and next year he"
                print "will turn 28. This is true only today. So what day is"
                print "his birthday? If you can solve this riddle, you will"
                print "know the murderers age as well', the man replies,"
                print "stifling a laugh."
                return 'library_scene'

            else:
                print "\n"
                print "That's not an option, concentrate!"
                return 'library_scene'

        elif "2" in action or "go" in action or "next" in action:
            time.sleep(2)
            print "\n"
            print "You decide that there is nothing more to investigate in this"
            print "room. 'Trust in the Lord with all your heart and lean not on"
            print "your own understanding; in all your ways submit to him, and"
            print "he will make your paths straight', you can hear the man"
            print "whisper while you are leaving."
            return 'dining_scene'

        else:
            print "\n"
            print "That's not an option, concentrate!"
            return 'library_scene'

class Dining(Scene):

    def enter(self):
        time.sleep(2)
        print "\n"
        print "You find yourself in the dining room. The table is still laid"
        print "for four persons, but only one man sits at it. He sips on a"
        print "drink that looks a lot like Scotch. What do you want do now,"
        print "detective?"
        print "1. Talk to the man."
        print "2. Go to the next room."

        action = raw_input(">> ").lower()

        if "1" in action or "talk" in action or "man" in action:
            time.sleep(2)
            print "\n"
            print "You decided to talk to the man."
            print "What do you want to ask him about?"
            print "1. Ask him for his name."
            print "2. Ask him for his age."
            print "3. Ask him for his profession."
            print "4. Ask him for a clue."

            question = raw_input(">> ").lower()

            if "1" in question or "name" in question:
                time.sleep(2)
                print "\n"
                print "'Hey there detective, you must have already met Reverend"
                print "Mr. Green?', the man slurs. 'Don\'t worry, I\'m only"
                print "half as weird as he is. My name is Prof. Dr. Plum!'"
                return 'dining_scene'

            elif "2" in question or "age" in question:
                time.sleep(2)
                print "\n"
                print "'Don\'t worry I\'m old enough to have this drink', the"
                print "man replies 'To be precise: I\'m 26 years old.'"
                return 'dining_scene'

            elif "3" in question or "profession" in question:
                time.sleep(2)
                print "\n"
                print "'I\'m a professional python programmer!!!', the man"
                print "shouts proudly. You can smell the alcohol in his breath."
                return 'dining_scene'

            elif "4" in question or "clue" in question:
                time.sleep(2)
                print "\n"
                print "'Of course I have a clue fo-' the man replies,"
                print "interrupted by a hiccup. '-Sorry about that -hic- where"
                print "was I? Ah sure, the clue! -hic- The murderer has married"
                print "-hic- many women, but has never -hic- been married. Can"
                print "you -hic- guess what his profession is?'"
                return 'dining_scene'

            else:
                print "\n"
                print "That's not an option, concentrate!"
                return 'dining_scene'

        elif "2" in action or "go" in action or "next" in action:
            time.sleep(2)
            print "\n"
            print "You decide that there is nothing more to investigate in this"
            print "room. 'Oh no buddy, don\'t leave me already!', the man at"
            print "the table shouts. 'Let\'s have a drink together! Or two?'."
            print "Even though that\'s tempting, you ignore him and enter the"
            print "next room."
            return 'kitchen_scene'

        else:
            print "\n"
            print "That's not an option, concentrate!"
            return 'dining_scene'

class Kitchen(Scene):

    def enter(self):
        time.sleep(2)
        print "\n"
        print "You have entered a cozy little kitchen. A young man with a"
        print "warm smile welcomes you: 'Detective, I've been already awaiting"
        print "you. Did you enjoy talking to my two friends? I can already"
        print "imagine what you want to ask me, so let's cut that short:"
        print "My name is Collin Mustard, I\'m 26 years old and I work as a"
        print "dentist. Moreover, I have to tell you something about me and my"
        print "friends, that you don't know yet. In order to make the meetings"
        print "of our riddle club more interesting we have agreed on the"
        print "following: Reverend Mr. Green always tells the truth while Mr."
        print "Boddy always lies- or lied, I should say. Prof. Dr. Plum and I"
        print "have the same agreement. One of us always lies and one of us"
        print "always tells the truth. However, we all know very well who"
        print "murdered Mr. Boddy - and if you ask me the right question you"
        print "will find out, too. But I will only answer one of the following"
        print "questions, so choose wisely.'"
        print "What do you want to ask Collin Mustard?"
        print "1. Have you killed Mr. Boddy?"
        print "2. If I asked Prof. Dr. Plum, who would he say killed Mr. Boddy?"
        print "3. Can I have a drink?"

        question = raw_input(">> ").lower()

        if "1" in question or "you" in question:
            time.sleep(2)
            print "\n"
            print "'Yes, I have. Please leave now.' You leave the kitchen."
            return 'solving_scene'

        elif "2" in question or "plum" in question:
            time.sleep(2)
            print "\n"
            print "'If you asked Prof. Dr. Plum who the killer was, he would"
            print "tell you it was him. Please leave now.' You leave the"
            print "kitchen."
            return 'solving_scene'

        elif "3" in question or "drink" in question:
            time.sleep(2)
            print "\n"
            print "'Sure, there you go. Please leave now.' You leave the"
            print "kitchen."
            return 'solving_scene'

        else:
            print "\n"
            print "That's not an option, concentrate!"
            return 'kitchen_scene'

class Solving(Scene):

    def enter(self):
        time.sleep(2)
        print "\n"
        print "You find yourself in the entrance hall again. While you are"
        print "still trying to collect your thoughts, you hear a well known"
        print "voice right behind you: 'Hello detective Gray, what are you"
        print "doing here? I didn't know that Scotland Yard let's amateurs"
        print "like you solve cases this big.' When you turn around you see"
        print "detective White, your archrival. You smile at him, as"
        print "disarmingly as you can. 'Detective White, what a pleasure to"
        print "see you. Sit down, grab a cup of tea, and don't worry about"
        print "this case - I have already solved it', you say. 'Oh, have you?"
        print "Well, I know who the solution to this riddle mess, too. So let"
        print "me know: Who do you think is the murderer?', White replies with"
        print "an evil smile. You know White is a wiseacre, so you type one of"
        print "the following names exactly right:"
        print "\n"

        # did this mostly because I wanted to use a list at some point
        murderer_list = [
        'Mr. Boddy',
        'Reverend Mr. Green',
        'Prof. Dr. Plum',
        'Collin Mustard',
        'Detective White'
        ]
        # adding quotes and 'or' to make it more readable for user
        murderer_string = '"' + '" or "'.join(murderer_list) + '"'

        murderer = raw_input("{} \n>> ".format(murderer_string))

        # saves time & space because you don't have to guess & type answers
        if murderer == murderer_list[3]:
            return 'solved_scene'
        elif murderer == murderer_list[0]:
            return 'unsolved_scene'
        elif murderer == murderer_list[1]:
            return 'unsolved_scene'
        elif murderer == murderer_list[2]:
            return 'unsolved_scene'
        elif murderer == murderer_list[4]:
            return 'unsolved_scene'
        else:
            print "That's not an option, concentrate!"
            return 'solving_scene'

class Solved(Scene):

    def enter(self):
        app = QApplication(sys.argv)
        winwindow = SolvedWindow()
        sys.exit(app.exec_())

class Unsolved(Scene):

    def enter(self):
        app = QApplication(sys.argv)
        loosewindow = UnsolvedWindow()
        sys.exit(app.exec_())

# limiting line length to 80 characters because ... style, that's why.
