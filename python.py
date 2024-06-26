html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Gallery</title>
    <style>
        /* Global Styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f3f3f3;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Heading Styles */
        .heading {
            text-align: center;
            margin-bottom: 40px;
        }

        .heading h1 {
            font-size: 36px;
            color: #007bff;
            margin: 0;
            padding: 10px 0;
        }

        /* Gallery Styles */
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }

        .gallery-box {
            position: relative;
            flex: 0 0 calc(33.33% - 20px);
            max-width: calc(33.33% - 20px);
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .gallery-box img {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 10px;
            transition: transform 0.3s; /* Added transition for zoom effect */
        }

        /* Zoom effect on hover */
        .gallery-box:hover img {
            transform: scale(1.1); /* Zoom in on hover */
        }

        /* Download button styles */
        .download-btn {
            position: absolute;
            bottom: 10px;
            right: 10px;
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            transition: background-color 0.3s;
            text-decoration: none;
            color: black;
            z-index: 1; /* Ensure button is above image */
        }

        .download-btn:hover {
            background-color: rgba(255, 255, 255, 1);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heading">
            <h1>Welcome to <span style="color: #ff6b6b;">Rodan's</span> Professional Gallery</h1>
        </div>
        <div class="gallery" id="gallery">
            <!-- Images will be added dynamically using JavaScript -->
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // Array of image URLs
            var imageUrls = [
                "1.jpg",
                "2.jpg",
                "3.jpg",
                // Add more image URLs here
                "33.jpg"
            ];

            // Get the gallery container
            var gallery = document.getElementById("gallery");

            // Loop through each image URL and create gallery box
            imageUrls.forEach(function(imageUrl, index) {
                // Create gallery box
                var galleryBox = document.createElement("div");
                galleryBox.classList.add("gallery-box");

                // Create link for modal
                var modalLink = document.createElement("a");
                modalLink.setAttribute("href", "#modal" + (index + 1));

                // Create image element
                var image = document.createElement("img");
                image.setAttribute("src", imageUrl);
                image.setAttribute("alt", "Image " + (index + 1));

                // Create download button
                var downloadBtn = document.createElement("button");
                downloadBtn.classList.add("download-btn");
                downloadBtn.textContent = "Download";
                downloadBtn.addEventListener("click", function() {
                    // Create a temporary anchor element
                    var tempAnchor = document.createElement("a");
                    tempAnchor.href = imageUrl;
                    tempAnchor.setAttribute("download", "");
                    tempAnchor.click();
                });

                // Append image and download button to modal link
                modalLink.appendChild(image);
                modalLink.appendChild(downloadBtn);

                // Append modal link to gallery box
                galleryBox.appendChild(modalLink);

                // Append gallery box to gallery container
                gallery.appendChild(galleryBox);
            });
        });
    </script>
</body>
</html>
"""

print(html_code)