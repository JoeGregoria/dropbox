"""
Pull down everything from my personal dropbox to my current directory
"""
import os

import dropbox_upload

if __name__ == '__main__':
    dropbox_pull_source = ""
    dropbox_pull_target = os.path.abspath(os.path.join(os.getcwd(), "dropbox_download"))
    print(f"Downloading {dropbox_pull_source} to {dropbox_pull_target}")

    dropbox_upload.set_logging_level("debug", dropbox_upload.logger)

    total_files, total_folders = dropbox_upload.agc_download_directory(dropbox_pull_source, dropbox_pull_target, interactive=True, use_team_root=False)
    print(f"Total files downloaded: {total_files}")
