# create3_docs

This repository contains the source code for the iRobot® Create® 3 Educational Robot documentation.
The automatically generated website can be viewed at https://iroboteducation.github.io/create3_docs/

### Build the docs locally

Install required dependencies:

```bash
pip3 install mkdocs
pip3 install mkdocs-material
pip3 -r requirements.txt
```

Optionally, if you desire to generate images of STL models dynamically install:

```bash
pip3 -r model_image_generation.txt
```


Build the documentation locally:

```bash
mkdocs serve
```

Open `http://127.0.0.1:8000/` in a browser to visualize the docs.

### Updating the docs

After commits are pushed to the `main` branch a new build of the website will automatically start.
