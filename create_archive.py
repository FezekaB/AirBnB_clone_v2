import tarfile
from datetime import datetime
import os

def create_archive():
    # Define the web_static folder path
    web_static_path = '/path/to/your/web_static/folder'  # Replace with actual path

    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get the current time in the specified format
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{now}.tgz"
    archive_path = os.path.join("versions", archive_name)

    try:
        # Create the .tgz archive
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(web_static_path, arcname=os.path.basename(web_static_path))

        print(f"Archive created successfully: {archive_path}")
        return archive_path
    except Exception as e:
        print(f"Failed to create archive: {str(e)}")
        return None

# Call the function to create the archive
create_archive()

