import streamlit as st
import re
import random
import string

def check_password_strength(password):
    messages = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        messages.append(("error", "❌ Password should be at least 8 characters long."))
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        messages.append(("error", "❌ Include both uppercase and lowercase letters."))
    
    if re.search(r'\d', password):
        score += 1
    else:
        messages.append(("error", "❌ Add at least one number (0-9)."))
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        messages.append(("error", "❌ Include at least one special character (!@#$%^&*)."))
    
    if score == 4:
        messages.append(("success", "✅ Strong Password!"))
    elif score == 3:
        messages.append(("warning", "⚠️ Moderate Password - Consider adding more security features."))
    else:
        messages.append(("error", "❌ Weak Password - Improve it using the suggestions above."))
    
    return messages

def generate_password(length=8):
    uppercase = random.choices(string.ascii_uppercase, k=1)
    lowercase = random.choices(string.ascii_lowercase, k=1)
    digits = random.choices(string.digits, k=1)
    special = random.choices("!@#$%^&*", k=1)
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining_length = length - 4
    remaining = random.choices(all_chars, k=remaining_length) if remaining_length > 0 else []
    password_chars = uppercase + lowercase + digits + special + remaining
    random.shuffle(password_chars)
    return ''.join(password_chars)

st.title("🔒 Password Strength Checker & Generator")

option = st.radio(
    "Choose an option:", 
    ("Check Password Strength", "Generate Password"),
    horizontal=True
)

if option == "Check Password Strength":
    password = st.text_input("Enter password:")
    if st.button("Check Strength"):
        feedback = check_password_strength(password)
        for msg_type, msg in feedback:
            if msg_type == "error":
                st.error(msg)
            elif msg_type == "warning":
                st.warning(msg)
            elif msg_type == "success":
                st.success(msg)

else:
    col1, col2 = st.columns([2, 1])
    with col1:
        length = st.slider(
            "Password length:", 
            min_value=8, 
            max_value=32, 
            value=12,
            help="Minimum length is 8 characters"
        )
    
    password = generate_password(length)
    st.subheader("Your Secure Password:")
    st.code(password, language="text")
    st.write("Click the code above to copy, then paste where needed!")