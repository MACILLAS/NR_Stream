from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "development"
socketio = SocketIO(app)

"""
Available models (scenes) that we can load
"""
idxs = {1, 2, 3}

@app.route('/', methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False) # see if they pressed it

        # Basic Error Checking
        if not name and not code:
            return render_template("home.html", error="Please enter email and model index.", code=code, name=name)
        elif not name:
            return render_template("home.html", error="Please enter email.", code=code, name=name)
        else:
            if not code:
                return render_template("home.html", error="Please enter model index.", code=code, name=name)

        session["name"] = name
        session["code"] = code
        return redirect(url_for("viewer"))

    return render_template("home.html")

@app.route("/viewer")
def viewer():
    code = session.get("code")
    if code is None or session.get("name") is None:
        return redirect(url_for("home"))

    return render_template("viewer.html")

@socketio.on('key_control')
def key_control(key):
    code = session.get("code")
    name = session.get("name")
    print(f'{name} pressed {key["key"]} in model {code}')

@socketio.on('my_event')
def handle_message(data):
    print('received message', data)

@socketio.on("connect")
def connect():
    """
    Socket connection event handler
    Gets the code (model index) and name (email) of the requester.
    :return:
    """
    code = session.get("code")
    name = session.get("name")
    print(f'User {name} has requested model {code}.')

    if not code or not name:
        return
    #TODO: make error checking code more robust
    if int(code) not in idxs:
        return

    #TODO: modifiy this to render from Gaussian Splats
    #TODO: support NeRF studio as well

    # Load initial image
    with open('test_data/celltower_'+code+'.jpg', 'rb') as f:
        img_data = f.read()
    # Send an initial (placeholder) image to canvas 1
    socketio.emit("img1", {'image':img_data})

@socketio.on("disconnect")
def disconnect():
    print('disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)