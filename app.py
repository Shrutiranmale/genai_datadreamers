import openai
import requests
from PIL import Image
import urllib.request

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

def generate_image(prompt, size="256x256"):
    """Generate an image from a text prompt."""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )
    return response['data'][0]['url']

def save_image(image_url, filename):
    """Download and save the image from the URL."""
    urllib.request.urlretrieve(image_url, filename)
    print(f"Image saved as {filename}")

def edit_image(original_image_path, mask_image_path, prompt, size="256x256"):
    """Edit an existing image using a mask."""
    with open(original_image_path, "rb") as original_image, open(mask_image_path, "rb") as mask_image:
        response = openai.Image.create_edit(
            image=original_image,
            mask=mask_image,
            prompt=prompt,
            n=1,
            size=size
        )
    
    return response['data'][0]['url']

# Example usage
if __name__ == "__main__":
    # Generate a new image
    prompt = "A futuristic city skyline at sunset"
    generated_image_url = generate_image(prompt)
    save_image(generated_image_url, "generated_city.png")

    # Edit an existing image
    original_image_path = "samle.png"  # Path to your original image
    mask_image_path = "mask.png"  # Path to your mask image (binary)
    edit_prompt = "Add flying cars in the sky"
    
    edited_image_url = edit_image(original_image_path, mask_image_path, edit_prompt)
    save_image(edited_image_url, "edited_city.png")