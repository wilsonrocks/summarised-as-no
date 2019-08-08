from quickstart import service

from datetime import datetime
from email.mime.text import MIMEText
import base64
from secrets import EMAIL_ADDRESS


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = sender
    message['from'] = to
    message['subject'] = subject
    return {
        'raw': base64.urlsafe_b64encode(
            message.as_string().encode()).decode()
    }


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message


def send_mail(text):
    send_message(
        service,
        'me',
        create_message(
            EMAIL_ADDRESS,
            EMAIL_ADDRESS,
            f'Questions summarised as No {datetime.today().strftime("%d-%m-%Y")}',
            text,
        ),
    )
