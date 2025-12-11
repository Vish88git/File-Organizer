# 🗂️ File Organizer Bot

A simple and beginner-friendly Python script that automatically organizes files in any folder by grouping them into subfolders based on file type (Images, Documents, Music, Archives, Others).

Perfect for cleaning up messy Downloads or Desktop folders!

---

## 🚀 Features

- Detects each file's extension  
- Classifies files into categories (Images, Documents, Music, Archives, Others)  
- Creates category folders automatically if needed  
- Moves files into the correct folders  
- Works on any folder the user selects  
- Clean and modular Python code (easy to understand)

---

## 📦 Requirements

- Python 3 installed  
- Works on Windows, macOS, or Linux  
- No external libraries needed (uses built-in `pathlib` and `shutil`)

---

## 🧠 How to Run the File Organizer Bot

Follow these simple steps to run the script on any machine.

---

### **1️⃣ Open a terminal**

You can use:

- **VS Code Terminal**  
  Press <kbd>Ctrl</kbd> + <kbd>`</kbd>  
  or go to **Terminal → New Terminal**

OR

- **Command Prompt / PowerShell**  
  Press <kbd>Win</kbd> + <kbd>R</kbd> → type `cmd` → press Enter

---

### **2️⃣ Navigate to the folder containing this script**

Example (change path based on your setup):

```bash
cd "C:\Users\Admin\Python-VSCode\Python Projects\Organizer_1"
Use quotes if the folder path contains spaces.

3️⃣ Run the script
bash
Copy code
python File_organizer.py
This starts the File Organizer Bot.

4️⃣ Enter the folder you want to organize
When the script asks:

css
Copy code
Enter the path of the folder to organize:
Paste any folder path, for example:

makefile
Copy code
C:\Users\Admin\Desktop\Playground
Then press Enter.

5️⃣ What happens next
The script will:

Detect each file’s extension

Create category folders (Images, Documents, Music, Archives, Others)

Move each file into the correct folder

Show progress in the terminal

Finish with:

nginx
Copy code
Done organizing! ✅
📁 Example Output
yaml
Copy code
Looking Inside: C:\Users\Admin\Desktop\Playground
Creating Folder: C:\Users\Admin\Desktop\Playground\Images
Moving: photo1.jpg → Images/
Creating Folder: C:\Users\Admin\Desktop\Playground\Documents
Moving: resume.pdf → Documents/
Creating Folder: C:\Users\Admin\Desktop\Playground\Music
Moving: song.mp3 → Music/
Done organizing! ✅
💡 Future Improvements (Optional Ideas)
Add a dry-run mode (shows actions without moving files)

Add a GUI version using Tkinter

Add a log file showing moved files

Allow custom category mapping via a config file

Version with drag-and-drop folder selection

📜 License
This project is open-source and free to use for learning.

👨‍💻 Author
Made by Vishwas as part of a Python learning journey and GitHub portfolio building.
Contributions, suggestions, and issues are welcome!