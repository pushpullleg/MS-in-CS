---

## title: "Automating Downloads Folder on macOS" date: 2025-04-23 tags: [automation, applescript, macos, productivity, obsidian-log, cs-journey]

## 🧐 Automation Journal: Organizing Downloads Folder on macOS with AppleScript

### 🗓️ Date: April 23, 2025

### 🧑‍💻 Authored by: Tejaswini D. Kannan

---

### 📌 Goal

Automate the organization of files downloaded into the `~/Downloads` folder by:

- Categorizing files based on their extensions (PDFs, Images, Docs, etc.)
    
- Automatically moving them into subfolders
    
- Later: Logging file activity to a `README.txt` inside each subfolder
    

---

### 🔍 Discovery Path

1. **Initial Curiosity**  
    Noticed a `Folder Action` option when right-clicking a folder on macOS.  
    Explored a sample AppleScript from Apple (2002–2007) that triggered a dialog box when items were added.
    
2. **Idea Sparked**  
    Realized I could **repurpose Folder Actions** to:
    
    - Auto-organize my messy Downloads folder
        
    - Improve my productivity and file hygiene
        
    - Treat automation like a mini side-project
        
3. **Script Creation**
    
    - Used **Script Editor** on macOS
        
    - Wrote an AppleScript to:
        
        - Detect new files
            
        - Read the file extension
            
        - Create subfolders (`PDFs`, `Images`, `Docs`, etc.)
            
        - Move files accordingly
            
4. **Setup Challenges**
    
    - **Script not showing up** in Folder Actions setup
        
    - Discovered I needed to move the script to:  
        `~/Library/Scripts/Folder Action Scripts`
        
    - Manually created this folder, then successfully added the script via:  
        `Right-click Downloads > Folder Actions Setup`
        
5. **Success 🎉**  
    Dropped sample files into `Downloads` → Instantly sorted into the correct subfolders.  
    No more clutter. Felt like magic ✨
    

---

### 📌 Learnings

- macOS **Folder Actions** are super underrated
    
- Folder Action scripts must live in `~/Library/Scripts/Folder Action Scripts` to be recognized
    
- AppleScript is quirky but effective for automation
    
- This kind of automation can be layered: next up — **logging file activity**
    

---

### 🔧 Tech Used

- **macOS Sonoma (v15)**
    
- **Script Editor** (built-in)
    
- **AppleScript**
    
- **Finder Automation**
    
- Manual troubleshooting + persistence 🧠
    

---

> Next: Add README logging to each folder!