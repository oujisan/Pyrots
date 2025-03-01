# Pyrots (Python ROT)
A tool to rotate plaintext or ciphertext using ROT (Caesar cipher) with customizable rotation, reverse direction (default right), and brute-force ciphertext. This script can do random rotation and direction of plaintext.

## Retricions
1. CLI (Command Line Interface) only.
2. Recieve only input text or string type.
3. Support in range ROT13 and ROT47.

## Installation & Usage of script
1. Download and install python in the Microsoft Store or Official Website [python.org](https://www.python.org/downloads/) (Official website recommended).
2. Copy repository to local directory
```
git clone https://github.com/oujisan/ROTen.git
```
3. Open terminal or CMD, make sure you're in path of ROTen before run installation. Installation script will auto add ROTen to PATH so, you can running it in easy way.

4. Run Installation based your Operation System.
- If you use Windows OS, open `sysdm.cpl` to add folder path ROTen to PATH in Environtment Variables.
- If use Linux or MacOS OS, run `install.sh`. Make sure file has execute permission.
```
./install.sh
```
5. Congratulations!!! Now you can run ROTen globally in terminal or cmd. Run `roten` to check it.
```
roten
```

If there's error while run install script or want to run in android device, run `roten.py` with python manually and make sure in path of script.
```
python roten.py
```

## Argument Documentation
**USAGE:** 
```
roten "text" -rot [numbers] [SETTING]
```
**OPTIONS:**

`-h`, `--help`       Show help message and exit.

`-rot`, `--rotation` Rotation character. Required for rotate text (except --random)

`--random`           Choose random rotation and direction for rotate plaintext

`--bruteforce`       List all possible ROT13 and ROT47 decryptions

**SETTINGS**

`--reverse`          Reverse rotate direction (Default: right or '→')

`--both`             display decryption in right and left direction of rotation


## Usage Example
rotate plaintext or ciphertext
```
roten "HelloWorld" -rot 13
```

rotate plaintext or ciphertext with reverse
```
pyrtos "Helloworld" -rot 13 --reverse
```

rotate plaintext with random rotate and direction
```
roten "HelloWorld" --random
```

rotate ciphertext with both direction
```
pyrtos "AxeehPhkew" -rot 19 --both
```

rotate ciphertext with bruteforce
```
roten "AxeehPhkew" --bruteforce
```

## Build-In
Python 3.13.1

**Created date:** Wednesday, February 26 2025
