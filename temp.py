"""
Flask-SocketIO entrypoint. Translates socket events <-> Game methods.
"""

from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room


