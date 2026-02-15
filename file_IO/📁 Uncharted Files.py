import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sent_message.txt')

sent_message = 'Hey there! This is a secret message.'

with open(file_path, 'w') as file:
    file.write(sent_message)

with open(file_path, 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)
    
    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'

    # Truncate the file to remove the original message
    file.truncate(len(unsent_message))

    # Write the modified message to the file
    file.write(unsent_message)

# Display the modified message
print('Original Message:', original_message)
print('Unsent Message:', unsent_message)
    
