# 🏆 Certificate Generator

A **Python-based tool** to generate personalized certificates in bulk by printing participant names from a CSV file onto a provided PDF template.

> **From CSV to certificate — fast and effortless.**

---

## 📌 Features

- Generate certificates in bulk using a CSV file of names
- Automatically centers and scales text to fit the certificate
- Supports custom fonts and templates
- Outputs individual PDF files for each name

---

## 🛠️ Requirements

- Python 3.x  
- Libraries:
  - `PyPDF2`
  - `reportlab`

Install the required libraries with:

```bash
pip install PyPDF2 reportlab
```

---

## 📂 Folder Structure

```
.
├── canva_template4.pdf        # Your certificate design template
├── names4.csv                 # CSV file with participant names
├── certificates/              # Folder where generated certificates are saved
└── certificate_generator.py   # Main Python script
```

---

## 🖨️ Usage

1. Rename your CSV file with names to `names4.csv` (or change the filename in the script).
2. Replace `canva_template4.pdf` with your certificate template.
3. Run the script:

```bash
python certificate_generator.py
```

All generated certificates will appear in the `certificates/` folder.

---

## 🎨 Customization

- Adjust `name_y` in the script to change vertical placement of the name.
- Font defaults to **Arial**, but uses **Montserrat-Bold** if not available.
- Text is auto-scaled to fit long names within the template width.


