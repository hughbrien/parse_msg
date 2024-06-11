

import os

import parse_message_file


def loop_over_files(directory, extension):

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(filepath):
            # Perform your action here (e.g., print the file path)
            print(filepath)
            my_file_name = filepath
            parse_message_file.parse_message_file(my_file_name)



if __name__ == '__main__':
    loop_over_files("/Users/hbrien/Software/appd_alert_outlook_messages",
                    ".msg")
