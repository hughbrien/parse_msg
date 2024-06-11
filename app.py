
import extract_msg

def parse_file(file_name):
    alert_message = file_name
    print(alert_message)
    msg = extract_msg.Message(alert_message)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = msg.body
    msg.close()
    print('Sender: {}'.format(msg_sender))
    print("")
    print('Sent On: {}'.format(msg_date))
    print("")
    print('Subject: {}'.format(msg_subj))
    print("")
    print('Body: {}'.format(msg_message))

if __name__ == '__main__':
    my_file = "/Users/hbrien/Software/appd_alert_outlook_messages/Warning events detected for Register Email Alerts! (995).msg"
    parse_file(my_file)