def show_messages(messages):
    for message in messages:
        print('\t' + message)

def send_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop(0)
        print(f'Sent: {sent_message}')
        sent_messages.append(sent_message)