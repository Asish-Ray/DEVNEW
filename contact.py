def contact_form():
    print("Contact Us")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    message = input("Enter your message: ").strip()

    if not name or not email or not message:
        print("Please fill in all fields.")
        return

    # Here you could add code to send/store the message
    print(f"\nThank you, {name}! Your message has been received.")

if __name__ == "__main__":
    contact_form()