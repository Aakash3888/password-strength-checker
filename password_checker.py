"""
Password Strength Checker
--------------------------
Ye tool kisi bhi password ki strength check karta hai based on:
- Length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common weak passwords list

Educational / Ethical use only.
"""

import re

# Common weak passwords ki chhoti list (aap ise badha sakte ho)
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password123", "admin", "letmein", "welcome", "monkey",
    "iloveyou", "111111", "12345678", "sunshine", "princess"
]


def check_password_strength(password: str) -> dict:
    """
    Password ko check karta hai aur score + feedback return karta hai.
    """
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password kam se kam 8 characters ka hona chahiye (12+ better hai).")

    # 2. Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Kam se kam ek UPPERCASE letter add karo (A-Z).")

    # 3. Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Kam se kam ek lowercase letter add karo (a-z).")

    # 4. Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Kam se kam ek number add karo (0-9).")

    # 5. Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        score += 1
    else:
        feedback.append("Kam se kam ek special character add karo (!@#$% etc.).")

    # 6. Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["Ye ek bahut common/weak password hai! Ise turant change karo."]

    # Final rating decide karna
    if score >= 6:
        rating = "Strong 💪"
    elif score >= 4:
        rating = "Medium ⚠️"
    else:
        rating = "Weak ❌"

    return {
        "password": password,
        "score": score,
        "rating": rating,
        "feedback": feedback
    }


def print_result(result: dict) -> None:
    print("\n--- Password Strength Result ---")
    print(f"Rating : {result['rating']}")
    print(f"Score  : {result['score']}/6")
    if result["feedback"]:
        print("Suggestions:")
        for tip in result["feedback"]:
            print(f"  - {tip}")
    else:
        print("Bahut badhiya! Koi suggestion nahi.")
    print("---------------------------------\n")


def main():
    print("=== Password Strength Checker ===")
    print("(Educational tool - passwords are NOT stored anywhere)\n")

    while True:
        pwd = input("Password enter karo (ya 'exit' likho band karne ke liye): ")
        if pwd.lower() == "exit":
            print("Bye! 👋")
            break

        result = check_password_strength(pwd)
        print_result(result)


if __name__ == "__main__":
    main()
