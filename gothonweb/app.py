from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return render_template('no_session.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            return render_template('no_input.html')
        else:
            currentscene = map.SCENES[session["scene"]]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('unknown_input.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('no_session.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = '112358'

if __name__ == "__main__":
    app.run()


#@app.route('/hello', methods=['POST'])
#def hello_post():
#    usergreet = request.form.get('greet')
#    username = request.form.get('name')
#    if usergreet is None or usergreet == "":
#        usergreet = "Hello"
#    if username is None or username == "":
#        username = "Nobody"
#    greeting = "%s, %s!" % (usergreet, username)
#    return render_template('index.html', greet=greeting)

#@app.route('/hello', methods=['GET'])
#def hello_get():
#    return render_template('hello_form.html')

#if __name__ == "__main__":
#    app.run()

#@app.route('/hello')
#def hello_world():
#    usergreet = request.args.get('greet')
#    username = request.args.get('name')
#    if usergreet is None or usergreet == "":
#        usergreet = "Hello"
#    if username is None or username == "":
#        username = "Nobody"
#    greeting = "%s, %s!" % (usergreet, username)
#    return render_template('index.html', greet=greeting)

#@app.route('/hello')
#def hello_world():
#    greeting = "%s, %s!" % (request.args.get('greet'), request.args.get('name'))
#    return render_template('index.html', greet=greeting)

#@app.route('/')
#def hello_world():
#    greeting = "Hello World"
#    render = render_template('index.html', greet=greeting)
#    return render

#@app.route('/')
#def page_start():
#    starting = "Here's the fancy stuff I can do with HTML: "
#    render = render_template('foo.html'), start=starting)
#    return render
