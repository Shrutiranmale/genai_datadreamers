// Access the video element and canvas
const video = document.getElementById('camera');
const canvas = document.getElementById('canvas');
const capturedImage = document.getElementById('capturedImage');

async function startCamera() {
    try {
        // Request access to the camera
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        video.style.display = "block";
        
        // Display capture button to snap the photo from video feed
        document.querySelector('.generate-btn').textContent = "Capture Photo";
        document.querySelector('.generate-btn').onclick = captureImage;
    } catch (error) {
        console.error("Camera access error:", error);
        alert("Camera access is required to capture an image.");
    }
}

function captureImage() {
    // Set canvas dimensions to the video feed dimensions
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    // Draw the current frame from video to canvas
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Convert canvas content to an image and display it
    const imageDataURL = canvas.toDataURL('image/png');
    capturedImage.src = imageDataURL;
    capturedImage.style.display = "block";
    
    // Stop the camera stream
    video.srcObject.getTracks().forEach(track => track.stop());
    video.style.display = "none";
    document.querySelector('.generate-btn').textContent = "Generate Image";
    document.querySelector('.generate-btn').onclick = generateImage;
}

function generateImage() {
    alert("Image generated successfully!");
}
