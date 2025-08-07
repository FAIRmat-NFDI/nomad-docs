import os
import pytest

def find_unused_assets():
    """
    Finds unused assets in the docs/ directory.

    An asset is considered unused if it is not referenced in any markdown file
    in the same directory.
    """
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    unused_assets = []
    asset_dirs = ['images', 'data']

    for root, dirs, files in os.walk(docs_dir):
        md_text = ''
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    md_text += f.read()

        for asset_subdir in asset_dirs:
            asset_path = os.path.join(root, asset_subdir)
            if os.path.isdir(asset_path):
                for asset_file in os.listdir(asset_path):
                    full_path = os.path.join(asset_path, asset_file)
                    if os.path.isdir(full_path):
                        continue
                    if asset_file not in md_text:
                        rel_path = os.path.relpath(full_path, docs_dir)
                        unused_assets.append(rel_path)
    return unused_assets

def test_no_unused_assets():
    """
    Tests that there are no unused assets in the docs directory.
    """
    unused_assets = find_unused_assets()
    if unused_assets:
        message = f'Found {len(unused_assets)} unused assets:\n' + '\n'.join(f'- {asset}' for asset in unused_assets)
        assert not unused_assets, message
