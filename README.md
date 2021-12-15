# create3_docs

This repository contains the source code for the iRobot® Create® 3 Educational Robot documentation.
The automatically generated website can be viewed at https://iroboteducation.github.io/create3_docs/

### Build the docs locally

Install required dependencies:

```bash
sudo apt-get update
sudo apt-get -y install python3-pip
sudo apt-get -y install mkdocs
pip3 install mkdocs
pip3 install mkdocs-material
```

Build the documentation locally:

```bash
python3 -m mkdocs serve
```

Open `http://127.0.0.1:8000/` in a browser to visualize the docs.

### Updating the docs

After commits are pushed to the `main` branch a new build of the website will automatically start.

```bash
python3 -m mkdocs gh-deploy
```