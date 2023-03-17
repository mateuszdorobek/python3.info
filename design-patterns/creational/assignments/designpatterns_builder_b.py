"""
* Assignment: DesignPatterns Creational BuilderEmail
* Complexity: easy
* Lines of code: 21 lines
* Time: 21 min

English:
    1. Create class `Email`
    2. Use builder pattern to set:
        a. `recipient: str` verify email address using regex
        b. `sender: str` verify email address using regex
        c. `subject: str` encode to bytes
        d. `body: str` encode to bytes
        e. `attachment: bytes` base64 encoded
    3. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    TODO: Tests
"""
from base64 import b64encode


class Email:
    recipient: str
    sender: str
    subject: str
    body: str
    attachment: bytes


# Solution
class Email:
    recipient: str
    sender: str
    subject: str
    body: str
    attachment: bytes

    def with_recipient(self, recipient):
        self.recipient = recipient
        return self

    def with_sender(self, sender):
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject
        return self

    def with_body(self, body):
        self.body = body
        return self

    def with_attachment(self, attachment):
        self.attachment = b64encode(attachment)
        return self

