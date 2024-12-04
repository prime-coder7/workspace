import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Define the username of the target account
username = "rf"

try:
    # Login to Instagram (optional, but needed for private profiles)
    # loader.login('your_username', 'your_password')

    # Download profile pictures, posts, and more from the account
    loader.download_profile(username, profile_pic_only=False)

    print(f"Successfully downloaded all posts from {username}.")

except instaloader.exceptions.InstaloaderException as e:
    print(f"Error occurred: {e}")
