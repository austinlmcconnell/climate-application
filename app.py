# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

#################################################


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
@app.route("/")
def home():
    print("Retrieving available routes...")
    return "Available routes:
                             "/api/v1.0/precipitation"
                             "/api/v1.0/stations"
                             "/api/v1.0/tobs"
                             "/api/v1.0/<start>"
                             "/api/v1.0/<start>/<end>"
                    
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    print("Retrieving precipitation data from past 12 months...")
    
    date_and_precip = session.query(measurement.date, func.sum(measurement.prcp)).filter(measurement.date >= (dt.date(2017, 8, 23) - dt.timedelta(days=365))).group_by(measurement.date).all()
    
    session.close()
    
    precips = []
    for date, prcp in date_and_precip:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['prcp'] = prcp
        precips.append(precip_dict)
        
    return jsonify(precips)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    print("Retrieving list of stations...")
    
    station_names = session.query(station.name).all()
    
    session.close()
    
    all_names = list(np.ravel(station_names))
    
    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    
    print("Retrieving previous year's temperature observations from most-active station...")
    
    active_stations = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    most_active = active_stations[0][0]
    
    session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.station == most_active).all()
    
    active_last_year = session.query(measurement.date, measurement.tobs).filter(measurement.station == most_active).filter(measurement.date >= (dt.date(2017, 8, 23) - dt.timedelta(days=365))).all()

    session.close()
    
    temperatures = []
    for date, tobs in active_last_year:
        temps_dict = {}
        temps_dict['date'] = date
        temps_dict['tobs'] = tobs
        temperatures.append(temps_dict)
        
    return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)
    
    print("Retrieving minimum, average, and maximum temperatures for your specified start date...")
    
    start_temps =  session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= (dt.date(start))).all()
    
    session.close()
    
    start_temperatures = []
    for date, tobs in start_temps:
        start_temps_dict = {}
        start_temps_dict['date'] = date
        start_temps_dict['tobs'] = tobs
        start_temperatures.append(start_temps_dict)
        
    return jsonify(start_temperatures)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session(engine)
    
    print("Retrieving minimum, average, and maximum temperatures for your specified timeframe...")
    
    start_end_temps =  session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= dt.date(start) <= dt.date(end)).all()
    
    session.close()
    
    start_end_temperatures = []
    for date, tobs in start_end_temps:
        start_end_temps_dict = {}
        start_end_temps_dict['date'] = date
        start_end_temps_dict['tobs'] = tobs
        start_end_temperatures.append(start_temps_dict)
        
    return jsonify(start_end_temperatures)
#################################################
