import pandas as pd
import os

# Function to generate an HTML page with menu and blog content
def generate_html_with_blog(csv_file, blog_text_files, output_html_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Start the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .container {
                display: flex;
                flex-direction: row;
            }
            .menu {
                width: 25%;
                background-color: #f4f4f4;
                padding: 10px;
            }
            .blog {
                width: 75%;
                padding: 20px;
            }
            .menu ul {
                list-style-type: none;
                padding: 0;
            }
            .menu li {
                margin-bottom: 10px;
            }
            .menu a {
                text-decoration: none;
                color: black;
                font-weight: bold;
            }
            .blog img {
                max-width: 100%;
                height: auto;
            }
        </style>
        <title>Menu and Blog Page</title>
    </head>
    <body>
        <div class="container">
            <div class="menu">
                <h2>Menu</h2>
                <ul>
    """

    # Add each link and name from the CSV file to the HTML content (menu)
    for index, row in df.iterrows():
        link = row[0]
        name = row[1]
        html_content += f'                    <li><a href="{link}">{name}</a></li>\n'

    # Close the menu section and start the blog section
    html_content += """
                </ul>
            </div>
            <div class="blog">
    """

    # Loop through each blog text file and add content to the blog section
    for i, blog_file in enumerate(blog_text_files, start=1):
        blog_title = f"Blog {i}"
        blog_image_prefix = f"{i}_blog_image"  # Images will be like '1_blog_image1.jpg', '2_blog_image1.jpg', etc.

        # Read the blog text from file
        if os.path.exists(blog_file):
            with open(blog_file, 'r') as file:
                blog_content = file.read()
        else:
            blog_content = "Blog content not found."

        # Add the blog title, content, and images
        html_content += f"""
                <h2>{blog_title}</h2>
                <p>{blog_content}</p>
        """

        # Add images for the blog (assuming image filenames are in the format '1_blog_image1.jpg', '2_blog_image1.jpg', etc.)
        for img_num in range(1, 4):  # Assuming each blog may have up to 3 images
            image_path = f'{blog_image_prefix}{img_num}.jpg'
            if os.path.exists(image_path):
                html_content += f'<img src="{image_path}" alt="Image {img_num} for Blog {i}">\n'

    # Close the blog section and HTML tags
    html_content += """
            </div>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_html_file, 'w') as file:
        file.write(html_content)

    print(f'HTML file "{output_html_file}" generated successfully!')

# Example usage
csv_file = 'website_pages.csv'  # Replace with the path to your CSV file
blog_text_files = ['1_blog.txt', '2_blog.txt']  # List of blog text files
output_html_file = 'index2.html'

generate_html_with_blog(csv_file, blog_text_files, output_html_file)
