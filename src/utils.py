import re


def sub_to_exec(string, params):
    cmd = re.sub(
        "<.+?>",
        lambda x: params[remove_chars(x.group(0), ["<", ">"])],
        string,
    )
    return cmd.split(" ")


def remove_chars(string, chars):
    to_remove = {c: "" for c in chars}
    return string.translate(str.maketrans(to_remove))


def override(a, b, fmt=None):
    if fmt:
        return {k: b[fmt(k)] if b[fmt(k)] else v for (k, v) in a.items()}
    else:
        return {k: b[k] if b[k] else v for (k, v) in a.items()}
