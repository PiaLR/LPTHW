from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    resp = client.post('/game') # user POST, but probice no data
    assert_response(resp, contains="You Died!")

    # Go to anohter scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there go to yet anohter scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")

    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': '2'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You Made It!")

    testdata = {'userinput': 'x'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You Died!")
