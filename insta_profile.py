import instaloader
import json
from utilities import *
from pathlib import *
from flask_restx import Namespace, Resource, Api
from utilities import *
import uuid
import shutil
api= Namespace('profile_dl')

#download all media from a profile
@api.route('/<username>')
class profile_dl(Resource):
    def get(self, username):
        #L=login.login()
        MyRateController(instaloader.RateController)
        id = str(uuid.uuid4())
        posts = instaloader.Profile.from_username(L.context, username).get_posts()
        for post in posts:
            print(post.date)
            L.dirname_pattern = './'+id+'/posts'
            L.download_post(post, username) 
        shutil.make_archive(id, 'zip', id)
        shutil.rmtree(id)

#download posts were a profile is tagged
@api.route('/<username>/tagged')
class profile_dl(Resource):
    def get(self, username):
        #L=login.login()
        MyRateController(instaloader.RateController)
        id = str(uuid.uuid4())
        posts = instaloader.Profile.from_username(L.context, username).get_tagged_posts()
        for post in posts:
            print(post.date)
            L.dirname_pattern = './'+id+'/tagged_posts'
            L.download_post(post, username) 
        shutil.make_archive(id, 'zip', id)
        shutil.rmtree(id)

#download a list of followers
@api.route('/<username>/followers')
class followers_dl(Resource):
    def get(self, username):
        L=login.login()
        MyRateController(instaloader.RateController)
        followers= instaloader.Profile.from_username(L.context, username).get_followers()
        follower_list=[]
        id = str(uuid.uuid4())
        for follower in followers:
            #print(follower)
            follower_list.append(follower)
        Path(id).mkdir(parents=True, exist_ok=True)
        filename= id+"_followers.json"
        with open(id+"/"+filename, "w") as f:
            f.write(json.dumps(follower_list, default=str, indent=4))
        shutil.make_archive(id, 'zip', id) 
        shutil.rmtree(id) 

#download a list of followees
@api.route('/<username>/followees')
class followers_dl(Resource):
    def get(self, username):
        L=login.login()
        MyRateController(instaloader.RateController)
        followees= instaloader.Profile.from_username(L.context, username).get_followees()
        followee_list=[]
        id = str(uuid.uuid4())
        for followee in followees:
            #print(followee)
            followee_list.append(followee)
        Path(id).mkdir(parents=True, exist_ok=True)
        filename= id+"_followee.json"
        with open(id+"/"+filename, "w") as f:
            f.write(json.dumps(followee_list, default=str, indent=4))
        shutil.make_archive(id, 'zip', id) 
        shutil.rmtree(id) 

#download profile stories
@api.route('/<username>/stories')
class stories_dl(Resource):
    def get(self, username):
        L=login.login()
        id = str(uuid.uuid4())
        MyRateController(instaloader.RateController)
        choices = {'stories': True,
                'posts': False,
                'profile_pic': True,
                'raise_errors': True}
        profile = instaloader.Profile.from_username(L.context, username)
        profiles = {profile}
        L.save_metadata = False
        L.dirname_pattern = './'+id+'/stories'
        L.compress_json = False
        L.post_metadata_txt_pattern = ''
        L.storyitem_metadata_txt_pattern = ''
        L.download_profiles(profiles, **choices)
        shutil.make_archive(id, 'zip', id) 
        shutil.rmtree(id)