# NishyAnime 2.1

Python-based, customizable list to keep track of your shows, and link them to your favorite websites to watch them.

## Features
- CSV-based list where you can index anime with their name, a link to a website, and a status: Plan to watch, Watching, or Watched.
- Easy editing of the list with simple interface.
- 3 base themes, and a customizable one, by changing the json.
  - 1 : Purple
  - 2 : Blue
  - 3 : Orange
  - 0 : Custom
- Option to sort by status in the json

## Install
Just download the latest build in the releases, depending on your OS. The app will initialize with default settings when first ran.

## Build
To build the app, you will need the following requirements:

### Debian/Ubuntu-based distro
Requirements:
```
sudo apt install python3 python3-pip
```
As well as the python modules:
```
pip install pyside6 cx_freeze
```
Then you can either run the app by running:
```
python3 main.py
```
Or create an executable by running:
```
python3 setup.py build
```
