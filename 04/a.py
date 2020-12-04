def evaluatePassport(passport):
    for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if key not in passport:
            return False
    return True

def a(input):
    current_passport = {}
    valid_passport_count = 0
    for line in input:
        line = line.strip()
        if len(line) == 0:
            valid_passport_count += evaluatePassport(current_passport)
            current_passport = {}


        else:
            for kp in line.split(' '):
                key, val = kp.split(':')
                current_passport[key] = val
    valid_passport_count += evaluatePassport(current_passport)
    return valid_passport_count
