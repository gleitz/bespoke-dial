import argparse
import glob
import serial

from os import system

from lib import pygvoicelib

with open('secret.txt', 'r') as f:
    USERNAME, PASSWD = f.read().strip().split('|||')

CALLBACK_NUMBER = '5102270616' # False to autoselect
SERIAL_INTERFACE = '/dev/tty.usbserial-A800eH6d' # False to autodetect

if not SERIAL_INTERFACE:
    try:
        SERIAL_INTERFACE = glob.glob("/dev/tty.usbserial*")
    except IndexError:
        print 'Could not find arduino serial port'

def listen():
    ser = serial.Serial(SERIAL_INTERFACE, 9600)
    previous_numbers = []
    while True:
        number = ser.readline().strip()
        system('say {0}'.format(number))
        previous_numbers.append(number)
        if len(previous_numbers) == 10:
            outgoing_number = ''.join(previous_numbers)
            call(outgoing_number)
            previous_numbers = []

def call(outgoing_number):
    voice = pygvoicelib.GoogleVoice(USERNAME, PASSWD)
    voice.get_numbers()
    state = voice.get_state()
    voice = pygvoicelib.GoogleVoice(*state)

    local_callback = CALLBACK_NUMBER
    if not local_callback:
        phone_list = voice.get_numbers()
        for num in phone_list:
            if num.isdigit() and phone_list[num]['verified']:
                local_callback = num

    voice.call('+1' + outgoing_number, '+1' + local_callback)

def command_line_runner():
    parser = argparse.ArgumentParser(description='bespoke dial: old-timey speed dial')
    parser.add_argument('-l','--listen', help='listens for dialed numbers and initiates the call after 10 numbers have been dialed')
    parser.add_argument('-d','--dial', help='dial a number')
    args = vars(parser.parse_args())
    if args.get('dial'):
        call(args.get('dial'))
    elif args.get('listen'):
        listen()
    else:
        listen()

if __name__ == '__main__':
    command_line_runner()
