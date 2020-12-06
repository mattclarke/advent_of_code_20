with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

passports = []
current = ""
for line in puzzle_input:
    if line == "":
        passports.append(current)
        current = ""
        continue
    current += line + " "
passports.append(current.strip())
# print(passports)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

current = []
num_valid = 0

for line in passports:
    print(line)
    for f in fields:
        if f + ":" in line:
            current.append(f)
    if len(current) == len(fields):
        print(f"okay {current}")
        num_valid += 1
    elif len(current) == len(fields) - 1 and "cid" not in current:
        print(f"okay {current}")
        num_valid += 1
    current.clear()

# 230
print(f"answer = {num_valid}")


# Part 2
def check_byr(value):
    return 1920 <= int(value) <= 2002


def check_iyr(value):
    return 2010 <= int(value) <= 2020


def check_eyr(value):
    return 2020 <= int(value) <= 2030


def check_hgt(input):
    value = int(input.replace("cm", "").replace("in", ""))
    if input[-2:] == "cm":
        return 150 <= value <= 193
    elif input[-2:] == "in":
        return 59 <= value <= 76
    return False


def check_hcl(value: str):
    if not value.startswith("#") or len(value) != 7:
        return False
    allowed = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    for c in value[1:]:
        if c not in allowed:
            return False
    return True


def check_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(value):
    return len(value) == 9


def check_cid(value):
    return True


checkers = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
    "cid": check_cid,
}

# All invalid
# PUZZLE_INPUT = """
# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# """

# All valid
# PUZZLE_INPUT = """
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# """

puzzle_input = PUZZLE_INPUT.strip().split("\n")
# print(puzzle_input)

passports = []
current = ""
for line in puzzle_input:
    if line == "":
        passports.append(current)
        current = ""
        continue
    current += line + " "
passports.append(current.strip())
print("\n==================")
print(passports)

total_valid = 0

for passport in passports:
    categories = passport.strip().split(" ")
    num_fields_valid = 1
    for category in categories:
        part = category.split(":")
        if part[0] == "cid":
            # cid is optional
            num_fields_valid -= 1
        if checkers[part[0]](part[1]):
            num_fields_valid += 1
    if num_fields_valid == len(fields):
        total_valid += 1

# 156
print(f"answer = {total_valid}")
