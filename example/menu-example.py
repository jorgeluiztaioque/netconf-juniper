#!/usr/bin/env python3

import argparse

class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "Description for my parser")
        parser.add_argument("-H", "--Host", help = "Example: Help argument", required = True, default = "")
        parser.add_argument("-u", "--user", help = "Example: Save argument", required = True, default = "")
        parser.add_argument("-p", "--password", help = "Example: Print argument", required = True, default = "")
        parser.add_argument("-n", "--netconfport", help = "Example: Output argument", required = False, default = "")
        parser.add_argument("-f", "--function", help = "Example: Output argument", required = False, default = "")
        parser.add_argument("-c", "--command", help = "Example: Output argument", required = False, default = "")

        argument = parser.parse_args()
        status = False

        if argument.Host:
            host = (argument.Host)
            status = True
        if argument.user:
            user = (argument.user)
            status = True
        if argument.password:
            password = (argument.password)
            status = True
        if argument.netconfport:
            netconfport = (argument.netconfport)
            status = True
        if argument.function:
            function = (argument.function)
            status = True
        if argument.command:
            command = (argument.command)
            status = True
        if not status:
            print("Maybe you want to use -H or -u or -p or -n or -f or -c as arguments ?")


if __name__ == '__main__':
    app = CommandLine()
