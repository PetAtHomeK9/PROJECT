import os
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(customer_name, dog_breed, amount_paid, old_home_address, new_home_address):
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    file_name = f"receipt_{dog_breed.replace(' ', '_')}.pdf"
    file_path = os.path.join(current_dir, file_name)
    
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Add company details
    c.drawString(100, 750, "PetAtHome K9")
    c.drawString(100, 735, "123 Pet Street")
    c.drawString(100, 720, "Pet City, NIGERIA")
    c.drawString(100, 705, "Phone: +234 901 440 1045")

    # Add slogan
    c.drawString(100, 690, "Where every tail finds a happy home!")

    # Add receipt details
    c.drawString(400, 735, "Date: 2024-07-10")

    # Add customer details
    c.drawString(100, 670, f"Customer Name: {customer_name}")
    c.drawString(100, 655, f"Dog Breed: {dog_breed}")
    c.drawString(100, 640, f"Amount Paid: #{amount_paid}")

    # Add addresses
    c.drawString(100, 620, f"Old Home Address: {old_home_address}")
    c.drawString(100, 605, f"New Home Address: {new_home_address}")

    # Add a thank you note
    c.drawString(100, 580, "Thank you for your purchase!")

    c.showPage()
    c.save()

    print(f"Receipt saved as {file_path}")

    # Automatically open the PDF file
    subprocess.Popen([file_path], shell=True)

# Example usage
generate_receipt(
    "DE TONIES KENNEL & PET STORE",
    "Boerboel",
    130000,
    "Ibadan, Oyo State",
    "Ilesha, Osun State"
)
