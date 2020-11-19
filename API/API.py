# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:54:49 2020

@author: Elève
"""

import json
import folium
import requests


tab_couleurs=["#0e7c0a","#c1ff00","#e1ba19","#ff0000"]

#latitude doit être indiquée avant la longitude.
coord_depart=(48.073639, 5.146993)

temps_max=2400 #soit 40 min

intervalle_temps=600 #soit 10 min

#l'API utilise des coordonnées avec la longitude avant la latitude 
coord=[coord_depart[1],coord_depart[0]]
body = {"locations":[coord],
        "range":[temps_max],
        "attributes":["area"],
        "interval":intervalle_temps,
        "location_type":"start",
        "range_type":"time"
        ,"area_units":"m"}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248ec6f505bcef84d86b73ac1494f8efbc1',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/isochrones/foot-hiking',
                     json=body, headers=headers)
print(call.status_code, call.reason)
print(call.text)

#headers = {
#    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
#}
#call = requests.get('https://api.openrouteservice.org/v2/directions/foot-hiking?api_key=5b3ce3597851110001cf6248ec6f505bcef84d86b73ac1494f8efbc1&start=5.146993,48.073639&end=5.139613,48.111006', headers=headers)
#
#print(call.status_code, call.reason)
#print(call.text)

geo=call.text
with open('datas.json','w') as f:
    f.write(geo)
    
with open('datas.json','r') as f:
    datas=json.load(f)
    
folium_map=folium.Map(location=coord_depart,zoom_start=14)
folium.Marker(coord_depart,popup="Lycée").add_to(folium_map)

i=0
for zone in datas["features"]:
    valeur_tps=zone["properties"]["value"]
    print(valeur_tps)
    path_list=[(y,x) for x,y in zone["geometry"]["coordinates"][0]]
    folium.Polygon(path_list,color=tab_couleurs[i]).add_to(folium_map)
    i=i+1
folium_map.save('map.appart.html')