# -*- coding: utf-8 -*-

import base64
import requests
import datetime


class LoginCreds:
    
    def __init__(self, app_token, consumer_key, consumer_secret):
        self.app_token = str(app_token)
        self.consumer_key = str(consumer_key)
        self.consumer_secret = str(consumer_secret)
    
    def call_api(self, username, password):
        """ Generate basic authorization token """
        combo = self.consumer_key + ':' + self.consumer_secret
        basic_authorization_token = base64.b64encode(combo.encode('utf-8'))
        
        """ Post parameters for API call """
        headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic ' + basic_authorization_token.decode('utf-8')}
        body = {
        'grant_type':'password',
        'username': str(username),
        'password': str(password),
        'scope':'PRODUCTION'}
        
        """ Make the API call """
        url = 'https://api.stubhub.com/login'
        return requests.post(url, headers=headers, data=body)
    
    def access_token(self, username, password):
        """ Generate basic authorization token """
        combo = self.consumer_key + ':' + self.consumer_secret
        basic_authorization_token = base64.b64encode(combo.encode('utf-8'))
        
        """ Post parameters for API call """
        headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic ' + basic_authorization_token.decode('utf-8')}
        body = {
        'grant_type':'password',
        'username': str(username),
        'password': str(password),
        'scope':'PRODUCTION'}
        
        """ Make the API call """
        url = 'https://api.stubhub.com/login'
        r = requests.post(url, headers=headers, data=body)
        token_respoonse = r.json()
        return token_respoonse['access_token']
    
""" Use the access token from function LoginCreds.access_token, find events"""
def pull_eventids(access_token, nWeeks = 3):
    if int(nWeeks > 3):
        nWeeks = 3
    else:
        nWeeks = int(nWeeks)
    
    inventory_url = 'https://api.stubhub.com/search/catalog/events/v3'
    headers['Authorization'] = 'Bearer ' + access_token
    headers['Accept'] = 'application/json'
    headers['Accept-Encoding'] = 'application/json'
    
    """ Create the raw dates """
    today = datetime.datetime.now()
    nweeks = today + datetime.timedelta(weeks = nWeeks)
    """ Format correctly """
    today = today.strftime('%Y-%m-%d')
    nweeks = nweeks.strftime('%Y-%m-%d')
    daterange = today + 'T00:00 TO ' + nweeks + 'T23:59'