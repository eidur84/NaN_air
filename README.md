# NAMS: NaN Air Management System

<dl>
  <dt>Hópur 49:</dt>
  <dd>Daníel Páll Smárason,</dd>
  <dd>Eiður Ágúst Egilsson,</dd>
  <dd>Logi Eyjólfsson,</dd>
  <dd>Pétur Daníel Þórðarson</dd>
</dl>

Verkefni í 3. vikna verklegum kúrs við HR, haust 2019.

# About
NAMS is a system for managing the employees, airplanes, destinations and flights of the fictional airline NaN Air.

** *For best experience run NAMS on Mac or Linux.* **
# How to run NAMS
In a terminal on Mac/Linux ([or Anaconda powershell if on Windows](https://docs.anaconda.com/anaconda/install/windows/)):  
cd to the NAMS directory.  
In the NAMS directory is a small python script which starts NAMS.  
Type in the terminal:
```
python3 run.py
```

# System explanation

## User Interface
The program starts by running the main() function in the class UILayer which is the main program loop. The program keeps track of where the user is by using a list called path. Page names are appended to the list and popped off it when a user goes back a page. Therefore the path list always contains the shortest route from the front page to a users current page. The variable state is the name of the current page.

There are three main different types of pages in NAMS, each handled by a different class in the view/UI layer:

The most simple pages, static pages, such as the front page are handled by the **StaticOptions** class. The class reads a text from a txt file, kept in `view/pages/`, displays it on screen and waits for user input.

When a page calls for displaying a list it is handled by the **Pager** class. It receives a dictionary with a key "data" mapped to a list of object instances. The objects all need to have the function short_display(), which should return a string with necessary information regarding the instance. Pager also reads text from a txt file and displays it. The user can then page forwards or backwards (in some cases by date) and see other instances.

When displaying a form for a user to fill out or change, the **Form** class is called upon. It prints a frame for the form fields, goes through them one-by-one and gets user input. It automatically updates the page when information is entered. The user can choose to keep information unchanged by entering nothing or leave the form at any time by entering "0".

## Model Classes
Instances of objects such as the Pager displays and the Form creates are the system's model classes. They are kept in the aptly named `model_classes` folder.
