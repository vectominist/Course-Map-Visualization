# Course-Map-Visualization
A simple website for course map visualization 🎓.

## Features

* Easy and fast to generate and deploy a course map website by yourself 🚀.
* Visualizing via an interactive website powered by [Sigma.js](http://sigmajs.org/).
* Supports filtering by chapters or sections 📖.
* Flexible and easy to modify 🛠.
* Demo website: [link](https://google.com)

## Requirements

* Install Web browser ([Firefox](https://www.mozilla.org/en-US/firefox/) is recommended).
* Install [Python3](https://www.python.org/).
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

* **Method 1**
  Open `index.html` with Firefox.
* **Method 2**
  Host from [VSCode](https://code.visualstudio.com/) with [Live Server](https://github.com/ritwickdey/vscode-live-server) and open the website with any Web browser.

### Step 3: Generate your own course map

1. Modify the `data/course.json` file as the following rules:

   ```
   {
     "nodes": [
       {
         "id": <an integer start from zero>,
         "label": "<name of the course module>",
         "chapter": "<chaper name>",
         "url": "<link to the course module>"
       },
       ...
     ],
     "edges": [
       {
         "source": <index of the source node>,
         "target": <index of the target node>
       },
       ...
     ]
   }
   ```
2. Generate `data/data.json` with `generate_json_file.py`:

   ```
   python3 generate_json_file.py data/course.json data/data.json
   ```

<!-- ## Example -->


## Author
[Heng-Jui Chang](https://vectominist.github.io/)  
For any questions, please contact me 😊.