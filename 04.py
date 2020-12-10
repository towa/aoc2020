from advent import AdventAPI

class Passport():
    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    def __init__(self, passport_string):
        self.passdict = dict([(p.split(':')[0], p.split(':')[1])
            for p in
            passport_string.split()
            if len(p.split(':')) > 1
        ])

    def __str__(self):
        return str(self.passdict)
    
    def is_valid(self):
        return [ k  for k in self.keys if k in self.passdict.keys()] == self.keys

    def byr_is_valid(self):
        byr = int(self.passdict.get('byr'))
        return byr >= 1920 and byr <= 2002

    def iyr_is_valid(self):
        iyr = int(self.passdict.get('iyr'))
        return iyr >= 2010 and iyr <= 2020

    def eyr_is_valid(self):
        eyr = int(self.passdict.get('eyr'))
        return eyr >= 2020 and eyr <= 2030

    def hgt_is_valid(self):
        hgt = self.passdict.get('hgt')
        try:
            hgt_int = int(hgt[:-2])
        except ValueError:
            return False
        if hgt.endswith('in'):
            return hgt_int >= 59 and hgt_int <= 76
        elif hgt.endswith('cm'):
            return hgt_int >= 150 and hgt_int <= 193
        return False

    def hcl_is_valid(self):
        hcl = self.passdict.get('hcl')
        try:
            int(hcl[1:], 16)
        except ValueError:
            return False
        return len(hcl) == 7 and hcl.startswith('#')

    def ecl_is_valid(self):
        ecl = self.passdict.get('ecl')
        return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def pid_is_valid(self):
        pid = self.passdict.get('pid')
        try:
            int(pid)
        except ValueError:
            return False
        return len(pid) == 9

    def is_valid_b(self):
        return self.is_valid() \
            and self.byr_is_valid() \
            and self.iyr_is_valid() \
            and self.eyr_is_valid() \
            and self.hgt_is_valid() \
            and self.hcl_is_valid() \
            and self.ecl_is_valid() \
            and self.pid_is_valid()


a = AdventAPI()
keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]
passports = [Passport(p) for p in a.get_input(4).decode().split('\n\n')]

valid_passports = [ p for p in passports if p.is_valid()]
valid_passports = [ p for p in passports if p.is_valid_b()]
print(len(valid_passports))


