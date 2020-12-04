def isInt(i):
    try:
        int(i)
        return True
    except:
        return False

def evaluatePassport(passport):
    # print(passport)
    if 'byr' not in passport or len(passport['byr']) < 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        # print('a')
        return False
    if 'iyr' not in passport or len(passport['iyr']) < 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        # print('b')
        return False
    if 'eyr' not in passport or len(passport['eyr']) < 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        # print('c')
        return False
    if 'hgt' not in passport or ('cm' not in passport['hgt'] and 'in' not in passport['hgt']):
        # print('d')
        return False
    if 'cm' in passport['hgt']:
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            # print('e')
            return False
    if 'in' in passport['hgt']:
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            # print('f')
            return False
    if 'hcl' not in passport or passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
        # print('g')
        return False
    for c in passport['hcl'][1:]:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            # print('h')
            return False
    if 'ecl' not in passport or passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        # print('i')
        return False
    if 'pid' not in passport or len(passport['pid']) < 9:
        # print('j')
        return False
    for c in passport['pid']:
        if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

def b(input):
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
                if key in current_passport:
                    print("oh shit key already present")
                current_passport[key] = val
    # valid_passport_count += evaluatePassport(current_passport)
    return valid_passport_count
