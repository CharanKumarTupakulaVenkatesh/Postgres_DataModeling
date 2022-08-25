# DROP TABLES

songplay_table_drop = "drop table if exists songplays"

user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays(
songplay_id serial primary key, 
start_time timestamp not null, 
user_id int not null, 
level varchar,
song_id varchar, 
artist_id varchar,
session_id int, 
location varchar,
user_agent varchar);
""")

user_table_create = ("""
create table if not exists users(
user_id int NOT NULL PRIMARY KEY , 
first_name varchar not null, 
last_name varchar,
gender varchar, 
level varchar);
""")

song_table_create = ("""
create table if not exists songs(
song_id varchar NOT NULL PRIMARY KEY, 
title varchar not null, 
artist_id varchar not null, 
year int, 
duration float not null);
""")

artist_table_create = ("""
create table if not exists artists(
artist_id varchar NOT NULL PRIMARY KEY,
name varchar not null, 
location varchar, 
latitude float, 
longitude float);
""")

time_table_create = ("""
create table if not exists time(
start_time timestamp not null PRIMARY KEY,
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
Insert into songplays(
start_time,
user_id,
level,
song_id,
artist_id,
session_id,
location,
user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s) 
on conflict(songplay_id)
do nothing
""")

user_table_insert = ("""
insert into users(
user_id,
first_name,
last_name,
gender,
level) 
values(%s,%s,%s,%s,%s) 
on conflict(user_id) 
do update set level = EXCLUDED.level
""")

song_table_insert = ("""
insert into songs(
song_id,
title,
artist_id,
year,
duration) 
values(%s,%s,%s,%s,%s)
on conflict(song_id)
do nothing
""")

artist_table_insert = ("""
insert into artists(
artist_id,
name,
location,
latitude,
longitude) 
values(%s,%s,%s,%s,%s)
on conflict(artist_id)
do nothing
""")


time_table_insert = ("""
insert into time(
start_time,
hour,
day,
week,
month,
year,
weekday)
values(%s,%s,%s,%s,%s,%s,%s)
on conflict(start_time)\
do nothing
""")

# FIND SONGS

song_select = ("""
SELECT a.song_id,
a.artist_id 
FROM songs a 
JOIN artists b 
ON b.artist_id = a.artist_id 
WHERE title = %s
AND name = %s
AND duration = %s;
""")
#songplay_table_drop = "drop table if exists songplays cascade"
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
