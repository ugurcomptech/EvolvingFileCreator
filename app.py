import os
import time
import shutil

def create_file(file_path):
    """
    Belirtilen dosya yolunda yeni bir dosya oluşturur ve içine boş bir metin yazar.

    Args:
        file_path (str): Oluşturulacak dosya yolunu içeren dizgi.
    """
    with open(file_path, "w") as file:
        file.write("")

def increase_file_size(file_path, size_mb):
    """
    Belirtilen dosyanın boyutunu artırır.

    Args:
        file_path (str): Boyutu artırılacak dosyanın yolu.
        size_mb (int): Dosyanın artırılacak boyutu megabayt cinsinden.
    """
    with open(file_path, "ab+") as file:
        file.seek(0, os.SEEK_END)
        file.write(b"\0" * (size_mb * 1024 * 1024))

def main():
    """
    Ana işlemi yürüten fonksiyon.
    """
    folder_paths = ["G:\\Program2\\1", "G:\\Program1\\2"]  
    file_count = 5
    file_size_increase = 500  
    max_loop_count = 100  

    # Klasörleri oluştur ve dosyaları başlangıç boyutuyla oluştur
    for folder_path in folder_paths:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)

        for i in range(file_count):
            file_path = os.path.join(folder_path, f"ArtanBoyutluDosya_{i + 1}.txt")
            create_file(file_path)

    loop_count = 0
    while loop_count < max_loop_count:
        # Dosyaların boyutunu artır ve birbirine kopyala
        for folder_path in folder_paths:
            for i in range(file_count):
                file_path = os.path.join(folder_path, f"ArtanBoyutluDosya_{i + 1}.txt")
                increase_file_size(file_path, file_size_increase)

        for folder_path in folder_paths:
            for i in range(1, file_count):
                source_file = os.path.join(folder_path, f"ArtanBoyutluDosya_{i}.txt")
                target_file = os.path.join(folder_path, f"ArtanBoyutluDosya_{i + 1}.txt")
                shutil.copyfile(source_file, target_file)

        time.sleep(1)
        loop_count += 1

if __name__ == "__main__":
    main()
