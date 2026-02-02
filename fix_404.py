"""
Adjusts asset paths in the 404.html file after the build process.

Specifically prepends a site-absolute prefix to 'assets/', 'stylesheets/',
and 'javascript.js' links to ensure they resolve correctly when the
404 page is served from a sub-directory.
"""

import os
import re


def on_post_build(config, **kwargs):
    file_path = os.path.join(config["site_dir"], "404.html")

    if not os.path.exists(file_path):
        raise FileNotFoundError("404.html file cannot be found.")

    with open(file_path) as f:
        content = f.read()

    # Site-absolute prefix for NOMAD
    # TODO: is there a way not to hard code this?
    prefix = "/nomad-oasis/docs/"

    # Find links starting with 'assets/' or 'stylesheets/' or 'javascript.js'
    # and prepend the prefix.
    content = re.sub(
        r'(href|src)="(assets/|stylesheets/|javascript.js)',
        rf'\1="{prefix}\2',
        content,
    )

    with open(file_path, "w") as f:
        f.write(content)
