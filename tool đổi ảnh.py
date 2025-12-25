import os
from tkinter import Tk, Button, Label, messagebox, filedialog
from PIL import Image

SUPPORTED_EXT = ('.jpg', '.jpeg', '.bmp', '.webp', '.gif', '.tiff', '.png')

def convert_and_rename(folder_path):
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(SUPPORTED_EXT)
    ]

    if not files:
        messagebox.showwarning("Không có ảnh", "Thư mục không chứa ảnh hợp lệ")
        return

    files.sort()  # Sắp xếp theo tên cũ

    index = 1
    errors = 0

    for file in files:
        old_path = os.path.join(folder_path, file)

        try:
            img = Image.open(old_path)
            img = img.convert("RGBA")

            new_name = f"{index}.png"
            new_path = os.path.join(folder_path, new_name)

            img.save(new_path, "PNG")

            # Xóa file cũ nếu không trùng tên
            if old_path != new_path:
                os.remove(old_path)

            index += 1

        except Exception as e:
            print("Lỗi:", file, e)
            errors += 1

    messagebox.showinfo(
        "Hoàn thành",
        f"Đã xử lý {index - 1} ảnh\nLỗi: {errors}"
    )

def choose_folder():
    folder = filedialog.askdirectory(title="Chọn thư mục chứa ảnh")
    if folder:
        confirm = messagebox.askyesno(
            "Xác nhận",
            "Ảnh gốc sẽ bị xóa và đổi tên.\nBạn có chắc chắn?"
        )
        if confirm:
            convert_and_rename(folder)

# ===== GUI =====
root = Tk()
root.title("Tool đổi tên & chuyển PNG")
root.geometry("380x180")
root.resizable(False, False)

Label(
    root,
    text="Chọn thư mục ảnh\nTool sẽ đổi tên + chuyển sang PNG",
    font=("Segoe UI", 10),
    pady=20
).pack()

Button(
    root,
    text="📂 Chọn thư mục & Thực hiện",
    font=("Segoe UI", 10, "bold"),
    width=32,
    height=2,
    command=choose_folder
).pack()

root.mainloop()
