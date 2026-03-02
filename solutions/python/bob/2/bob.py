def response(hey_bob):
    msg = hey_bob.strip()
    if not msg:
        return "Fine. Be that way!"
    if msg.endswith("?") and not msg.isupper():
        return "Sure."
    if msg.isupper() and not msg.endswith("?"):
        return "Whoa, chill out!"
    if msg.isupper() and msg.endswith("?"):
        return "Calm down, I know what I'm doing!"
    return "Whatever."
    
