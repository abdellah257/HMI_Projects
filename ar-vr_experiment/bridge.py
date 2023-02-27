import sys
import getopt
import time, threading
import serial
from pynput.keyboard import Key,Controller

SERIALPORT = "COM3"
SERIALBAUD = 9600


VERBOSE = 0
Keyboard = Controller()
elements = [['_','a','b'],['c','d','e'],['f','g','h'],['i','j','k'],['l','m','n'],['o','p','q'],['r','s','t'],['u','v','w'],['x','y','z'],['0','1','2']]
last_finger = ""

#Reading command line
def print_help():
    print('\nUsage:    python bridge.py [[OPTIONS]]')
    print('  -s [arg] or --serial [arg]: path to the glove serial port (default: "{}")'.format(SERIALPORT))
    print('  -b [arg] or --baud [arg]: baudrate used to connect (default: "{}")'.format(SERIALBAUD))
    print('  -h or --help: print help (no argument)')

opts, args = getopt.getopt(
    sys.argv[1:],
    's:b:p:v:h',
    ["serial=", "baud=", "verbose=", "help"])

for o, v in opts:
    if o in ('-s, --serial'):
        SERIALPORT = v
    if o in ('-b, --baud'):
        try:
            SERIALBAUD = int(v)
        except:
            print('/!\\ Baudrate value should be an integer. /!\\')
            print('   => The default {} value will be used.'.format(SERIALBAUD))
    if o in ('-v, --verbose'):
        try:
            VERBOSE = int(v)
            if VERBOSE < 0: VERBOSE = 0
            if VERBOSE > 2: VERBOSE = 2
        except:
            print('/!\\ Verbose mode value should be 0, 1 or 2. /!\\')
            print('   => The default {} value will be used.'.format(VERBOSE))

    if o in ('-h', '--help'):
        print_help()
        sys.exit()


def connect():
    if VERBOSE > 0:
        print("######## SERIAL INFOS ########")
        print("     PORT:", SERIALPORT)
        print(" BAUDRATE:", SERIALBAUD)
        print("##############################")

    conn = None

    try:
        conn = serial.Serial(
                port     = SERIALPORT,
                baudrate = SERIALBAUD,
                bytesize = 8,
                timeout  = 2,
                stopbits = serial.STOPBITS_ONE
            )
    except Exception as e:
        print("########### ERROR ############")
        print('Error while connecting to the serial port. Please check the settings.')
        print()
        print(e)
        print("##############################")
        conn = None
    
    return conn


def process_data(data):

    counter = [int(s) for s in data.split() if s.isdigit()]
    if counter == []:
        counter.append(0)

    '''Right Hand Mapping'''

    if 'Right THUMB' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[0][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[0][counter[0]%3])
        else:
            Keyboard.press(Key.space)
            time.sleep(0.1)
            Keyboard.release(Key.space)
        
    if 'Right INDEX' in data:
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[1][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[1][counter[0]%3])
        else:
            Keyboard.press(elements[1][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[1][counter[0]])         
    if 'Right MIDDLE' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[2][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[2][counter[0]%3])
        else:
            Keyboard.press(elements[2][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[2][counter[0]])
    if 'Right DDD' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[3][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[3][counter[0]%3])
        else:
            Keyboard.press(elements[3][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[3][counter[0]])   
    if 'Right PETIT' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[4][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[4][counter[0]%3])
        else:
            Keyboard.press(elements[4][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[4][counter[0]])
    '''Left Hand Mapping'''
    if 'Left THUMB' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[5][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[5][counter[0]%3])
        else:
            Keyboard.press(elements[5][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[5][counter[0]])
    if 'Left INDEX' in data:
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[6][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[6][counter[0]%3])
        else:
            Keyboard.press(elements[6][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[6][counter[0]])         
    if 'Left MIDDLE' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[7][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[7][counter[0]%3])
        else:
            Keyboard.press(elements[7][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[7][counter[0]])
    if 'Left DDD' in data: 
        if 'MULTI' in data:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace)
            if(counter[0]%3 == 0):
                Keyboard.press(Key.space)
                time.sleep(0.1)
                Keyboard.release(Key.space)
            else:
                Keyboard.press(elements[8][counter[0]%3])
                time.sleep(0.1)
                Keyboard.release(elements[8][counter[0]%3])
        else:
            Keyboard.press(elements[8][counter[0]])
            time.sleep(0.1)
            Keyboard.release(elements[8][counter[0]])   
    if 'Left PETIT' in data: 
        # if 'MULTI' in data:
        #     Keyboard.press(Key.backspace)
        #     time.sleep(0.1)
        #     Keyboard.release(Key.backspace)
        #     if(counter[0]%3 == 0):
        #         Keyboard.press(Key.space)
        #         time.sleep(0.1)
        #         Keyboard.release(Key.space)
        #     else:
        #         Keyboard.press(elements[9][counter[0]%3])
        #         time.sleep(0.1)
        #         Keyboard.release(elements[9][counter[0]%3])
        # else:
            Keyboard.press(Key.backspace)
            time.sleep(0.1)
            Keyboard.release(Key.backspace) 


def main():

    print("Arduino server initializing...")
    conn = None

    while True:

        print("Arduino server trying to connect...")
        conn = connect()
        if conn == None:
            print(" => Connection Failed. Please check wire and serial options.")
            time.sleep(1)
            continue

        print("Arduino server running")
        while conn.is_open:
            # try:
            #     if(conn.in_waiting > 0):
            #         data = None
            #         try:
            #             data = conn.readline().decode('Ascii')
            #             process_data(data)
            #         except:
            #             break

            #         if VERBOSE > 0:
            #             print("Data received:")
            #             print(">", data)

            # except:
            #     time.sleep(1)
            #     break
            data = conn.readline().decode('Ascii')
            process_data(data)

        conn = None
        print("Arduino server closed.")


if __name__ == '__main__':
    main()
