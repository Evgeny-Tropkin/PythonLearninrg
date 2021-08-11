def check_email(string):
    res = False
    at_count = string.count('@')
    email = string.strip()
    if at_count == 1 and ' ' not in email:
        address, domain = email.split('@')
        passed = ['.' in domain, len(address) > 0, domain[0] != '.']
        if all(passed):
            res = True
        
    return res
