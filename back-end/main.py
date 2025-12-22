"""
version 1.3

@Date: 12/22/2025
"""
import folium
import csv
import webbrowser
import os
from flask import Flask, render_template

app = Flask(__name__)


"""
Park Item Key:
[
(0. Name), 
(1. State/Territory full name), 
(2. State/Territory abbreviation), 
(3. Latitude), 
(4. Longitude),
(5. Year Established),
(6. NPS Website index)
]
"""

# Creates the map and adds markers for each US National Park
def build_and_save_map():
    # Starts the map at the center of the mainland U.S.
    main_map = folium.Map(
        location=(39.833333, -98.583333), # Where the map will be positioned
        zoom_start=3, max_bounds=True, min_zoom=3, max_lat=75, min_lat=-20, max_lon=-60, min_lon=-180, # The bounds of the map
        )

    with open('npdata.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        park_list = list(reader)[1:] # Skips the header
        
    for park in park_list:
        #popup_content = "<a target=\"_blank\" href=https://www.nps.gov/" + park[6] + "/index.htm><button>" + park[0] + "</button></a>"
        popup_content = "<div id=\"sidebar\"><h2>About the park</h2><iframe src=\"https://www.nps.gov/" + park[6] + "/index.htm\" width=\"300%\" height=\"400px\" frameborder=\"0\"></iframe></div>"
        popup = folium.Popup(popup_content, max_width=400)
        folium.Marker(
            location=[float(park[3]), float(park[4])], 
            tooltip=park[0],
            popup=popup
        ).add_to(main_map)

    # Saves the completed map as an HTML File
    main_map.save("templates\\nps_map.html")
    # with open(f"nps_map.html", "r", encoding="utf-8") as file:
    #     nps_map_file = file.read()
    # os.remove(f"nps_map.html")
    # return nps_map_file

@app.route('/')
def index():
    return render_template('nps_map.html')

if __name__ == '__main__':
    build_and_save_map()
    app.run(debug=True)