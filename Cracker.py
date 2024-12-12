import PyPDF2

def brute_force_pdf(pdf_path, password_list_path):
    """
    Brute-force a password-protected PDF using a list of passwords.
    
    Parameters:
    pdf_path (str): Path to the PDF file.
    password_list_path (str): Path to the password list file.
    
    Returns:
    str: The correct password if found, otherwise None.
    """
    # Open the password-protected PDF
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None

    # Open the password list file
    try:
        with open(password_list_path, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print("Password list file not found.")
        return None

    # Try each password
    for password in passwords:
        password = password.strip()  # Remove whitespace and newline characters
        try:
            # Attempt to decrypt the PDF
            if pdf_reader.decrypt(password):
                print(f"Password found: {password}")
                return password
        except Exception as e:
            # Log decryption attempts
            print(f"Failed attempt with password: {password}")
    
    print("Password not found in the list.")
    return None


# Example usage
# Uncomment the following lines to run the script
# pdf_path = "protected.pdf"  # Path to your PDF file
# password_list_path = "passwords.txt"  # Path to your password list
# brute_force_pdf(pdf_path, password_list_path)
