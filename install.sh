#!/bin/bash
chmod +x ./pyrots.py
sudo cp pyrots.py /usr/local/bin/pyrots
sudo sed -i 's/\r$//' "/usr//local/bin/pyrots"
echo "PyROT has been successfully installed! You can run it using: pyrots"