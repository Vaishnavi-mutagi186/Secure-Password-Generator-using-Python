Secure Password Generator

A secure and customizable **Password Generator** built with **Python**. This project allows users to generate strong passwords by selecting the password length and character types including uppercase, lowercase, digits, and special symbols. The generated password is copied to the clipboard for easy use.

---

 Features
- Generate strong, secure passwords
- Choose password length
- Include/exclude:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special symbols
- Option to avoid ambiguous characters (like l, 1, O, 0, I)
- Runs via **Command-Line Interface (CLI)**
- Copies generated password automatically to clipboard (optional)

---
 Technologies Used
- Python 3
- `secrets` module (for cryptographically secure random generation)
- `string` module
- `pyperclip` (for clipboard support)

---

## How to Run

1. Clone or download this repository:

```bash
git clone https://github.com/yourusername/password-generator-python.git
Navigate to the project folder:

cd password-generator-python
(Optional) Install pyperclip to enable clipboard copying:

pip install pyperclip
Run the program:


python password_generator.py
Follow the on-screen instructions to generate your password.

Sample Output

Enter password length (default 12): 16
Include lowercase? (Y/n): 
Include uppercase? (Y/n): 
Include digits? (Y/n): 
Include symbols? (Y/n): 
Avoid ambiguous characters (l,1,O,0,I)? (y/N): n

Generated password:
y6)s|!:39Q*3ERj>
(Password copied to clipboard)
Skills Gained
Python programming

Cybersecurity basics (secure random generation)

Command-Line Interface (CLI) development

Problem-solving

Software development practices

Author
Your Name – VAISHNAVI MUTAGI
GitHub: 


