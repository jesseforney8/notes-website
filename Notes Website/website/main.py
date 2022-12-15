from __init__ import create_app

app = create_app()

#only if you run this file, it will run the web server
if __name__ == '__main__':

    #debug reruns web server when changes are made
    app.run(debug=True)