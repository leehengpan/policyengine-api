"""
This is the main Flask app for the PolicyEngine API.
"""

print(f"Initialising API...")

import flask
from flask_cors import CORS

# Endpoints

from .endpoints import get_home, get_metadata, get_household, post_household, get_policy, set_policy, get_policy_search, get_household_under_policy, get_calculate, get_economic_impact

app = application = flask.Flask(__name__)

CORS(app)

app.route("/", methods=["GET"])(get_home)

app.route("/<country_id>/metadata", methods=["GET"])(get_metadata)

app.route("/<country_id>/household/<household_id>", methods=["GET"])(
    get_household
)

app.route("/<country_id>/household", methods=["POST"])(post_household)

app.route("/<country_id>/policy/<policy_id>", methods=["GET"])(get_policy)

app.route("/<country_id>/policy", methods=["POST"])(set_policy)

app.route("/<country_id>/policies", methods=["GET"])(get_policy_search)

app.route(
    "/<country_id>/household/<household_id>/policy/<policy_id>", methods=["GET"]
)(get_household_under_policy)

app.route(
    "/<country_id>/calculate", methods=["POST"]
)(get_calculate)

app.route(
    "/<country_id>/economy/<policy_id>/over/<baseline_policy_id>", methods=["GET"]
)(get_economic_impact)

print(f"API initialised.")