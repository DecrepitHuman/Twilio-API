from flask import Flask, render_template
#from flask_restplus import Api, Resource
import json

app = Flask(__name__)
#api = Api(app)

@app.route('/')
#class language(Resource):
def get(self):
    return render_template('home.html')

#return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
