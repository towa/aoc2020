# Automatically get inputs from AOC and check solutions
import requests

class AdventAPI():
    def __init__(self, token):
        self.session_cookie = { 'session' : token }

    def get_input(self, day):
        res = requests.get(
            'https://adventofcode.com/2020/day/{}/input'.format(day),
            cookies=self.session_cookie
        )
        return res.content