

import os

def loop_over_files(directory, extension):

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(filepath):
            # Perform your action here (e.g., print the file path)
            print(filepath)
            # You can open and read the file, or perform other file operations
            # with open(filepath, 'r') as file:
            #     content = file.read()
            #     # Do something with the content

if __name__ == '__main__':
    loop_over_files("/Users/hbrien/Software/appd_alert_outlook_messages",
                    ".msg")
