import tkinter as tk
from tkinter import filedialog
from tkinterweb import HtmlFrame
import folium
import xml.etree.ElementTree as ET

# Funktioner för att parsar XML och skapa kartan
def parse_field_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    fields = []
    for field in root.findall('field'):
        field_id = field.find('id').text
        name = field.find('name').text
        polygon = field.find('coordinates/polygon').text
        coords = polygon.replace("POLYGON((", "").replace("))", "").split(", ")
        lat_lon_pairs = [(float(coord.split()[1]), float(coord.split()[0])) for coord in coords]
        fields.append({"id": field_id, "name": name, "coordinates": lat_lon_pairs})
    return fields

def create_map(fields):
    m = folium.Map(location=[56.0, 13.0], zoom_start=10)
    for field in fields:
        folium.Polygon(
            locations=field["coordinates"],
            color="blue",
            weight=2,
            fill=True,
            fill_color="cyan",
            fill_opacity=0.4,
            popup=field["name"]
        ).add_to(m)
    return m

def display_map(root, fields):
    field_map = create_map(fields)
    field_map.save("field_map.html")
    map_frame = HtmlFrame(root, horizontal_scrollbar="auto")
    map_frame.load_file("field_map.html")
    map_frame.pack(fill="both", expand=True)

def load_xml_and_display_map():
    xml_file = filedialog.askopenfilename(title="Välj XML-fil", filetypes=[("XML files", "*.xml")])
    if xml_file:
        fields = parse_field_data(xml_file)
        display_map(root, fields)

# Huvudfönster för GUI:t
root = tk.Tk()
root.title("Fältkarta")
root.geometry("800x600")

# Knapp för att ladda XML och visa kartan
load_button = tk.Button(root, text="Ladda XML-fil och Visa Karta", command=load_xml_and_display_map)
load_button.pack()

root.mainloop()