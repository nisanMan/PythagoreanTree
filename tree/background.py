# tree\background.py
import cv2 as cv
import numpy as np


class BackgroundDrawer:
    DEFAULT_DAY_COLOR = (250, 240, 153)
    DEFAULT_NIGHT_COLOR = (0, 0, 0)

    def __init__(self, width, height, skyline, day=True,
                 day_color=None, night_color=None):
        self.width = width
        self.height = height
        self.skyline = skyline
        self.day = day
        self.day_color = day_color or self.DEFAULT_DAY_COLOR
        self.night_color = night_color or self.DEFAULT_NIGHT_COLOR

    def draw(self, img):
        if self.day:
            self._draw_day_background(img)
        else:
            self._draw_night_background(img)

    def _draw_day_background(self, img):
        cv.rectangle(img, (0, 0), (self.width, self.skyline), self.day_color, -1)

    def _draw_night_background(self, img):
        cv.rectangle(img, (0, 0), (self.width, self.skyline), self.night_color, -1)

    @staticmethod
    def draw_ground(img, skyline):
        height = img.shape[0]
        for y in range(skyline + 1, height):
            color_ratio = (height - y) / (height - skyline + 1)
            color = (
                int(125 + color_ratio * (150 - 125)),
                int(179 + color_ratio * (255 - 179)),
                int(60 + color_ratio * (70 - 60))
            )
            img[y, :] = color

    @staticmethod
    def create_canvas(width, height):
        return np.zeros((height, width, 3), dtype=np.uint8)

    @staticmethod
    def draw_sun(img, center=(340, 125), size=75, glow=75):
        glow_color = (0, 255, 255)
        cv.circle(img, center, glow, glow_color, -1)
        cv.circle(img, center, size, (33, 222, 255), -1)

    @staticmethod
    def draw_moon_and_stars(
            img,
            moon_center=(700, 225),
            moon_size=55,
            moon_glow=75,
            small_star_count=100,
            big_star_count=7
    ):
        height, width = img.shape[:2]

        # stars small
        rng = np.random.default_rng(seed=42)
        xs = rng.integers(0, width, size=small_star_count)
        ys = rng.integers(0, int(height * 0.8), size=small_star_count)

        img[ys, xs] = (255, 255, 255)

        # big stars
        big_star_centers = [(960, 79), (1345, 240), (205, 52)]
        for center in big_star_centers[:big_star_count]:
            for r in range(11, 4, -1):
                ratio = (11 - r) / 7
                gray = int(ratio * 255)
                cv.circle(img, center, r, (gray, gray, gray), -1)

        # moon glow
        for r in range(moon_glow, moon_glow - 30, -1):
            alpha = (moon_glow - r) / 30
            glow_color = tuple(int(alpha * 255) for _ in range(3))
            cv.circle(img, moon_center, r, glow_color, -1)

        # moon
        cv.circle(img, moon_center, moon_size, (255, 255, 255), -1)
        cv.circle(img, moon_center, moon_size - 10, (245, 255, 255), -1)
