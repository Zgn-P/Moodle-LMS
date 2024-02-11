import paramiko
import os

# SFTP server details
SFTP_HOST = 'your_sftp_host'
SFTP_PORT = 22
SFTP_USERNAME = 'your_sftp_username'
SFTP_PASSWORD = 'your_sftp_password'

# Local directory to save files
LOCAL_DIR = 'path/to/local/directory'

# Connect to SFTP server
transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)

# List files in the SFTP directory
sftp.chdir('path_to_sftp_directory')
file_list = sftp.listdir()

# Download and check files
for file_name in file_list:
    remote_path = f'path_to_sftp_directory/{file_name}'
    local_path = os.path.join(LOCAL_DIR, file_name)

    # Download file from SFTP server to local directory
    sftp.get(remote_path, local_path)
    print(f"File downloaded: {file_name}")

    # Perform data checks or validations on the local file
    # Replace the following code with your own data checks
    with open(local_path, 'r') as file:
        file_content = file.read()
        if 'your_data_check' in file_content:
            print(f"Data check passed for: {file_name}")
        else:
            print(f"Data check failed for: {file_name}")

# Close SFTP connection
sftp.close()
transport.close()
