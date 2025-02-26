import sys
import argparse
import textwrap

banner = r'''
      ___      ___  ___ _____ 
     | _ \_  _| _ \/ _ \_   _|
     |  _/ || |   / (_) || |  
     |_|  \_, |_|_\\___/ |_|  
          |__/                
'''
def rotation(text, rot, decrypt=False, reverse=False):
    rotated = ''
    for i in text:
        direction = -1 if decrypt ^ reverse else 1
            
        if rot in range(1,26) and i.isalpha():
            base, mod = ord('a') if i.islower() else ord('A'), 26
            rotated += chr((ord(i) - base + rot * direction) % mod + base)
        elif rot in range(33,127) and 33 <= ord(i) <= 126:
            base, mod = 33, 94
            rotated += chr((ord(i) - base + rot * direction) % mod + base)
        else:
            rotated += i
    return rotated

def bruteforce(text):
    space = 7
    for i in range(127):
        if i in range(26):
            print(f'ROT-{i:02} → = {rotation(text=text, rot=i, decrypt=True, reverse=False)}')
            print(f'{' '*space}← = {rotation(text=text, rot=i, decrypt=True, reverse=True)}')
        elif i in range(33,127):
            if len(str(i)) == 3:
                space = 8
            print(f'ROT-{i:02} → = {rotation(text=text, rot=i, decrypt=True, reverse=False)}')
            print(f'{' '*space}← = {rotation(text=text, rot=i, decrypt=True, reverse=True)}')

def main():
    try:
        parser = argparse.ArgumentParser(
            prog='pyrot-san',
            description='A tool to encrypt and decrypt text using ROT (Caesar cipher) with customizable rotation, reverse direction, and brute-force decryption.',
            usage='python pyrots.py (-e "plaintext" | -d "ciphertext") -rot [number] [--reverse | --bruteforce]',
            epilog='''Example:
                python pyrots.py -e "HelloWorld" -rot 13 | 
                python pyrots.py -d "GdkknVnqkc" -rot 13 --reverse | 
                python pyrots.py -d "GdkknVnqkc" --bruteforce'''
        )

        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument(
            "-e", "--encrypt",
            type=str,
            help='Encrypt plaintext'
        )

        group.add_argument(
            "-d", "--decrypt",
            type=str,
            help='Decrypt ciphertext'
        )

        parser.add_argument(
            "-rot", "--rotation",
            type=int,
            help='Rotation character. Required for encryption and reverse mode'
        )

        settings_group = parser.add_argument_group('Settings')
        settings_group.add_argument(
            "--reverse",
            action="store_true",
            help='Reverse rotation direction (Default: right)'
        )
        settings_group.add_argument(
            "--bruteforce",
            action="store_true",
            help='List all possible ROT13 or ROT47 decryptions (Requires -d/--decrypt)'
        )

        if len(sys.argv) == 1:
            print(banner)
            parser.print_help()
            sys.exit(1)

        args = parser.parse_args()

        if args.encrypt:
            if not args.rotation:
                parser.error("--encrypt requires -rot / --rotation")
                sys.exit(1)
            switch = True if args.reverse else False
            rotated = rotation(text=args.encrypt, rot=args.rotation, decrypt=False, reverse=switch)
            print(rotated)
        elif args.decrypt:
            if args.bruteforce:
                if args.rotation or args.reverse:
                    parser.error("--bruteforce cannot be used with --reverse or --rotation")
                    sys.exit(1)
                bruteforce(args.decrypt)
            elif args.rotation:
                reverse = True if args.reverse else False
                rotated = rotation(text=args.decrypt, rot=args.rotation, decrypt=True, reverse=reverse)
                print(rotated)
            else:
                parser.error("--decrypt requires -rot / --rotation. Try --bruteforce to show all possible decryptions")
                sys.exit(1)
            
        if args.reverse and args.rotation is None:
            parser.error("--reverse requires --rotation")

        if args.encrypt and args.rotation is None:
            parser.error("Encryption (-e/--encrypt) requires --rotation")

    except SystemExit:
        sys.exit(1)

if __name__ == "__main__":
    main()
