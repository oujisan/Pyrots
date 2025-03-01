# 🔄 **ROTen (ROTATION-n)**
A tool to rotate plaintext or ciphertext using ROT (Caesar cipher) with customizable rotation, reverse direction (default right), and brute-force ciphertext. This script can perform random rotation and direction of plaintext.

## ✨ **Features**
✅ Rotate text with custom rotation and direction.  
✅ Random rotation and direction mode.  
✅ Brute-force possible text rotation and direction.  
✅ Support in range **ROT13** and **ROT47**.  

## 📥 **Installation & Usage of script**
1. 🐍 Download and install Python from the Microsoft Store or the official website [python.org](https://www.python.org/downloads/) (official website recommended).

2. 📂 Clone the repository to your local directory:
   ```bash
   git clone https://github.com/oujisan/ROTen.git
   ```

3. 📌 Open your terminal (or CMD on Windows) and navigate to the **ROTen** directory. The installation script will automatically add **ROTen** to your system's **PATH** for easy global access.

4. 🛠️ Run the installation script based on your operating system:

   - **Windows**: Open run or `win + r` write `sysdm.cpl` and manually add the **ROTen** folder's path in  Advanced -> **Environment Variables** under **PATH**. 

     Example:
     ```
     C:/Users/oujisan/ROTen/
     ```

   - **Linux/macOS**: Ensure the `install.sh` script has execute permissions and run it:
      ```bash
      ./install.sh
      ```

5. 🎉 Congratulations! You can now use **ROTen** globally. Check if the installation is successful by running:
   ```bash
   roten
   ```

💡 If there's an error during installation, or if you want to run it on Android, execute the script manually with Python:
```bash
python roten.py
```

## 📚 **Argument Documentation**

### 📌 **USAGE:**
```bash
roten "text" -rot [numbers] [SETTING]
```

### ⚙️ **OPTIONS:**

| Option            | Description                                      |
|-------------------|--------------------------------------------------|
| `-h`, `--help`    | Show help message and exit.                      |
| `-rot`, `--rotation` | Specify rotation value (required except for `--random`). |
| `--random`        | Use a random rotation value and direction.        |
| `--bruteforce`    | Display all possible decryptions (ROT13 & ROT47). |

### 🔧 **SETTINGS:**

| Setting           | Description                                      |
|-------------------|--------------------------------------------------|
| `--reverse`       | Reverse the rotation direction (Default: Right →).|
| `--both`          | Show decryptions in both right and left directions.|

## 📊 **Usage Examples**

👉 **Rotate plaintext or ciphertext:**
```bash
roten "HelloWorld" -rot 13
```

👉 **Rotate with reverse direction:**
```bash
roten "HelloWorld" -rot 13 --reverse
```

👉 **Rotate with random rotation and direction:**
```bash
roten "HelloWorld" --random
```

👉 **Rotate and show both directions:**
```bash
roten "AxeehPhkew" -rot 19 --both
```

👉 **Brute-force ciphertext (ROT13 & ROT47):**
```bash
roten "AxeehPhkew" --bruteforce
```

## 🧰 **Build-In**
- Python **3.13.1**

📅 **Created Date:** Wednesday, February 26, 2025

🚀 **Happy Rotating!**

