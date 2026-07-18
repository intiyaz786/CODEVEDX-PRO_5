import os
import shutil

# ==========================================
# TASK AUTOMATION TOOL - FILE ORGANIZER
# ==========================================

# Change this path to your folder
SOURCE_FOLDER = input("Enter Folder Path: ")

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Programs": [".exe", ".msi"],
    "Python": [".py"],
    "Compressed": [".zip", ".rar", ".7z"],
}


def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("\nFolder not found!")
        return

    moved = 0

    for file in os.listdir(SOURCE_FOLDER):

        filepath = os.path.join(SOURCE_FOLDER, file)

        if os.path.isdir(filepath):
            continue

        extension = os.path.splitext(file)[1].lower()

        destination = "Others"

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination = folder
                break

        destination_folder = os.path.join(SOURCE_FOLDER, destination)

        create_folder(destination_folder)

        shutil.move(filepath, os.path.join(destination_folder, file))

        print(f"Moved: {file} ---> {destination}")

        moved += 1

    print("\n================================")
    print("Automation Completed Successfully")
    print("Total Files Moved:", moved)
    print("================================")


try:
    organize_files()

except PermissionError:
    print("Permission Denied!")

except Exception as e:
    print("Error:", e)