import cv2
import numpy as np
import os

# Load YOLO pre-trained model for vehicle detection
net = cv2.dnn.readNet("yolov7.weights", "yolov7.cfg")

# Load the COCO names file (contains class names)
classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Path to the directory containing the images
image_dir = "test_images/"
output_dir = "output_images/"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each image
for i in range(1, 5):  # Loop over images 1.jpg, 2.jpg, and 3.jpg
    # Load the image
    image_path = image_dir + str(i) + ".jpg"
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = image.shape

    # Preprocess the image for YOLO
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Set input blob for the network
    net.setInput(blob)

    # Get output layer names
    output_layers = net.getUnconnectedOutLayersNames()

    # Perform forward pass and get detections
    detections = net.forward(output_layers)

    # Loop through detections
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:  # Check confidence threshold
                label = classes[class_id]
                if label == 'car' or label == 'bus' or label == 'truck':
                    center_x = int(obj[0] * width)
                    center_y = int(obj[1] * height)
                    w = int(obj[2] * width)
                    h = int(obj[3] * height)
                    
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)

    # Display the image with detections
    cv2.imshow("Vehicle Detection", image)
    cv2.waitKey(0)

    # Save the output image
    output_path = output_dir + "output_" + str(i) + ".jpg"
    cv2.imwrite(output_path, image)

# Destroy all windows after processing
cv2.destroyAllWindows()
