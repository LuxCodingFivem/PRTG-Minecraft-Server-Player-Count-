"""
My Python Script

Copyright (c) 2024 Liam Weckbecker

This script is licensed under the MIT License.
For full details, see the LICENSE file in the repository.
"""

# Lib for requesting minecraft server data 
from mcstatus.server import JavaServer

# Libs to get variabels from PRTG and converting to JSON
import sys
import json

# Libs from PRTG to create the Custom Sensor 
from paesslerag_prtg_sensor_api.sensor.result import CustomSensorResult
from paesslerag_prtg_sensor_api.sensor.units import ValueUnit

# Create the Translation 
locale = 'en'

translation = {
    'de': {
        'limit_error_msg': 'die Slots gehen blad aus.',
    },
    'en': {
        'limit_error_msg': 'the slots are running out.',
    },
    'sp': {
    'limit_error_msg': 'los espacios se están agotando.',
    },
    'fr': {
        'limit_error_msg': 'les créneaux se remplissent rapidement.',
    },
    'it': {
        'limit_error_msg': 'gli slot stanno per finire.',
    },
    'pt': {
        'limit_error_msg': 'os slots estão se esgotando.',
    },
    'zh': {
        'limit_error_msg': '名额即将用完。',
    },
    'ja': {
        'limit_error_msg': 'スロットが間もなく埋まります。',
    },
    'ru': {
        'limit_error_msg': 'слоты заканчиваются.',
    },
    'tr': {
        'limit_error_msg': 'slotlar tükenmek üzere.',
    },
    'nl': {
        'limit_error_msg': 'de slots raken bijna op.',
    }
}

# Request the Variables and format them 
data = json.loads(sys.argv[1])
params = data["params"].split(", ")

# Defining the variables
SERVER_IP = params[0]
SERVER_PORT = params[1]
SERVER_MAX_PLAYER_TO_ERROR = params[2]
SERVER_NAME = params[3]
SERVER_ADDRESSE = f"{SERVER_IP}:{SERVER_PORT}" 

Player_Online = 0

# Connect to the Minecraft server and get the current players 
server = JavaServer.lookup(SERVER_ADDRESSE)
status = server.status()
Player_Online = status.players.online

# Create the Custom sensor and print them 
csr = CustomSensorResult(text='')

csr.add_primary_channel(name=SERVER_NAME,
                        value=Player_Online,
                        unit=ValueUnit.COUNT,
                        is_float=False,
                        is_limit_mode=True,
                        limit_max_error=SERVER_MAX_PLAYER_TO_ERROR,
                        limit_error_msg=translation[locale]['limit_error_msg'])

print(csr.json_result)