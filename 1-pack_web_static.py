#!/usr/bin/python3
"""Creates a .tgz archive from web_static folder."""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generate a .tgz archive from web_static folder.

    Returns:
        str: Archive path if success, None otherwise.
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        print(f"Packing web_static to {archive_path}")
        result = local(f"tar -cvzf {archive_path} web_static", capture=True)
        if result.succeeded:
            print(f"web_static packed: {archive_path}")
            return archive_path
        return None

    except Exception:
        return None
