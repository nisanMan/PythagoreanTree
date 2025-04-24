# tree/scene_generator.py
import cv2 as cv
from tree.background import BackgroundDrawer
from tree.drawer import TreeDrawer


def generate_scene(day: bool, with_sun: bool, with_moon: bool, text: str, filename: str, trees: list[dict] = None, WIDTH: int = 1500, HEIGHT: int = 1000):
    if trees is None:
        trees = []
    SKYLINE = int(HEIGHT * 0.8)
    img = BackgroundDrawer.create_canvas(WIDTH, HEIGHT)

    # רקע
    bg = BackgroundDrawer(WIDTH, HEIGHT, SKYLINE, day=day)
    bg.draw(img)
    bg.draw_ground(img, SKYLINE)

    if day and with_sun:
        bg.draw_sun(img)
    elif not day and with_moon:
        bg.draw_moon_and_stars(img)

    # trees
    drawer = TreeDrawer()
    for t in trees:
        drawer.draw(
            img,
            t["tree"],
            start_color=t["start_color"],
            end_color=t["end_color"],
            gradient=t["gradient"]
        )

    # text
    font = cv.FONT_HERSHEY_TRIPLEX
    cv.putText(img, text, (25, 590), font, 2, (245, 255, 245), 2)

    # save
    cv.imwrite(filename, img)
