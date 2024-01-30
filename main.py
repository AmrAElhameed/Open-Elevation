import arcpy
from flask import Flask, render_template
import folium

app = Flask(__name__)
@app.route("/")
def home():
  m = folium.Map(location=[28.092569,30.769300],zoom_start=6)
  m.get_root().width = "1000px"
  m.get_root().height = "700px"
  map = m.get_root()._repr_html_()
  return render_template("homepage.html",dom=map)

if __name__ == "__main__":
  app.run(debug=True, port=3000)


