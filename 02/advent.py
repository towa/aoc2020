def parse_password_policy(policy_string):
    split = policy_string.split(': ')
    password = split[1]
    policy = split[0].split(' ')
    char = policy[1]
    min_ = int(policy[0].split('-')[0])
    max_ = int(policy[0].split('-')[1])

    return password.count(char) >= min_ and password.count(char) <= max_

def parse_password_policy_b(policy_string):
    split = policy_string.split(': ')
    password = split[1]
    policy = split[0].split(' ')
    char = policy[1]
    min_ = int(policy[0].split('-')[0])
    max_ = int(policy[0].split('-')[1])

    return (password[min_ - 1] == char) != (password[max_ - 1] == char)


with open('input') as file:
    lines = file.readlines()
    print(len(list(filter(parse_password_policy, lines))))
    print(len(list(filter(parse_password_policy_b, lines))))
