def age_assignment(*args, **kwargs):
    # info = {}
    # for name in args:
    #     first_letter = name[0]
    #     info[name] = kwargs[first_letter]
    return kwargs


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
