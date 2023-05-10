# Import Modul Flask
from flask import Flask

# CONSTRUCTOR FLASK TIDAK PERLU DIGANTI
app = Flask(__name__)

# SET ROUTE UNTUK URL YANG DIGUNAKAN PADA WEB
@app.route('/')
# FUNCTION YANG AKAN DIPANGGIL PADA URL /
def hello_world():
    return 'Hello World'

# UNTUK URL YANG MENGGUNAKAN PARAMETER 
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()