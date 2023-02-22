#
#   @file : burn.py
#   @authors : PuppetBlocks team
#   @date : 22 February 2023
#
# This file is used for burning ESP32 devices, and not being uploaded to the micro controller.
#
import pathlib
import serial
import requests
import tempfile
import argparse


def main() -> None:
    cl_parser = argparse.ArgumentParser(description='PuppetBlocks - Learn programming with blocks and a puppet.',
                                        epilog='For help with the burner please read SUPPORT.md .',
                                        allow_abbrev=False)
    cl_parser.add_argument('-m', '--micropython', action='store', type=str,
                            help='the url of the MicroPython firmware (default: v1.19.1)', dest='micropython',
                            default="https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin")
    cl_parser.add_argument('-e', '--esptool', action='store', type=pathlib.Path, required=True,
                            help='the root for esptool.exe', dest='esptool')
    cl_parser.add_argument('-c', '--connection', action='store', type=str, required=True,
                            help='the connection to the device (usually COM4)', dest='connection')
    cl_parser.add_argument('-s', '--ssid', action='store', type=str, required=True,
                            help='the SSID of the network', dest='network_id')
    cl_parser.add_argument('-p', '--password', action='store', type=str, required=True,
                            help='the password of the network', dest='network_password')
    arguments = cl_parser.parse_args()

    micropython = arguments.micropython
    esptool = arguments.esptool
    connection = arguments.connection
    network_id = arguments.network_id
    network_password = arguments.network_password

    with tempfile.NamedTemporaryFile() as file:

        # First stage: download MicroPython
        response = requests.get(micropython)
        file.write(response.content)
        print('--- PuppetBlocks BURNER: MicroPython file has downloaded successfully! ---')

        # Second stage: burn firmware
        cmd = [
            esptool,
            '--chip esp32',
            '--port',
            connection,
            '--baud 921600',
            '--before default_reset',
            '--after hard_reset',
            '--erase-all',
            'write_flash -z',
            '--flash_mode dio',
            '--flash_freq 80m',
            '--flash_size 4MB',
            '0x1000',
            file.name
        ]
        full_cmd = ' '.join(cmd)
        exec(full_cmd)
        print('--- PuppetBlocks BURNER: MicroPython firmware has burned! ---')
    
    with tempfile.NamedTemporaryFile() as file:

        # Third stage: create 'Secrets.py' file 
        content = f'NETWORK_ID = "{network_id}"; NETWORK_PASSWORD = "{network_password}"\n'
        file.write(content.encode('utf-8'))
        file.seek(0)
        print('--- PuppetBlocks BURNER: Secrets.py file has been created! ---')

        # Fourth stage: set standard library
        files = {
            'Audio.py': open('Audio.py', 'rb'),
            'boot.py': open('boot.py', 'rb'),
            'PuppetBlocks.py': open('PuppetBlocks.py', 'rb'),
            'Screen.py': open('Screen.py', 'rb'),
            'Secrets.py': file,
        }
        with serial.Serial(connection, 115200, timeout=5, rtscts=False, dsrdtr=False) as serial_connection:
            for name, file_stream in files.items():
                content = file_stream.read()
                length = len(content)
                code =  f'import sys\n' + \
                        f'with open("{name}", "wb") as file:\n' + \
                        f'\tfile.write(sys.stdin.buffer.read({length}))\n\n'
                serial_connection.write(code.encode('utf-8'))
                serial_connection.write(content)
        print('--- PuppetBlocks BURNER: Standard library has installed! ---')


if __name__ == '__main__':
    main()
