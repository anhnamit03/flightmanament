import json, os
from FlightManament import app, db
from FlightManament.models import *
import hashlib
from datetime import datetime
from sqlalchemy.orm import aliased
from geopy.distance import geodesic

