# Start of Program

def rearrange_name(name):
    import re
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])
