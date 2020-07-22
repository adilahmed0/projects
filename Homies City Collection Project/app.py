# Import MatPlotLib
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import Numpy and Pandas
import numpy as np
import pandas as pd

# Import DateTime
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

###########################################################
# Database Setup
###########################################################
engine = create_engine("sqlite:///Resources/city.sqlite")
connection = engine.connect()

# Declare bases and map class
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# view all of the classes
Base.classes.keys()

# Save references to each table
City = Base.classes.city

###########################################################
# Flask setup
###########################################################
app = Flask(__name__)

###########################################################
# Flask Route
###########################################################
# Home page
# List all routes that are available
@app.route("/")
# def home():
#     return (
#         f"Available Routes:<br/>"
#         f"/api/data"
#     )

# # Convert the query results to a dictionary using date as the key and prcp as the value
# # Return the JSON representation of your dictionary
# @app.route("/api/data")
def data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query results to a dictionary
    results = session.query(City.city,
        City.state,
        City.country,
        City.crime_index,
        City.safety_index,
        City.quality_of_life_index,
        City.purchasing_power_index,
        City.health_care_index,
        City.cost_of_living_index,
        City.traffic_commute_time_index,
        City.price_to_income_ratio,
        City.affordability_index,
        City.lat,
        City.long).\
        order_by(City.city).all()

    session.close()

    # List all
    data = []
    for city, state, country, crime, safety, life, purchasing, health, cost, traffic, price, affordability, lat, long in results:
        data_dict = {}
        data_dict["city"] = city
        data_dict["state"] = state
        data_dict["country"] = country
        data_dict["crime_index"] = crime
        data_dict["safety_index"] = safety
        data_dict["quality_of_life_index"] = life
        data_dict["purchasing_power_index"] = purchasing
        data_dict["health_care_index"] = health
        data_dict["cost_of_living_index"] = cost
        data_dict["traffic_commute_time_index"] = traffic
        data_dict["price_to_income_ratio"] = price
        data_dict["affordability_index"] = affordability
        data_dict["lat"] = lat
        data_dict["long"] = long
        data.append(data_dict)
    
    # Jsonify the data
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)