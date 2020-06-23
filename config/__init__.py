import os
import json

LOCAL_ENV = "config/env_local.json"

if os.path.exists(LOCAL_ENV):
    with open(LOCAL_ENV) as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            os.environ[key] = value
