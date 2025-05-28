from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Archive is stored in the versions directory.
    Returns the archive path if successful, or None otherwise.
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create timestamp format
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        # Compress the web_static folder into the archive
        print(f"Packing web_static to {archive_path}")
        result = local(f"tar -cvzf {archive_path} web_static", capture=True)

        if result.succeeded:
            print(f"web_static packed: {archive_path}")
            return archive_path
        else:
            return None

    except Exception as e:
        return None
