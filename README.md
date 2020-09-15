# Course-Map-Visualization
[![Python version](https://img.shields.io/badge/python-%3E=_3.6-green.svg?style=flat-square)](_blank)
[![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](./LICENSE)  
A simple website for visualizing course maps 🎓🗺.


## Features

* Easy and fast to generate and deploy a course map website by yourself 🚀.
* Visualizing via an interactive website powered by [Sigma.js](http://sigmajs.org/).
* Supports filtering by chapters or sections 📖.
* Flexible and easy to customize 🛠.
* Demo website: [link](https://google.com) (not lauched yet)

## Requirements

* Install Web browser ([Firefox](https://www.mozilla.org/en-US/firefox/) is recommended).
* Install [Python](https://www.python.org/) (>= 3.6).
* Install required python packages for generating and drawing the course map structure:
  ```
  matplotlib
  networkx
  python-igraph
  ```

## Instructions

### Step 1: Download source code

```
git clone https://github.com/vectominist/Course-Map-Visualization.git
```

### Step 2: Open the example with your Web browser

* **Method 1:**
  Open `index.html` with Firefox.
* **Method 2:**
  Host from [VSCode](https://code.visualstudio.com/) with [Live Server](https://github.com/ritwickdey/vscode-live-server) and open the website with any Web browser.

### Step 3: Generate your own course map

1. Modify the `data/course.json` file as the following rules:

   ```
   {
     "category": [
       "<category 1>",
       ...
     ]
     "nodes": [
       {
         "id": <an integer start from zero>,
         "label": "<name of the course module>",
         "category": "<category name>",
         "key": [list of keys (can be empty)],
         "url": "<link to the course module>"
       },
       ...
     ],
     "edges": [
       [<index of the source node>, <index of the target node>],
       ...
     ]
   }
   ```
2. Generate `data/data.json` with `generate_json_file.py`:

   ```
   python3 generate_json_file.py data/course.json data/data.json
   ```
   **Note:** We assume the course map is a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) and thus can be viewed as a *tree-like* structure that can be plotted with the [Reingold-Tilford algorithm](https://reingold.co/tidier-drawings.pdf).

### Step 4: Set colors for different categories (optional)

The color of the nodes and edges are determined by their categoties. The default color for each category is in `color_selection.py`. You may want to customize your colors by modifying:
1. `COLORS`: the color dictionary (default: `matplotlib.colors.CSS4_COLORS`)
2. `DEFAULT_COLORS`: the default color list for each category, which is shown in the following image
<p align="left">
  <img src="images/default_colors.png" width="500">
</p>

Another recommended method for assigning colors to categories is to use the [Colormaps in Matplotlib](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html). The default colormap is `rainbow`, which is shown in the following image
<p align="left">
  <img src="images/rainbow.png" width="500">
</p>


## Author
[Heng-Jui Chang](https://vectominist.github.io/)  
For any questions, please contact me 😊.