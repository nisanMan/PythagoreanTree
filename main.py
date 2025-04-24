# main.py
import numpy as np
import cv2 as cv
from tree.generator import TreeGenerator
from tree.drawer import TreeDrawer
from tree.background import BackgroundDrawer
from tree.scene_generator import generate_scene

WIDTH, HEIGHT = 1200, 630
SKYLINE = int(HEIGHT * 0.8)

if __name__ == "__main__":
    tree_gen = TreeGenerator()
    scene1_trees = [
        {
            "tree": tree_gen.generate(300, SKYLINE, 61, np.pi / 2, np.pi / 5, 12),
            "start_color": (255, 0, 0),
            "end_color": (0, 255, 0),
            "gradient": "linear"
        },
        {
            "tree": tree_gen.generate(900, SKYLINE, 90, np.pi / 2, np.pi / 3.6, 12),
            # "start_color": (0, 0, 255),
            # "end_color": (255, 255, 0),
            "start_color": (255, 0, 0),
            "end_color": (0, 255, 150),
            "gradient": "reverse"
        },
        # {
        #     "tree": tree_gen.generate(600, SKYLINE, 70, np.pi / 2, np.pi / 3, 11),
        #     "start_color": (255, 165, 0),
        #     "end_color": (34, 139, 34),
        #     "gradient": "constant"
        # }
    ]

    scenes = [
        {"day": True,  "sun": True,  "moon": False, "text": "OpenCV and NumPy Explorer",        "file": "scene_day_sun.png"},
        {"day": False, "sun": False, "moon": True,  "text": "OpenCV and NumPy Explorer",     "file": "scene_night_moon.png"},
        {"day": True,  "sun": False, "moon": False, "text": "Cloudy Day",       "file": "scene_day_cloudy.png"},
        {"day": False, "sun": False, "moon": False, "text": "Dark Night",       "file": "scene_night_dark.png"},
    ]

    for scene in scenes:
        generate_scene(
            day=scene["day"],
            with_sun=scene["sun"],
            with_moon=scene["moon"],
            text=scene["text"],
            filename=fr"output\{scene['file']}",
            trees=scene1_trees,
            WIDTH=WIDTH,
            HEIGHT=HEIGHT
        )

    print(": ) finished")
