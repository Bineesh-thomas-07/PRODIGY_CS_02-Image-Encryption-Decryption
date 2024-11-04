{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Encrypting the file: C:/Data_Analytics/image/ROBOT.jpg with key: 123\n",
      "Image encrypted and saved as encrypted_ROBOT.png\n",
      "Decrypting the file: encrypted_ROBOT.png with key: 123\n",
      "Image decrypted and saved as decrypted_ROBOT.png\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "import os\n",
    "\n",
    "# Encrypt Image\n",
    "def encrypt_image(input_image_path, output_image_path, key=123):\n",
    "    \n",
    "    print(f\"Encrypting the file: {input_image_path} with key: {key}\")\n",
    "    \n",
    "    if not os.path.exists(input_image_path):\n",
    "        print(f\"Error: The file '{input_image_path}' does not exist.\")\n",
    "        return\n",
    "\n",
    "    image = Image.open(input_image_path)\n",
    "    pixels = image.load()\n",
    "\n",
    "    for i in range(image.width):\n",
    "        for j in range(image.height):\n",
    "            r, g, b = pixels[i, j]\n",
    "            # XOR each pixel value with the key for encryption\n",
    "            pixels[i, j] = (r ^ key, g ^ key, b ^ key)\n",
    "\n",
    "    image.save(output_image_path)\n",
    "    print(f\"Image encrypted and saved as {output_image_path}\")\n",
    "\n",
    "# Decrypt Image\n",
    "def decrypt_image(encrypted_image_path, output_image_path, key=123):\n",
    "    \n",
    "    print(f\"Decrypting the file: {encrypted_image_path} with key: {key}\")\n",
    "    \n",
    "    if not os.path.exists(encrypted_image_path):\n",
    "        print(f\"Error: The file '{encrypted_image_path}' does not exist.\")\n",
    "        return\n",
    "\n",
    "    image = Image.open(encrypted_image_path)\n",
    "    pixels = image.load()\n",
    "\n",
    "    for i in range(image.width):\n",
    "        for j in range(image.height):\n",
    "            r, g, b = pixels[i, j]\n",
    "            # XOR each pixel value with the key for decryption\n",
    "            pixels[i, j] = (r ^ key, g ^ key, b ^ key)\n",
    "\n",
    "    image.save(output_image_path)\n",
    "    print(f\"Image decrypted and saved as {output_image_path}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    input_image = \"C:/Data_Analytics/image/ROBOT.jpg\"\n",
    "    encrypted_image = \"encrypted_ROBOT.png\"\n",
    "    decrypted_image = \"decrypted_ROBOT.png\"\n",
    "\n",
    "    # Key for encryption and decryption\n",
    "    encryption_key = 123\n",
    "\n",
    "    # Encrypt the image\n",
    "    encrypt_image(input_image, encrypted_image, key=encryption_key)\n",
    "\n",
    "    # Decrypt the image (to check if we get the original back)\n",
    "    decrypt_image(encrypted_image, decrypted_image, key=encryption_key)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
