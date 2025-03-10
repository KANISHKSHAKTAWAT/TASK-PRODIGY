from PIL import Image
import numpy as np

# Encrypt Image Function
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    
    # Encrypting pixels (using XOR for reversible encryption)
    encrypted_array = img_array ^ key

    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as: {output_path}")

# Decrypt Image Function
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    
    # Decrypting pixels (XOR again reverses the encryption)
    decrypted_array = img_array ^ key

    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as: {output_path}")

# File paths and encryption key
input_path = r"D:\nattu-adnan-vvHRdOwqHcg-unsplash.jpg"
encrypted_path = r"D:\peter-vanosdall-uZVtAixV8c8-unsplash.jpg"
decrypted_path = r"D:\decrypted_image.jpg"

# Encryption key (Use any integer value for security)
key = 123  

# Encrypt and Decrypt
encrypt_image(input_path, encrypted_path, key)
decrypt_image(encrypted_path, decrypted_path, key)
