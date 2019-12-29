from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", " Malesuada fames ac turpis egestas integer eget aliquet. Tortor id aliquet lectus proin nibh nisl. Rutrum quisque non tellus orci ac auctor augue." ,"Neque viverra justo nec ultrices dui sapien eget mi. Quam quisque id diam vel. In metus vulputate eu scelerisque. Sit amet volutpat consequat mauris nunc. Consectetur lorem donec massa sapien faucibus et. Semper viverra nam libero justo laoreet sit. Habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Ac turpis egestas maecenas pharetra convallis posuere. Malesuada bibendum arcu vitae elementum. Nisl suscipit adipiscing bibendum est ultricies integer. Massa placerat duis ultricies lacus sed turpis tincidunt id aliquet. Scelerisque varius morbi enim nunc faucibus a pellentesque. Ornare aenean euismod elementum nisi quis eleifend quam."]

@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]
   
@app.route("/third")
def third():
    return texts[2]