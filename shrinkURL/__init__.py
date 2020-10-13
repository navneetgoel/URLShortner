import logging
from flask import Flask, json, request, redirect, render_template,make_response
from compressURL import compressURL
from functools import wraps
from bernhard import Client
from riemann_wrapper import riemann_wrapper
import urllib.parse

app = Flask(__name__)
shrt = compressURL()
logger = logging.getLogger()

logger.info("Starting the app")
