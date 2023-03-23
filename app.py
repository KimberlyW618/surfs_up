# import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# access the SQLite database
engine = create_engine("sqlite:///resources/hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the tables in the database
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes to reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Create a new Flask instance called app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Create a function welcome() with a return statement
# Then add the precipitation, stations, tobs, and temp routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')



##### INFO: When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. This convention signifies that this is version 1 of our application. 


########### PRACTICE CODE ################ 
# import dependencies 
##from flask import Flask

# Create a new Flask instance called app
##app = Flask(__name__)

##### Create Route #####
# First, define the starting point, also known as the root
##@app.route('/')
##def hello_world():
##    return 'Hello world'

# Modify the path that will run app.py file so that we can run our file.
# add to terminal after navigating to the surfs_us file where this app.py is 
    ##export FLASK_APP=app.py
    ##flask run
# Terminal should prvide a web address where the code is writing to. 
