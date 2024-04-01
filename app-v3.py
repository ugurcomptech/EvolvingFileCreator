import os
import time
import logging
import win32api
import win32con

logging.basicConfig(level=logging.INFO)

def create_file(file_path):
    try:
        with open(file_path, "x"):
            pass
        win32api.SetFileAttributes(file_path, win32con.FILE_ATTRIBUTE_HIDDEN)
    except FileExistsError:
        pass

def increase_file_size(file_path, size_mb):
    with open(file_path, "ab+") as file:
        file.seek(0, os.SEEK_END)
        file.write(b"\0" * (size_mb * 1024 * 1024))

def copy_files(source_path, target_path, file_count):
    for i in range(1, file_count):
        source_file = os.path.join(source_path, f"ArtanBoyutluDosya_{i}.txt")
        target_file = os.path.join(target_path, f"ArtanBoyutluDosya_{i + 1}.txt")

        try:
            with open(source_file, "rb") as src_file, open(target_file, "wb") as dest_file:
                dest_file.write(src_file.read())
        except FileNotFoundError:
            pass

def main(file_count=1, file_size_increase=500, max_loop_count=100):
    folder_paths = ["F:\\Script1\\1"]
    
    for folder_path in folder_paths:
        os.makedirs(folder_path, exist_ok=True)
        for i in range(file_count):
            file_path = os.path.join(folder_path, f"ArtanBoyutluDosya_{i + 1}.txt")
            create_file(file_path)

    loop_count = 0
    while loop_count < max_loop_count:
        for folder_path in folder_paths:
            for i in range(file_count):
                file_path = os.path.join(folder_path, f"ArtanBoyutluDosya_{i + 1}.txt")
                increase_file_size(file_path, file_size_increase)

            copy_files(folder_path, folder_path, file_count)

        logging.info(f"Loop {loop_count + 1}: Files processed.")
        time.sleep(1)
        loop_count += 1

if __name__ == "__main__":
    main()
