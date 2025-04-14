# tree\generator.py
import numpy as np
from typing import List, Tuple


class TreeGenerator:
    """
    Generates a Pythagorean Tree represented as a list of squares.
    Each square is a NumPy array of shape (4, 1, 2) for OpenCV.
    """

    def generate(self,
                 x: float,
                 y: float,
                 side_length: float,
                 angle: float,
                 branch_angle: float,
                 depth: int) -> List[np.ndarray]:
        """
        Generate a list of squares representing a Pythagorean Tree.

        Parameters
        ----------
        x : float
            X-coordinate of the initial square's bottom-left corner.
        y : float
            Y-coordinate of the initial square's bottom-left corner.
        side_length : float
            Side length of the initial square.
        angle : float
            The angle between the left and right branches (or grond)
        branch_angle : float
            The constant angle between the left and right branches (the triangle on top of the square).
        depth : int
            Recursion depth. Must be >= 1.

        Returns
        -------
        List[np.ndarray]
            A list of squares, each as a NumPy array of shape (4, 1, 2).

        Raises
        ------
        ValueError
            If depth <= 0 or side_length <= 0.
        """
        if depth <= 0 or side_length <= 0:
            raise ValueError("depth and side_length must be greater than 0")

        squares = []
        stack: List[Tuple[float, float, float, float, int]] = [(x, y, side_length, angle, depth)]

        while stack:
            x, y, side, angle, depth = stack.pop()
            square = self._create_square(x, y, side, angle)
            squares.append(square)

            if depth > 1:
                x3, y3 = square[3, 0]
                next_x, next_y = self._compute_branch_joint(x3, y3, side, angle, branch_angle)

                # Right branch
                right_side = side * np.sin(branch_angle)
                right_angle = angle - branch_angle + np.pi / 2
                stack.append((next_x, next_y, right_side, right_angle, depth - 1))

                # Left branch
                left_side = side * np.cos(branch_angle)
                left_angle = angle - branch_angle
                stack.append((x3, y3, left_side, left_angle, depth - 1))

        return squares

    @staticmethod
    def _create_square(x: float, y: float, side: float, angle: float) -> np.ndarray:
        """
        Compute the four corner points of a square given its bottom-left corner,
        side length, and rotation angle.

        Parameters
        ----------
        x : float
            X-coordinate of the bottom-left corner.
        y : float
            Y-coordinate of the bottom-left corner.
        side : float
            Length of the side of the square.
        angle : float
            Rotation angle of the square in radians.

        Returns
        -------
        np.ndarray
            A NumPy array of shape (4, 1, 2) containing the square's corner points,
            suitable for OpenCV drawing.
        """
        dx = side * np.sin(angle)
        dy = side * np.cos(angle)

        x1, y1 = x + dx, y - dy
        x2, y2 = x + dx - dy, y - dy - dx
        x3, y3 = x - dy, y - dx

        return np.array([[x, y], [x1, y1], [x2, y2], [x3, y3]],
                        dtype=np.int32).reshape((-1, 1, 2))

    @staticmethod
    def _compute_branch_joint(x: float, y: float,
                              side: float, angle: float,
                              branch_angle: float) -> tuple[float, float]:
        """
        Calculate the starting point of the right branch (joint between left and right squares)
        based in the top-left corner of the current square.

        Parameters
        ----------
        x : float
            X-coordinate of the top-left corner of the current square.
        y : float
            Y-coordinate of the top-left corner of the current square.
        side : float
            Side length of the current square.
        angle : float
            Current rotation angle in radians.
        branch_angle : float
            The branching angle between the two child squares.

        Returns
        -------
        tuple[float, float]
            Coordinates (x, y) of the joint point between the left and right branches.
        """
        dx = side * np.cos(branch_angle) * np.sin(angle - branch_angle)
        dy = side * np.cos(branch_angle) * np.cos(angle - branch_angle)

        return x + dx, y - dy
