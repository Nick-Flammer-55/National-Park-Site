"""
version 1.1

@Date: 11/26/2025
"""
import folium
import csv
import webbrowser
import os

# Starts the map at the center of the mainland U.S.
main_map = folium.Map(
    location=(39.833333, -98.583333), # Where the map will be positioned
    zoom_start=3, max_bounds=True, min_zoom=3, max_lat=75, min_lat=-20, max_lon=-60, min_lon=-180, # The bounds of the map
    )

with open('npdata.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    park_list = list(reader)[1:] # Skips the header

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

# Adds markers for each US National Park
def build_map():
    for park in park_list:
        #popup_content = "<a target=\"_blank\" href=https://www.nps.gov/" + park[6] + "/index.htm><button>" + park[0] + "</button></a>"
        popup_content = "<div id=\"sidebar\"><h2>About the park</h2><iframe src=\"https://www.nps.gov/" + park[6] + "/index.htm\" width=\"300%\" height=\"400px\" frameborder=\"0\"></iframe></div>"
        popup = folium.Popup(popup_content, max_width=400)
        folium.Marker(
            location=[float(park[3]), float(park[4])], 
            tooltip=park[0],
            #popup="<a href=https://www.nps.gov/" + park[6] + "/index.htm><button>" + park[0] + "</button></a>"
            popup=popup
        ).add_to(main_map)

    # Saves the completed map as an HTML File
    main_map.save("..\\nps_map.html")

if __name__ == "__main__":
    # Build the map of parks
    build_map()

    # Open file
    file_path = os.path.abspath('..\\nps_map.html')
    url = 'file://' + file_path
    webbrowser.open(url)