from PIL import Image, ImageDraw, ImageFont

# Open the images
ground_truth = Image.open("ground.png")
predicted = Image.open("predicted.png")

# Resize predicted to match ground_truth dimensions
predicted = predicted.resize(ground_truth.size)

# Create a new image with a white background
combined_width = ground_truth.width
combined_height = ground_truth.height + predicted.height
combined_image = Image.new('RGBA', (combined_width, combined_height), (255, 255, 255, 255))

# Paste the ground truth image at the top
combined_image.paste(ground_truth, (0, 0))

# Paste the predicted image below the ground truth image
combined_image.paste(predicted, (0, ground_truth.height))

# Add labels to the images
draw = ImageDraw.Draw(combined_image)
font_size = 24
font = ImageFont.load_default()
label_height = font.getsize("Text")[1]

# Ground Truth label
draw.text((10, ground_truth.height - label_height - 10), "Ground Truth", (0, 0, 0), font=font)

# Predicted label
draw.text((10, combined_height - label_height - 10), "Predicted", (0, 0, 0), font=font)

# Save the combined image with labels to a file
output_combined_image_path = "/mnt/data/combined_image_with_labels.png"
combined_image.save(output_combined_image_path)

output_combined_image_path