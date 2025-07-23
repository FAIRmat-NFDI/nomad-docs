import os
import argparse

# --- Argument parsing ---
parser = argparse.ArgumentParser(
    description="Find (and optionally remove) unreferenced assets in docs."
)
parser.add_argument("--remove", action="store_true", help="Remove unreferenced assets")
args = parser.parse_args()

# --- Setup paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
docs_dir = os.path.normpath(os.path.join(script_dir, "..", "docs"))
asset_dirs = ["images", "data"]

unused_assets = []

# --- Scan docs/ tree ---
for root, dirs, files in os.walk(docs_dir):
    # Gather all markdown text in this folder
    md_text = ""
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                md_text += f.read()

    # Look in images/ and data/ folders
    for asset_subdir in asset_dirs:
        asset_path = os.path.join(root, asset_subdir)
        if os.path.isdir(asset_path):
            for asset_file in os.listdir(asset_path):
                full_path = os.path.join(asset_path, asset_file)
                if os.path.isdir(full_path):
                    continue  # skip subfolders
                if asset_file not in md_text:
                    rel_path = os.path.relpath(full_path, docs_dir)
                    unused_assets.append((rel_path, full_path))

# --- Output results ---
if unused_assets:
    if args.remove:
        print("Removing unreferenced assets:\n")
    else:
        print("Unreferenced assets found:\n")

    for rel_path, full_path in unused_assets:
        print(f"- {rel_path}")
        if args.remove:
            try:
                os.remove(full_path)
            except Exception as e:
                print(f"  Failed to delete {rel_path}: {e}")
else:
    print("All assets are referenced.")
