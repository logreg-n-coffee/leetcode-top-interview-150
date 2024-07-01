import os

def update_file_numbering(base_dir, directories, increment):
    """
    Automatically renames files in specified directories by incrementing their numbering.
    
    :param base_dir: str - the base directory where subdirectories are located
    :param directories: list - a list of directory names to process
    :param increment: int - the value to increment the file numbering by
    """
    for subdir in directories:
        full_dir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(full_dir_path):
            print(f"Directory not found: {full_dir_path}")
            continue
        
        for filename in os.listdir(full_dir_path):
            if filename.endswith('.ipynb'):
                parts = filename.split('-')
                try:
                    number = int(parts[0])
                except ValueError:
                    continue  # Skip files that don't start with a number
                
                rest_of_name = '-'.join(parts[1:])
                new_number = number + increment
                new_filename = f"{new_number}-{rest_of_name}"
                old_path = os.path.join(full_dir_path, filename)
                new_path = os.path.join(full_dir_path, new_filename)
                
                # Rename the file using os.rename
                os.rename(old_path, new_path)
                print(f"Renamed '{old_path}' to '{new_path}'")

# List of directories to renumber files within
directories_to_process = [
    "7-stack", 
    "8-linked-list", 
    "9-binary-tree-general", 
    "10-binary-tree-bfs", 
    "11-graph-general", 
    "12-graph-bfs", 
    "13-trie",
    "14-backtracking", 
    "15-divide-and-conquer", 
    "16-kadanes-algorithm", 
    "17-binary-search", 
    "18-heap", 
    "19-bit-manipulation", 
    "20-math", 
    "21-1d-dp", 
    "22-multidimensional-dp"
]

# Base directory where these directories are located
base_directory = "./"  # Adjust this path to your local setup

# Generate the rename
update_file_numbering(base_directory, directories_to_process, 2)
