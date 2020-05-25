from flask import Flask
from flask_restplus import Api, Resource, fields
from twilio.rest import Client
import json
import os

# API contents : 14
# Routes : 20

#Initiating Flask_RestPlus
app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language' : fields.String('The language.')}) #, 'id' : fields.Integer('ID')

#API contents
languages = []
python = {'language' : 'Python', 'id' : 1}
languages.append(python)

#Looking for "language" route
@api.route('/language')
class Language(Resource):

    @api.marshal_with(a_language, envelope='the_data')
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result' : 'Language added'}, 201

class data():
    contents = {
    "numbers": ["0826161123"],
    "message": "Collecting stats for nerds.."
    }

#Interfacing Twilio
class Twilio():
    #Data vars
    numbers = data.contents['numbers']
    message = data.contents['message']

    #Twilio vars
    account_sid = "################"
    auth_token = "#########"
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"{numbers}",
            message_service_sid="#################",
            to=f"{numbers}"
        )
    print(message.sid)

if __name__ == '__main__':
    app.run(debug=True)
