
import extract_msg
import os

def parse_message_file(file_name):
    alert_message = file_name
    print(alert_message)
    msg = extract_msg.Message(alert_message)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = msg.body
    msg.close()

    # Extract the filename
    newfile_name = os.path.basename(file_name + ".txt")


    # Define the text you want to write to the file
    # Open a file in write mode (this will create the file if it doesn't exist)
    with open("./output_files/" + newfile_name, "w") as file:
        # Write the text to the file
        file.write('SENDER: {}'.format(msg_sender))
        file.write('SENT_ON: {}'.format(msg_date))
        file.write('SUBJECT: {}'.format(msg_subj))
        file.write('BODY: {}'.format(msg_message))



if __name__ == '__main__':
    my_file = "/Users/hbrien/Software/appd_alert_outlook_messages/Warning events detected for Register Email Alerts! (995).msg"
    parse_message_file(my_file)