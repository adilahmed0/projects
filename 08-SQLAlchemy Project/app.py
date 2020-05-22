# import Dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine,reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector = inspect(engine)
inspector.get_table_names()

app = Flask(__name__)

@app.route("/")
def home():
    return("/api/v1.0/precipitation<br/>"
    "/api/v1.0/stations<br/>"
    "/api/v1.0/tobs<br/>"
    "/api/v1.0/2019-01-01<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    first_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>="2018-05-18").all()
    first_dictionary = list(np.ravel(first_results))

    first_dictionary = []
    for temps in first_results:
        temps_dictionary = {}
        temps_dictionary["date"] = Measurement.date
        temps_dictionary["tobs"] = Measurement.tobs
        first_dictionary.append(temps_dictionary)
    return jsonify(first_dict)

@app.route("/api/v1.0/stations")
def stations():
    second_results = session.query(Station.station, Station.name).all()

    second_dictionary = list(np.ravel(second_results))
second_dictionary = []
for station in second_results:
    station_dictionary = {}
    station_dictionary["station"] = Station.station
    station_dictionary["name"] = Station.name
    second_dictionary.append(station_dictionary)
    return jsonify(second_dictionary)

@app.route("/api/v1.0/tobs")

def tobs():
    third_results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date>="2018-05-18").\
            filter(Measurement.date<="2019-05-23").all()
    temporary_dictionary = list(np.ravel(third_results))

third_dictionary = []
for temps in third_results:
    temporary_dictionary = {}
    temporary_dictionary["date"] = Measurement.date
    temporary_dictionary["tobs"] = Measurement.tobs
    third_dictionary.append(temporary_dictionary)
    return jsonify(temporary_dictionary)

@app.route("/api/v1.0/<date>")

def first_start(date):

    fourth_results = session.query((Measurement.date, func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
            filter(Measurement.date)>=date).all()
    temporary_dates = list(np.ravel(fourth_results))
    
    five_dict = []
    for x in fourth_results:

        start_dictionary["Date"] = float(x[0])
        start_dictionary["Avg"] = float(x[1])
        start_dictionary["Min"] = float(x[2])
        start_dictionary["Max"] = float(x[3])
        five_dictionary.append(start_dictionary)
        start_dictionary = {}
        start_dictionary["Date"] = x.Date
        start_dictionary["Avg"] = x.func.avg(Measurement.tobs)
        start_dictionary["Min"] = x.func.min(Measurement.tobs)
        start_dictionary["Max"] = x.func.max(Measurement.tobs)
        five_dictionary.append(start_dictionary)

    return jsonify(five_dictionary)
    return jsonify(temporary_dates)

    
if __name__ == '__main__':
    app.run(debug=True)