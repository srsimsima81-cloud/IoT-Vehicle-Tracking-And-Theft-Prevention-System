import folium

m = folium.Map(location=[8.5241, 76.9366], zoom_start=12)

folium.Marker([8.5241, 76.9366], tooltip="Safe Zone").add_to(m)

m.save("outputs/map.html")

print("Map generated!")