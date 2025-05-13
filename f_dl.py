from drive_browser import browse_drive

def main():
    selected_path = browse_drive()
    print("✅ Đường dẫn bạn chọn:", selected_path)

if __name__ == "__main__":
    main()
