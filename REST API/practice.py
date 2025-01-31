#Currently practincing on implememting a rest api so we can use the rest api or a maded one for this project!
from flask import Flask 
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data" : "Hello World"}
    def post(self):
        return {"data": "posted"}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)


#https://youtu.be/GMppyAPbLYk?feature=shared
#continue later