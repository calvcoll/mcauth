#!/usr/bin/python

import argparse, urllib2
debug = False

parser = argparse.ArgumentParser(description='Returns a session id from Minecraft auth server')
parser.add_argument('username', metavar='username',
                   help='The username that you log in to Minecraft with!')
parser.add_argument('password', metavar='password',
                   help='The password that you log in to Minecraft with!')

args = parser.parse_args()
if debug:
    print args

response = urllib2.urlopen('http://login.minecraft.net/?user='+args.username + '&password=' + args.password + '&version=12')
html = response.read()
if debug:
    print html

print html.split(':')[-1]
