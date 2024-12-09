def show_messages(messagees):
    """Print each one of messages in a list."""
    for messagee in messagees:
        print(messagee)


def send_messages(msgs, sent_m):
    """Sending our messages."""
    while msgs:
        current_msg = msgs.pop()
        print(f"Sending message: {current_msg}")
        sent_m.append(current_msg)


messages = [
    "Hello, I'm Saman",
    "I'm the king of the world.",
    "bmw's are too expensive",
    "We can have a meeting today in hur cafe.",
    "I send packages for our client",
    "Our company will be glad for hosting you.",
]
sent_messages = []
show_messages(messages)
print()

send_messages(messages[:], sent_messages)

print(f"\n{sent_messages}")
print(f"\n{messages}")
