#
#   @file : burn.py
#   @authors : PuppetBlocks team
#   @date : 22 February 2023
#
# This file is used for burning ESP32 devices, and not being uploaded to the micro controller.
#
import pathlib
import subprocess
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
    arguments = cl_parser.parse_args()

    micropython = arguments.micropython
    esptool = arguments.esptool
    connection = arguments.connection

    # First stage: download MicroPython
    with tempfile.NamedTemporaryFile(delete=False) as file:
        response = requests.get(micropython)
        file.write(response.content)
        address = file.name
        print('--- PuppetBlocks BURNER: MicroPython file has downloaded successfully! ---')

    # Second stage: burn firmware
    cmd = [
        str(esptool),
        '--chip esp32',
        '--port',
        connection,
        '--baud 921600',
        '--before default_reset',
        '--after hard_reset',
        'write_flash -z',
        '--flash_mode dio',
        '--flash_freq 80m',
        '--flash_size 4MB',
        '0x1000',
        address
    ]
    full_cmd = ' '.join(cmd)
    subprocess.run(full_cmd, shell=True)
    print('--- PuppetBlocks BURNER: MicroPython firmware has burned! ---')


if __name__ == '__main__':
    main()
