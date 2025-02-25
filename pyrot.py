import sys
import argparse

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
    for i in range(127):
        if i in range(26):
            print(f'ROT-{i:02} → = {rotation(text=text, rot=i, decrypt=True, reverse=False)}')
            print(f'ROT-{i:02} ← = {rotation(text=text, rot=i, decrypt=True, reverse=True)}')
        elif i in range(33,127):
            print(f'ROT-{i:02} → = {rotation(text=text, rot=i, decrypt=True, reverse=False)}')
            print(f'ROT-{i:02} ← = {rotation(text=text, rot=i, decrypt=True, reverse=True)}')

def main():
    try:
        parser = argparse.ArgumentParser(
            prog='pyrot-san',
            description='A tool to encrypt and decrypt text using ROT (Caesar cipher) with customizable rotation, reverse direction, and brute-force decryption.',
            usage='python pyrot.py (-e "plaintext" | -d "ciphertext") -rot [number] [--reverse | --bruteforce]',
            epilog='''Example:
                python pyrot.py -e "HelloWorld" -rot 13 | 
                python pyrot.py -d "GdkknVnqkc" -rot 13 --reverse | 
                python pyrot.py -d "GdkknVnqkc" --bruteforce'''
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

        args = parser.parse_args()

        if not len(sys.argv) > 1:
            parser.print_help()
            sys.exit()
            
        if args.bruteforce:
            if not args.decrypt:
                parser.error("--bruteforce only works with -d/--decrypt")
            if args.rotation or args.reverse:
                parser.error("--bruteforce cannot be used with --reverse or --rotation")

        if args.reverse and args.rotation is None:
            parser.error("--reverse requires --rotation")

        if args.encrypt and args.rotation is None:
            parser.error("Encryption (-e/--encrypt) requires --rotation")

    except SystemExit:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
