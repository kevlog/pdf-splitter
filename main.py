import os
import sys
import time
from pypdf import PdfReader, PdfWriter

def split_all_pdfs_in_folder(folder_path):
    # Ambil semua file PDF dalam folder
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("[INFO] 🙏 Tidak ada file PDF ditemukan di folder ini.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        pdf_name = os.path.splitext(pdf_file)[0]  # Tanpa ekstensi

        # Buat folder output untuk file ini
        output_dir = os.path.join(folder_path, pdf_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"[INFO] ⚙️ Memproses: {pdf_file}...")

        # Buka dan pecah PDF
        reader = PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)

            output_filename = os.path.join(output_dir, f"{pdf_name}_page_{i+1}.pdf")
            with open(output_filename, "wb") as out_file:
                writer.write(out_file)

        print(f"[INFO] ✅ Selesai memecah: {pdf_file} -> {output_dir}")

# Contoh pemakaian
if __name__ == "__main__":
    folder = input("[INFO] 📂 Masukkan path folder berisi file PDF: ").strip()
    if os.path.isdir(folder):
        split_all_pdfs_in_folder(folder)
        for i in range(3, 0, -1):
            sys.stdout.write(f"\r[INFO] 🕒 Menutup aplikasi dalam {i} detik" + "." * (4 - i))
            sys.stdout.flush()
            time.sleep(1)
        exit()
    else:
        print("[ERR]  ⚠️ Path folder tidak valid.")
