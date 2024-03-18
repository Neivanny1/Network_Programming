import os
import shutil
import requests

'''
Modules to copy files in specified dir
'''
def copy_directory_contents(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        if os.path.isdir(source_item):
            copy_directory_contents(source_item, destination_dir)  # Copy contents recursively without creating additional subdirectories
        else:
            shutil.copy2(source_item, destination_item)

'''
Sends files to the server listening at specified ip
'''
def send_to_server(directory_path, server_address):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(server_address, files=files)
                print(f"Uploaded {filename}: {response.text}")


if __name__ == "__main__":
    source_directory = "/home/cisco/Desktop/ALX/100daysofALXSE/DAY5/"
    destination_directory = "uploads/"
    server_address = "http://127.0.0.1:8000/upload"
    
    copy_directory_contents(source_directory, destination_directory)
    send_to_server(destination_directory, server_address)
