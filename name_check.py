import os

def snake_to_kebab(name):
    base, ext = os.path.splitext(name)
    if "_" in base:
        new_base = base.replace("_", "-")
        return new_base + ext
    return name

def rename_files_in_dir(directory):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # Skip directories
        if not os.path.isfile(old_path):
            continue

        new_name = snake_to_kebab(filename)
        new_path = os.path.join(directory, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    directory = "./JS Front End/JS Syntax Fundamentals - Exercises"
    rename_files_in_dir(directory)
