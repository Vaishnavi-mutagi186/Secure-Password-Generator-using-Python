import secrets
import string
import sys

def build_charset(include_lower, include_upper, include_digits, include_symbols, avoid_ambiguous):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|~"

    if avoid_ambiguous:
        ambig = {'l', 'I', '1', 'O', '0'}
        lower = ''.join(c for c in lower if c not in ambig)
        upper = ''.join(c for c in upper if c not in ambig)
        digits = ''.join(c for c in digits if c not in ambig)

    charset = ""
    if include_lower:
        charset += lower
    if include_upper:
        charset += upper
    if include_digits:
        charset += digits
    if include_symbols:
        charset += symbols

    return charset, lower, upper, digits, symbols


def generate_password(length, include_lower=True, include_upper=True,
                      include_digits=True, include_symbols=True,
                      avoid_ambiguous=False):
    charset, lower, upper, digits, symbols = build_charset(
        include_lower, include_upper, include_digits, include_symbols, avoid_ambiguous)

    if not charset:
        raise ValueError("No character set selected!")

    required = []
    if include_lower:
        required.append(secrets.choice(lower))
    if include_upper:
        required.append(secrets.choice(upper))
    if include_digits:
        required.append(secrets.choice(digits))
    if include_symbols:
        required.append(secrets.choice(symbols))

    if length < len(required):
        raise ValueError("Password length too short!")

    remaining = length - len(required)
    password = required + [secrets.choice(charset) for _ in range(remaining)]

    # Shuffle password securely
    for i in range(len(password)-1, 0, -1):
        j = secrets.randbelow(i+1)
        password[i], password[j] = password[j], password[i]

    return ''.join(password)


def prompt_bool(question, default=True):
    d = "Y/n" if default else "y/N"
    ans = input(f"{question} ({d}): ").strip().lower()
    if ans == "":
        return default
    return ans[0] == 'y'


def main():
    print("=== PASSWORD GENERATOR ===")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except:
        print("Invalid number!")
        sys.exit()

    include_lower = prompt_bool("Include lowercase letters?", True)
    include_upper = prompt_bool("Include uppercase letters?", True)
    include_digits = prompt_bool("Include digits?", True)
    include_symbols = prompt_bool("Include symbols?", True)
    avoid_ambiguous = prompt_bool("Avoid ambiguous characters (l,1,O,0,I)?", False)

    try:
        password = generate_password(
            length,
            include_lower,
            include_upper,
            include_digits,
            include_symbols,
            avoid_ambiguous
        )
    except ValueError as e:
        print("Error:", e)
        sys.exit()

    print("\nGenerated Password:")
    print(password)

    try:
        import pyperclip
        pyperclip.copy(password)
        print("(Password copied to clipboard)")
    except:
        pass


if __name__ == "__main__":
    main()
