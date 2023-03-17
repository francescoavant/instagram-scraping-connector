from flask_restx import Api
from insta_profile import api as profile_dl
from insta_location import api as location_dl
from flask import Flask
from flask_restx import Namespace, Resource

app = Flask(__name__)
api = Api(app)


api.add_namespace(profile_dl)
api.add_namespace(location_dl)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
