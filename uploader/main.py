from wordpress_uploader_class import wordpress_uploader
import os
from dotenv import load_dotenv
load_dotenv()
image_path = "/Users/mmachkou/Documents/wordpress_poster/uploader/a.png"
wordpress_url = "https://theitcompare.com"
wordpress_username = os.environ.get("wordpress_username")
wordpress_application_password = os.environ.get("wordpress_application_password")



title = "hhhhhhhh Post Title"
content = ''' 
    <div class="post-container">
        <h1 style="post-header-title">hello world</h1>
        <p> this is just a test paragraph </p>
        <div class="post-body-container">
            <div style="flex-basis: 25%;background: red;"></div>
            <div style="flex-basis: 25%;background:blue"></div>
            <div style="flex-basis: 25%;background: yellow"></div>
            <div style="flex-basis: 25%;background: green"></div>
        </div>
    </div>
  '''
  
if __name__ == "__main__":
    
    Uploader = wordpress_uploader(wordpress_url, wordpress_username, wordpress_application_password, image_path=image_path)
    Uploader.create_post_with_featured_image(title, content)