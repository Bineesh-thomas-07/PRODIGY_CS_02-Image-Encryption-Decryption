# Image Encryption and Decryption

This project provides a simple Python-based tool to encrypt and decrypt images using an XOR encryption technique. The program takes an image file as input, applies an XOR operation to each pixel's RGB values using a specified key, and saves the result as an encrypted image. The same key can be used to decrypt the image back to its original state.

## Features

- **Encrypt Image**: Securely obfuscates image data using a specified key.
- **Decrypt Image**: Reverts encrypted images back to their original form using the same key.
- **Simple XOR Encryption**: Uses a basic XOR operation for encryption and decryption.

## Project Structure

- `encrypt_image(input_image_path, output_image_path, key)`: Encrypts an image file using an XOR operation on each pixel.
- `decrypt_image(encrypted_image_path, output_image_path, key)`: Decrypts an XOR-encrypted image file, restoring the original image.
- `main`: Executes both encryption and decryption on a sample image for demonstration.

## Getting Started

### Prerequisites

- Python 3.x
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/): Image processing library. Install via pip:

  ```bash
  pip install pillow
  ```

### Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/image-encryption-decryption.git
   cd image-encryption-decryption
   ```

2. **Run the Script**

   Modify the file paths and key as needed in the `main` block of `encrypt_decrypt_image.py`.

   ```python
   if __name__ == "__main__":
       input_image = "path/to/your/input_image.jpg"
       encrypted_image = "encrypted_image.png"
       decrypted_image = "decrypted_image.png"
       encryption_key = 123  # Example key, can be any integer

       # Encrypt the image
       encrypt_image(input_image, encrypted_image, key=encryption_key)

       # Decrypt the image
       decrypt_image(encrypted_image, decrypted_image, key=encryption_key)
   ```

3. **Run the script**

   ```bash
   python encrypt_decrypt_image.py
   ```

   This will create two output files:
   - `encrypted_image.png`: The encrypted version of your input image.
   - `decrypted_image.png`: The decrypted version, which should match the original image if the correct key is used.

### Example

Given an input image `image.jpg` and a key of `123`, the program will produce:
- An encrypted file `encrypted_image.png`.
- A decrypted file `decrypted_image.png`, which should resemble the original image.

## Encryption Details

- **Algorithm**: XOR-based encryption
- **Key**: A single integer key used to encrypt and decrypt each pixel's RGB values.

> **Note**: This method is for educational purposes and is not suitable for high-security encryption.

## License

This project is licensed under the MIT License.

