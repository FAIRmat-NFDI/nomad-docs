import os
import argparse
import shutil

# --- Argument parsing ---
parser = argparse.ArgumentParser(
    description="Find (and optionally remove) unreferenced assets in docs/"
)
parser.add_argument(
    "--remove", action="store_true", help="Move unreferenced assets to .trash/"
)
parser.add_argument(
    "--empty-trash", action="store_true", help="Permanently delete all files in .trash/"
)
args = parser.parse_args()

# --- Setup paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.normpath(os.path.join(script_dir, ".."))
docs_dir = os.path.join(root_dir, "docs")
trash_dir = os.path.join(root_dir, ".trash")

asset_dirs = ["images", "data"]
unused_assets = []

# --- Empty trash if requested ---
if args.empty_trash:
    if os.path.exists(trash_dir):
        shutil.rmtree(trash_dir)
        print(".trash/ has been permanently emptied.")
    else:
        print(".trash/ is already empty or does not exist.")
    exit(0)

# --- Scan docs/ tree for unreferenced assets ---
for root, dirs, files in os.walk(docs_dir):
    # Collect Markdown text in current folder
    md_text = ""
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                md_text += f.read()

    # Check assets in images/ and data/
    for asset_subdir in asset_dirs:
        asset_path = os.path.join(root, asset_subdir)
        if os.path.isdir(asset_path):
            for asset_file in os.listdir(asset_path):
                full_path = os.path.join(asset_path, asset_file)
                if os.path.isdir(full_path):
                    continue  # Skip folders
                if asset_file not in md_text:
                    rel_path = os.path.relpath(full_path, docs_dir)
                    unused_assets.append((rel_path, full_path))

# --- Handle results ---
if unused_assets:
    if args.remove:
        print("Moving unreferenced assets to .trash/:\n")
        os.makedirs(trash_dir, exist_ok=True)
        for rel_path, full_path in unused_assets:
            dest_path = os.path.join(trash_dir, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.move(full_path, dest_path)
            print(f"- {rel_path}")
        print("\nUnused assets moved to .trash/")
        print(
            "   Use `python utils/find_unused_assets.py --empty-trash` to permanently remove them."
        )
    else:
        print("Unreferenced assets found:\n")
        for rel_path, _ in unused_assets:
            print(f"- {rel_path}")
else:
    print("All assets are referenced.")
