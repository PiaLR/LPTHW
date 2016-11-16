from scenes import *


class Runner(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('solved_scene') or self.scene_map.next_scene('unsolved_scene')
        # didn't know who to break line properly in this case

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map(object):

    scenes = {
        'crime_scene': Crime(),
        'library_scene': Library(),
        'dining_scene': Dining(),
        'kitchen_scene': Kitchen(),
        'solving_scene': Solving(),
        'solved_scene': Solved(),
        'unsolved_scene': Unsolved(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('crime_scene')
a_game = Runner(a_map)
a_game.play()

# limiting line length to 80 characters because ... style, that's why.
