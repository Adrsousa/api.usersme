from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UsersMe(Resource):
    def get(self):
        return {'hello': 'Aqui serao retornados todos os usuarios'}

api.add_resource(UsersMe, '/Users')

if __name__ == '__main__':
	app.run(debug=True, port=8080) 