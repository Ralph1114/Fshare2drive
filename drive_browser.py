import subprocess
import json
import os

def browse_drive(remote="gdrive"):
    current_path = ""
    while True:
        full_path = f"{remote}:{current_path}" if current_path else f"{remote}:"
        try:
            result = subprocess.run(["rclone", "lsjson", full_path], capture_output=True, text=True, check=True)
            entries = json.loads(result.stdout)
            folders = [entry for entry in entries if entry["IsDir"]]
            if not folders:
                print("Không còn thư mục con. Đã chọn:", current_path or "/")
                return current_path.strip("/")
            print(f"📁 Đang trong thư mục: /{current_path.strip('/')}")
            for i, folder in enumerate(folders, 1):
                print(f"{i}. {folder['Name']}/")
            choice = input("Chọn (số thứ tự) hoặc Enter để chọn thư mục hiện tại: ").strip()
            if not choice:
                return current_path.strip("/")
            if choice.isdigit() and 1 <= int(choice) <= len(folders):
                current_path = os.path.join(current_path, folders[int(choice) - 1]['Name'])
            else:
                print("❌ Lựa chọn không hợp lệ.")
        except Exception as e:
            print("❌ Lỗi khi truy cập Google Drive:", e)
            return current_path.strip("/")
