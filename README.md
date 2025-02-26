# Pyrots (Python ROT)
A tool to encrypt and decrypt text using ROT (Caesar cipher) with customizable rotation, reverse direction, and brute-force decryption. This script can do random rotation and direction encryption of plaintext.

## Retricions
1. CLI (Command Line Interface) only.
2. Recieve only input text or string type.
3. Support only between ROT13 and ROT47.

## Installation & Usage of script
1. Download and install python in the Microsoft Store or Official Website [python.org](https://www.python.org/downloads/) (Official website recommended).
2. Copy repository to local directory
```
git clone https://github.com/oujisan/Pyrots.git
```
3. Open terminal or CMD, make sure you're in path of PyROTS before run installation. Installation script will auto add PyROTS to PATH so, you can running it in easy way.

4. Run Installation based your Operation System.
- If you use Windows OS, run `install.bat`.
```
install.bat
```
- If use Linux or MacOS OS, run `install.sh`. Make sure file has execute permission.
```
./install.sh
```
5. Congratulations!!! Now you can run PyROTS globally in terminal or cmd. Run `pyrots` to check it.
```
pyrots
```

## Argument Documentation
**USAGE:** 
```
pyrots [MODE] "text" -rot [numbers] [SETTING]
```
**OPTIONS:**

`-h`, `--help`       Show help message and exit.

`-rot`, `--rotation` Rotation character. Required for encryption and decryption mode (except --bruteforce and --random)

**MODES:**

`-e`, `--encrypt`    Encrypt plaintext.

`-d`, `--decrypt`    Decrypt ciphertext.

**SETTINGS**

`--reverse`          Reverse rotate direction (Default: right or '→')

`--bruteforce`       List all possible ROT13 and ROT47 decryptions (Requires -d/--decrypt)

`--both`             display decryption in right and left direction of rotation (Requires -d/--decrypt)

`--random`           Choose random rotation and direction for encrypt plaintext (Requires -e/--encrypt)

## Usage Example
Encrypt plaintext with reverse direction
```
pyrots -e "HelloWorld" -rot 13
```

Encrypt plaintext with random
```
pyrots -e "HelloWorld" --random
```

Decrypt ciphertext with reverse direction or with both direction
```
pyrtos -d "AxeehPhkew" -rot 19 --reverse
```
```
pyrtos -d "AxeehPhkew" -rot 19 --both
```

Decrypt ciphertext with bruteforce
```
pyrots -d "AxeehPhkew" --bruteforce
```

## Build-In
Python 3.13.1

**Created date:** Wednesday, February 26 2025
