# password-strength-checker
# 🔐 Password Strength Checker

A simple Python CLI tool that checks how strong a password is — built for learning basic cybersecurity/ethical hacking concepts.

## Features
- Checks password length
- Checks for uppercase, lowercase, numbers, special characters
- Flags common/weak passwords (e.g. `password123`, `qwerty`)
- Gives a score and rating: **Weak / Medium / Strong**
- Suggests improvements

## Requirements
- Python 3.x
- No external libraries needed (uses only Python's built-in `re` module)

## How to Run
```bash
python password_checker.py
```

Then type any password to check its strength. Type `exit` to quit.

## Example Output
```
Password enter karo (ya 'exit' likho band karne ke liye): abc123

--- Password Strength Result ---
Rating : Weak ❌
Score  : 2/6
Suggestions:
  - Password kam se kam 8 characters ka hona chahiye (12+ better hai).
  - Kam se kam ek UPPERCASE letter add karo (A-Z).
  - Kam se kam ek special character add karo (!@#$% etc.).
---------------------------------
```

## Disclaimer
This tool is built for **educational purposes only**, to understand password security concepts. It does not store, log, or transmit any password entered.

## Future Improvements (Ideas)
- Add a GUI version (Tkinter)
- Check password against real leaked-password databases (e.g. Have I Been Pwned API)
- Add entropy-based strength calculation

## License
MIT
