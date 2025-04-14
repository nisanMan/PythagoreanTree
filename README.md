# Pythagorean Tree Generator

## Overview

This project generates visual scenes containing Pythagorean trees, using **OpenCV** and **NumPy**. Each scene can include a sky, earth, sun, moon, and stars, and multiple fractal trees with customizable colors and styles.

## Project Structure


```
PythagoreanTree/
├── main.py
├── tree/
│   ├── __init__.py
│   ├── generator.py
│   ├── drawer.py
│   ├── background.py
│   └── scene_generator.py
├──output/
│   ├── output.png
├── requirements.txt
├──README.md
└──.gitignore
```


## Libraries

- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

## Requirements

- Python 3.x
- Install dependencies with:

```bash
pip install -r requirements.txt
```

## Example .png Output

 <p float="left">
  <img src="output/Pythagorean treeb.png" alt="Tree Base" width="300"/>
  <img src="output/scene_day_sun.png" alt="Sunny Scene" width="300"/>
</p>


## Usage
To generate the Pythagorean tree, simply run:
```bash
python main.py
```
This will generate multiple images with different background 

### settings and tree designs.

Tree Customization
Each tree can be configured using the following parameters in `tree_gen.generate(...)`:
```python
generate(x, y, length, angle, branch_angle, depth)
```
### Tree Generation Parameters

- `x, y`: starting position of the tree  
- `length`: length of the base square  
- `angle`: starting angle (usually `π/2`)  
- `branch_angle`: angle between branches (e.g., `np.pi / 4`)  
- `depth`: recursion depth (e.g., `10`)  

### Tree Styling

Each tree dictionary also supports:

- `start_color`: RGB tuple for the base color  
- `end_color`: RGB tuple for the top color  
- `gradient`: one of `"linear"`, `"reverse"`, `"constant"`  

### Scene Configuration

Each scene is defined by a dictionary like:

```python
{
    "day": True or False,            # Background color (day/night)
    "sun": True or False,            # Show sun
    "moon": True or False,           # Show moon and stars
    "text": "Scene title",           # Text label
    "file": "output_file.png"        # Output file name
}
```

### generator.py
<img src="output\Screenshot 2025-04-14 221645.png" alt="Alt Text" width="300">

