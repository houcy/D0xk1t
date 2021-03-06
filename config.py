############################################
# D0xk1t Flask Configuration File.
# Note: Since D0xk1t is not an actual deployed web application, but rather a
# self-hosted webapp, you may leave these options as they are if you are just 
# using D0xk1t on a home machine and on a local area network. 
#
# HOWEVER!!!! If you decide to use something like ngrok or cloud-based web hosting,
# it is absolutely necessary that you look through these configurations and change
# them according to the comments!
############################################

# Enabling CSRF for WTForms! Leave this be, since you really won't be screwing
# around with the forms
WTF_CSRF_ENABLED = True

# Enter your Google Maps API Key here!
GOOGLEMAPS_API_KEY = "AIzaSyCk5ZBJ0IyhfbI2ENGCzun0DcA3abTtQ_I"

# Time to check for active users for Redis Server
ONLINE_LAST_MINUTES = 5

# If you are planning to host this on a cloud-based service or some sort of 
# server that is accessible to the Internet, it is ESSENTIAL that you change the 
# secret key. 

SECRET_KEY = 'SECRET_KEY_HERE'

# The USER_LOGIN and USER_PASSWORD fields are utilized so that the Flask application
# can severless-ly authenticate by comparing with these two values. If deployed to the
# Internet, CHANGE THESE, otherwise users will be able to login onto your instance 
# with these default credentials.

USER_LOGIN = "hackerman"
USER_PASSWORD = "password"

