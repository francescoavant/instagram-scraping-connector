import instaloader
import json
from utilities import *
from pathlib import *
from flask_restx import Namespace, Resource, Api
from utilities import *
import uuid
import shutil

api= Namespace('location_dl')


#download post by location (id location)
@api.route('/<location>')
class location(Resource):
    def get(self,location):
        L=login.login()
        MyRateController(instaloader.RateController)
        id = str(uuid.uuid4())
        L.dirname_pattern = './'+id+'/location_posts'
        L.download_location(location, max_count=5)
        shutil.make_archive(id, 'zip', id)
        shutil.rmtree(id)