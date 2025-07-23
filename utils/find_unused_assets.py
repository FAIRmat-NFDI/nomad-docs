import os

# Get absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the 'docs/' folder
docs_dir = os.path.normpath(os.path.join(script_dir, "..", "docs"))

# Subfolders to scan for assets
asset_dirs = ["images", "data"]

unused_assets = []

# Traverse all subdirectories under 'docs/'
for root, dirs, files in os.walk(docs_dir):
    # Gather all markdown content in this folder (non-recursive)
    md_text = ""
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                md_text += f.read()

    # Look in 'images/' and 'data/' subdirectories (non-recursive)
    for asset_subdir in asset_dirs:
        asset_path = os.path.join(root, asset_subdir)
        if os.path.isdir(asset_path):
            for asset_file in os.listdir(asset_path):
                full_path = os.path.join(asset_path, asset_file)
                # Skip folders (you can make this recursive if needed)
                if os.path.isdir(full_path):
                    continue
                # If asset filename is not mentioned in any markdown content in this folder
                if asset_file not in md_text:
                    rel_path = os.path.relpath(full_path, docs_dir)
                    unused_assets.append(rel_path)

# Output results
if unused_assets:
    print("Unreferenced assets found:\n")
    for path in unused_assets:
        print(f"- {path}")
else:
    print("All assets are referenced.")
