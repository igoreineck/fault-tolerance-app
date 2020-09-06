from datetime import datetime


class MultiCast:
    def __init__(self):
        self.messages = []

    def get_messages(self):
        return self.messages

    def echo(self, message):
        assert message is not None, "You cannot pass empty messages"

        self.messages.append(message)

        return "{message}: {datetime}".format(
            message=message,
            datetime=datetime.now().strftime("%d-%m-%Y - (%H:%M:%S)")
        )
