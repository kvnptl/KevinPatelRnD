import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def move_file(file_path, destination_dir):
    """
    Move a file from its current location to a destination directory.
    
    Parameters:
        file_path (str): The full path of the file to move.
        destination_dir (str): The directory where the file will be moved.
        
    Returns:
        None
    """
    try:
        # Create the destination path by combining the destination directory and the file name
        destination = os.path.join(destination_dir, os.path.basename(file_path))
        
        # Move the file
        shutil.move(file_path, destination)
        print(f"Moved {file_path} to {destination}")
        
    except Exception as e:
        print(f"Failed to move {file_path}: {e}")

def main():
    """
    Main function to execute the file moving operation.
    """
    # Source directory: The directory from where the files will be moved
    source_dir = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/SeeingThroughFog_ONLY_ZIP"
    
    # Destination directory: The directory where the files will be moved
    destination_dir = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/SeeingThroughFog_ONLY_ZIP"  # Replace with your specific destination directory

    # Initialize an empty list to store file paths
    file_paths = []
    
    # Walk through the source directory to find all files
    for root, dirs, files in os.walk(source_dir):
        # Skip the source directory itself
        if root != source_dir:
            for file in files:
                # Append each file path to the list
                file_paths.append(os.path.join(root, file))

    # Move files in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Partial function application to set the second argument (destination_dir) of move_file function
        executor.map(lambda file_path: move_file(file_path, destination_dir), file_paths)

if __name__ == "__main__":
    main()
