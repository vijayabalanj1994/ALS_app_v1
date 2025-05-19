from torchcam.methods import GradCAM
from torchcam.utils import overlay_mask
from torchvision.transforms.functional import to_pil_image
import torch
import numpy as np
import cv2
from PIL import Image, ImageDraw


def extract_cam_and_image(model, image_tensor, class_idx, target_layer="features.denseblock4"):

    cam_extractor = GradCAM(model.model, target_layer=target_layer)
    output = model(image_tensor)
    cam = cam_extractor(class_idx, output)[0]

    # De-normalize image
    denorm_img = image_tensor.squeeze().clone()
    mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    denorm_img = denorm_img * std + mean
    original_image = to_pil_image(denorm_img.clamp(0, 1))

    return cam, original_image

def generate_gradcam_overlay(cam, original_image):

    overlay = overlay_mask(original_image, to_pil_image(cam, mode="F"))
    return overlay

def generate_gradcam_circles(cam, original_image, threshold=0.8):

    if torch.is_tensor(cam):
        cam = cam.detach().cpu().squeeze().numpy()

    # Resize and normalize CAM
    cam_resized = Image.fromarray(np.uint8(cam * 255)).resize(original_image.size, Image.BILINEAR)
    cam_array = np.array(cam_resized) / 255.0
    binary_mask = (cam_array >= threshold).astype(np.uint8)

    # Detect contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw circles
    draw = ImageDraw.Draw(original_image)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2
        r = max(w, h) // 2 + 4
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline="yellow", width=3)

    return original_image