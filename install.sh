#!/bin/bash
chmod +x ./roten.py
sudo cp roten.py /usr/local/bin/roten
sudo sed -i 's/\r$//' "/usr//local/bin/roten"
echo "ROTen has been successfully installed! You can run it using: roten"