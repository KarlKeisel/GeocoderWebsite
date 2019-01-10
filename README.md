"# GeocoderWebsite" 

Hello everyone!

This app is a ready to deploy website that can take an uploaded .csv file and if it contains an 'Address', 'address', or 'ADDRESS' column, it will then process that through a class that takes that column, and if it contains a valid address (Street, city, state, zip) will then add two new columns to the database named 'Latitude' and 'Longitude'. It will then display your database on the website and allow you to download the new .csv file to allow easier use to use geocoding.

This app works with Flask for website production, geopy for the location part, and of course pandas to open, close and save the DB.

It also possesses all the files needed, that it could be pushed to heroku or the like and it would be ready to work.
