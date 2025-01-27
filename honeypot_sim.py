import socket
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import argparse

class HoneypotSimulator:
    """
    A class to simulate different types of connections and attacks against our honeypot.
    This will help to test the honeypot's logging and response capabilities.
    """

    def __init__(self, target_ip = "127.0.0.1", intensity = "medium"):

        self.target_ip = target_ip
        self.intensity = intensity

        self.target_ports = [21, 22, 23, 25, 80, 443, 3306, 5432]

        self.attack_patterns = {
            21: [
                "USER admin\r\n",
                "PASS admin123\r\n",
                "LIST\r\n",
                "STOR malware.exe\r\n"
            ],
            22: [
                "SSH-2.0-OpenSSH_7.9\r\n",
                "admin:password123\n",
                "root:toor\n"
            ],
            80: [
                "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
                "POST /admin HTTP/1.1\r\nHost: localhost\r\nConstant-Length: 0\r\n\r\n",
                "GET /wp-admin HTTP/1.1\r\nHost: localhost\r\n\r\n"
            ]
        }

        self.intensity_settings = {
            "low":{"max_threads":2, "delay_range":(1,3)},
            "medium":{"max_threads":5, "delay_range":(0.5, 1.5)},
            "high":{"max_threads":10, "delay_range":(0.1,0.5)}
        }