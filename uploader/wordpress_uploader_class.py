import requests

class wordpress_uploader:
    def __init__(self, wordpress_url, wordpress_username, wordpress_application_password, image_path=None):
        self.wordpress_application_password = wordpress_application_password
        self.wordpress_username = wordpress_username
        self.wordpress_url = wordpress_url
        self.image_path = image_path
        self.image_id = None
    
    def upload_image_to_wordpress(self, image_path):
        auth = (self.wordpress_username, self.wordpress_application_password)
        headers = {
            "Content-Disposition": "attachment; filename=image.jpg"
        }

        files = {'file': open(image_path, 'rb')}

        response = requests.post(
            f"{self.wordpress_url}/wp-json/wp/v2/media",
            auth=auth,
            headers=headers,
            files=files
        )

        if response.status_code == 201:
            self.image_id = response.json()["id"]
            print(f"Image uploaded successfully. Image ID: {self.image_id}")
        else:
            print(f"Failed to upload image. Status code: {response.text}")

    def create_post_with_featured_image(self, title, content):
        self.upload_image_to_wordpress(self.image_path)
        
        if self.image_id is None:
            print("Post creation aborted. image not uploaded")
            return

        auth = (self.wordpress_username, self.wordpress_application_password)

        data = {
            "title": title,
            "content": content,
            "status": "publish",
            "featured_media": self.image_id
        }

        response = requests.post(
            f"{self.wordpress_url}/wp-json/wp/v2/posts",
            auth=auth,
            json=data
        )

        if response.status_code == 201:
            print("Post created successfully.")
        else:
            print(f"Failed to create post. Status code: {response.status_code}")

