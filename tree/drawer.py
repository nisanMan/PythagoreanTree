# tree\drawer.py
import cv2 as cv
import numpy as np
from typing import List, Literal


class TreeDrawer:
    @staticmethod
    def draw(img: np.ndarray,
             squares: List[np.ndarray],
             start_color: tuple = (255, 0, 0),
             end_color: tuple = (0, 255, 0),
             gradient: Literal['linear', 'reverse', 'constant'] = 'linear') -> None:
        """
        Draw a list of squares onto the image using a color gradient.

        Parameters
        ----------
        img : np.ndarray
            Image to draw on.
        squares : List[np.ndarray]
            List of squares to draw.
        start_color : tuple
            RGB color at the start of the gradient.
        end_color : tuple
            RGB color at the end of the gradient.
        gradient : {'linear', 'reverse', 'constant'}
            Type of gradient:
            - 'linear' : from start_color to end_color.
            - 'reverse': from end_color to start_color.
            - 'constant': all squares in start_color.
        """
        n = len(squares)
        for i, sq in enumerate(squares):
            match gradient:
                case 'linear':
                    t = i / n
                case 'reverse':
                    t = 1 - i / n
                case 'constant':
                    t = 0
                case _:
                    raise ValueError(f"Unsupported gradient: {gradient}")

            color = tuple(int(start_color[j] * (1 - t) + end_color[j] * t) for j in range(3))
            cv.fillPoly(img, [sq], color)
