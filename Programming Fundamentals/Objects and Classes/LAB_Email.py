class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
line = input()
while line != "Stop":
    tokens = line.split()

    sender_name = tokens[0]
    receiver_name = tokens[1]
    content_of_message = tokens[2]

    email = Email(sender_name, receiver_name, content_of_message)
    emails.append(email)

    line = input()

sent_emails = list(map(lambda send_message_index: int(send_message_index), input().split(", ")))

for index in sent_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())

# to_understand
