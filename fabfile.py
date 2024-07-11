from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get the current time in the specified format
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)

    # Create the archive
    result = c.local("tar -cvzf {} web_static".format(archive_path), capture=True)

    # Check if the archive was created successfully
    if result.ok:
        return archive_path
    else:
        return None

