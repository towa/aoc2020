# Automatically get inputs from AOC and check solutions
import requests
import os

class AdventAPI():
    def __init__(self, token = None):
        if not token:
            token = os.environ.get('AOC_TOKEN')
        self.session_cookie = { 'session' : token }

    def get_input(self, day):
        res = requests.get(
            'https://adventofcode.com/2020/day/{}/input'.format(day),
            cookies=self.session_cookie
        )
        return res.content