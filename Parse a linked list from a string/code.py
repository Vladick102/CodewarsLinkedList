def linked_list_from_string(s):
    if isinstance(s, str):
        s = s.split(" -> ")
    if len(s) > 1:
        n = s[0]
        s = s[1:]
    else:
        return
    return Node(int(n), linked_list_from_string(s))
