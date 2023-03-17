import json
from pickle import TRUE
import instaloader
from random import *


class MyRateController(instaloader.RateController):
    def query_waittime(self, query_type, current_time, untracked_queries=False):
        return 15 + super().query_waittime(query_type, current_time, untracked_queries)

L = instaloader.Instaloader(rate_controller=lambda ctx: MyRateController(ctx))


class account:
    def rotate_accounts(read_from_file= True):
        if read_from_file:
            with open('accounts.json') as f:
                accounts = json.load(f)
                count=0
            for account in accounts:
                count+=1
            num=randrange(count)
            print('Using account num:',num+1)
            user= accounts[num]['user']
            passw= accounts[num]['pass']
            #print (user, passw)
            return user, passw

class login:
    def login():
        USER,PASSWORD= account.rotate_accounts(read_from_file=True)
        L = instaloader.Instaloader()
        #L.load_session_from_file(USER)
        L.login(USER, PASSWORD)
         
        
        return L

