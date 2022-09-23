from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


def check_is_valid(cmd):
    if "@" not in cmd:
        raise MustContainAtSymbolError("Email must contain @")
    username, domain = cmd.split("@")
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." not in domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    name, extension = domain.split(".")

    if extension not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    return True


command = input()
domains = {'com', 'bg', 'net', 'org'}
while not command == "End":
    if check_is_valid(command):
        print("Email is valid")

    command = input()
