import random
import string

print("🛡️ Password Generator 🛡️\n")

length = int(input("Enter the desired password length: "))

print("\nChoose password complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")
choice = input("Enter choice (1/2/3): ")

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to letters + numbers + symbols.")
    characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("\n🔑 Generated Password:", password)
