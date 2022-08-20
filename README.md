# Project: Data Modeling with Postgres

## 1.Introduction
A startup called **Sparkify** wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from **Sparkify** and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.

**song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json**
And below is an example of what a single song file, **TRAABJL12903CDCF1A.json**, looks like.

**{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}**
## Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

**log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json**
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.


If you would like to look at the JSON data within log_data files, you will need to create a pandas dataframe to read the data. Remember to first import JSON and pandas libraries.

**df = pd.read_json(filepath, lines=True)**

**For example, df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True) would read the data file 2018-11-01-events.json.**

# Project Instructions
## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

## Fact Table
****songplays**** - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
## Dimension Tables
**users** - users in the app
user_id, first_name, last_name, gender, level
**songs** - songs in music database
song_id, title, artist_id, year, duration
**artists** - artists in music database
artist_id, name, location, latitude, longitude
**time** - timestamps of records in **songplays** broken down into specific units
start_time, hour, day, week, month, year, weekday
## Project Template
To get started with the project, go to the workspace on the next page, where you'll find the project template files. You can work on your project and submit your work through this workspace. Alternatively, you can download the project template files from the Resources folder if you'd like to develop your project locally.

In addition to the data files, the project workspace includes six files:

**test.ipynb **displays the first few rows of each table to let you check your database.
****create_tables.py**** drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
**etl.ipynb** reads and processes a single file from **song_data** and **log_data** and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
****sql_queries.py**** contains all your sql queries, and is imported into the last three files above.
**README.md** provides discussion on your project.
Project Steps
NOTE: You will not be able to run test.ipynb, etl.ipynb, or etl.py until you have run **create_tables.py** at least once to create the sparkifydb database, which these other files connect to.

## Below are steps you can follow to complete the project:

## Create Tables
Write CREATE statements in **sql_queries.py** to create each table.
Write DROP statements in **sql_queries.py** to drop each table if it exists.
Run **create_tables.py** to create your database and tables.
Run **test.ipynb** to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
Build ETL Processes
Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run **test.ipynb** to confirm that records were successfully inserted into each table. Remember to rerun **create_tables.py** to reset your tables before each time you run this notebook.

## Build ETL Pipeline
Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run **create_tables.py** before running etl.py to reset your tables. Run **test.ipynb**to confirm your records were successfully inserted into each table.

## Run Sanity Tests
When you are satisfied with your work, run the cell under the Sanity Tests section in the **test.ipynb**notebook. The cells contain some basic tests that will evaluate your work and catch any silly mistakes. We test column data types, primary key constraints and not-null constraints as well look for on-conflict clauses wherever required. If any of the test cases catches a problem, you will see a warning message printed in Orange that looks like this:

[WARNING] The **songplays** table does not have a primary key!
You may want to make appropriate changes to your code to make these warning messages go away. The tests below are only meant to help you make your work foolproof. The submission will still be graded by a human grader against the project rubric.