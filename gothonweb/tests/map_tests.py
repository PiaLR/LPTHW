from nose.tools import *
from map import *


def test_scene():
    gold = Scene("GoldScene", "goldroom", """
                This room has gold in it you can grab. There's a
                door to the north.
                """)
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})

def test_scene_paths():
    center = Scene("Center", "center", "Test room in the center.")
    north = Scene("North", "north", "Test room in the north.")
    south = Scene("South", "south", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.")
    west = Scene("Trees", "trees", "There are trees here, you can go east.")
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), death_corridor_shoot)
    assert_equal(START.go('dodge!'), death_corridor_dodge)
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal(NEXT.go('132'), the_bridge)
    assert_equal(NEXT.go('999'), death_laser_weapon_armory)
    assert_equal(NEXTNEXT.go('slowly place the bomb'), escape_pod)
    assert_equal(NEXTNEXT.go('throw the bomb'), death_bridge)
    assert_equal(END.go('2'), the_end_winner)
    assert_equal(END.go('4'), the_end_loser)
