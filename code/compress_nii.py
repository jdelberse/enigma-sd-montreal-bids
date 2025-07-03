import os
import nibabel as nib

def convert_nii_to_niigz(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        # Process only if any folder in the path starts with "sub-"
        if any(part.startswith("sub-") for part in dirpath.split(os.sep)):
            for file in filenames:
                if file.endswith(".nii") and not file.endswith(".nii.gz"):
                    nii_path = os.path.join(dirpath, file)
                    nii_gz_path = nii_path + ".gz"

                    try:
                        print(f"Converting: {nii_path} -> {nii_gz_path}")
                        img = nib.load(nii_path)
                        nib.save(img, nii_gz_path)
                        os.remove(nii_path)  # Comment this out if you want to keep original
                    except Exception as e:
                        print(f"Failed to convert {nii_path}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert .nii to .nii.gz in sub-* folders")
    parser.add_argument("root_dir", help="Root directory to search from")
    args = parser.parse_args()

    convert_nii_to_niigz(args.root_dir)