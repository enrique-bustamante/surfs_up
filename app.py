#%%
import datetime as dt
import pandas as pd 
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, extract
from flask import Flask, jsonify, render_template

# %%
# Create the engine for connection
engine = create_engine("sqlite:///hawaii.sqlite")


# %%
# Reflect database into classes 
Base = automap_base()
Base.prepare(engine, reflect=True)

# %%
# Create references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# %%
# Create session link for connection
session = Session(engine)

# %%
# Set up Flask
app = Flask(__name__)

# %%
# Define the routes for the data
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    <br>
    Available Routes:<br>
    <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a><br>
    <a href="/api/v1.0/stations">/api/v1.0/stations</a><br>
    <a href="/api/v1.0/tobs">/api/v1.0/tobs</a><br>
    <a href="/api/v1.0/start/end">/api/v1.0/temp/start/end</a><br>
    <a href="/api/v1.0/june-stats">/api/v1.0/june-stats</a><br>
    <a href="/api/v1.0/dec-stats">/api/v1.0/dec-stats</a><br>
    ''')


# %%
# Create the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# %%
# Create the stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# %%
# Create the temperatures route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps = temps)

# %%
# Create the statistics route
@app.route("/api/v1.0/temp<start>")
@app.route("/api/v1.0/temp<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results= session.query(*sel).\
            filter(Measurement.date >= start)
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
# %%
# Create the June statistical summary route
@app.route("/api/v1.0/june-stats")
def june_stats():
    june_results = session.query(Measurement.date,Measurement.tobs, Measurement.prcp).\
        filter(extract('month',Measurement.date) == 6).all()
    june_df = pd.DataFrame(june_results, columns=['date', 'temperature', 'precipitation'])
    june_df.set_index(june_df['date'], inplace=True)
    june_stats = june_df.describe()
    return june_stats.to_html()

# %%
# Create the December statistical summary route
@app.route("/api/v1.0/dec-stats")
def dec_stats():
    dec_results = session.query(Measurement.date,Measurement.tobs, Measurement.prcp).\
        filter(extract('month',Measurement.date) == 12).all()
    dec_df = pd.DataFrame(dec_results, columns=['date', 'temperature', 'precipitation'])
    dec_df.set_index(dec_df['date'], inplace=True)
    dec_stats = dec_df.describe()
    return dec_stats.to_html()
# %%
type(june_stats)

# %%
