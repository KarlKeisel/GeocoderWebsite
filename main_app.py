"""
Karl's Geocoding Webapp

This webapp will allow the user to upload a .csv file to a website and take the addresses from the address (or Address)
column and then create two new columns that will display latitude and longitude of the address if available. Then it
will append that data to a new .csv file and allow the user to download it from the webapp, while displaying it
on the website as well. Scroll bar for very long info.

main_app.py will supply code to for the website and html.
geocoder.py will take the address info and generate the Lat and Lon.
"""

from flask import Flask, request, render_template, send_file
from geocoder import GeocoderAdd  # Used to apply geocoding to the db and return the new db
import pandas as pd               # Used to display completed df on website before download
from werkzeug import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success/', methods=["POST"])
def success():
    global info
    if request.method == "POST":
        info = request.files['file']    # Grabs the csv file
        geo = GeocoderAdd(info)  # Creates the object to read csv file
        geo.transform_database()    # Adds lat and long to the csv file
        if geo.geocoded is not None:
            info = geo.geocoded     # Grabs the completed csv file
            # info.save(secure_filename("uploaded_" + info.filename))  # ALWAYS add the secure_filename to this code
            return render_template('success.html', tables=[info.to_html(classes='data')], titles=info.columns.values,
                                   btn='downloader.html')
        else:
            return render_template('index.html',  # Failure text if unsuccessful
                                   text="File does not have the appropriate 'Address' column or is not a .csv!")


@app.route('/downloader/')
def downloader():
    info.to_csv("Geo_Addresses.csv")
    return send_file("Geo_Addresses.csv", attachment_filename="Geo_Addresses.csv", as_attachment=True)

# TODO Create a success page if no errors
# TODO Create download button page, which must also display df table.

# TODO Create main_app connections to html
# TODO Create geocoder (accept a df with address column and return a new df with same info plus lat and lon columns)
# TODO Link main_app to geocoder
# TODO Create heroku app name and upload via git


if __name__ == "__main__":
    app.run(debug=True)
