import re

def pattern_1(string):
    pattern = 'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

def pattern_2(string):
    pattern = 'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

def sequence_3(string):
    pattern = '[a-z]+_[a-z]+'
    ans = re.fullmatch(pattern, string)
    return ans

def sequence_4(string):
    pattern = '[A-Z][a-z]+'
    ans = re.fullmatch(pattern, string)
    return ans

def pattern_5(string):
    pattern = '^a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False

def replace_6(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

def snake_to_camel(string):
    components = string.split('_')
    camel_case = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case

def split_at_uppercase(string):
    return re.findall('[A-Z][a-z]*', string)

def insert_space(string):
    result = re.sub(r'(?<=[a-z])([A-Z])', r' \1', string)
    return result

def camel_to_snake(string):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', string)
    return snake_case.lower()