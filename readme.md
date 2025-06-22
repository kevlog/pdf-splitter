# PDF Splitter

A simple command-line tool to split PDF files into smaller chunks.

## ✅ Features
- Automatically splits each page of a PDF into its own file
- Processes **all PDF files in a folder**, not just one
- For each PDF, creates a new output folder with the **same name as the file**
- Saves each split page inside the corresponding folder
- Lightweight and easy to use from the command line (CMD)
- No need for external GUI or complex setup

## Example of Hierarki Folder After Running this Tool
```
FOLDER_PDF/
├── file1.pdf
├── file2.pdf
├── file1/
│   ├── file1_page_1.pdf
│   ├── file1_page_2.pdf
│   └── ...
└── file2/
    ├── file2_page_1.pdf
    ├── file2_page_2.pdf
    └── ...
```

## 📦 Requirements

- Python 3.x
- `pypdf` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kevlog/pdf-splitter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf-splitter
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Split PDF by Page Range

To split a PDF file by a specific page range, use the following command:

```bash
python main.py
```

## Convert to exe

1. pyinstaller --onefile main.py
2. Run main.exe in dist folder

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.