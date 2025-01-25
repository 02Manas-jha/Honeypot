import socket
import sys
import datetime
import json
import threading
from pathlib import Path

LOG_DIR = Path("honeypot_logs")
LOG_DIR.mkdir(exist_ok=True)

