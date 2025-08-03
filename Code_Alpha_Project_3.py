"""
Python Automation Toolkit
- Move JPG files between folders
- Extract emails from text files
- Scrape webpage titles
"""

import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

def move_jpg_files():
    """Move all JPG files from source to destination folder"""
    print("\n" + "="*40)
    print("JPG FILE MOVER".center(40))
    print("="*40)
    
    while True:
        source = input("\nEnter source folder path: ").strip()
        if os.path.isdir(source):
            break
        print("Error: Folder doesn't exist. Try again.")
    
    dest = input("Enter destination folder path: ").strip()
    os.makedirs(dest, exist_ok=True)
    
    moved_files = []
    for filename in os.listdir(source):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(source, filename)
            dest_path = os.path.join(dest, filename)
            shutil.move(src_path, dest_path)
            moved_files.append(filename)
    
    print("\nResults:")
    print(f"- Found {len(moved_files)} JPG files")
    if moved_files:
        print("- Moved files:")
        for f in moved_files:
            print(f"  • {f}")
    print(f"\nAll files moved to: {dest}")

def extract_emails():
    """Extract all email addresses from a text file"""
    print("\n" + "="*40)
    print("EMAIL EXTRACTOR".center(40))
    print("="*40)
    
    while True:
        input_file = input("\nEnter path to text file: ").strip()
        if os.path.isfile(input_file):
            break
        print("Error: File doesn't exist. Try again.")
    
    output_file = input("Enter output file path: ").strip()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(emails))
    
    print("\nResults:")
    print(f"- Found {len(emails)} email addresses")
    print(f"- Saved to: {output_file}")
    if emails:
        print("\nSample emails:")
        for email in emails[:3]:  # Show first 3 as sample
            print(f"  • {email}")
        if len(emails) > 3:
            print(f"  • ...and {len(emails)-3} more")

def scrape_web_title():
    """Scrape and save title from a webpage"""
    print("\n" + "="*40)
    print("WEBPAGE TITLE SCRAPER".center(40))
    print("="*40)
    
    url = input("\nEnter URL (include http:// or https://): ").strip()
    output_file = input("Enter output file path: ").strip()
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(title)
        
        print("\nResults:")
        print(f"- Title: '{title}'")
        print(f"- Saved to: {output_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"\nError: Failed to fetch webpage - {e}")
    except Exception as e:
        print(f"\nError: {e}")

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*40)
        print("PYTHON AUTOMATION TOOLKIT".center(40))
        print("="*40)
        print("\n1. Move JPG Files")
        print("2. Extract Email Addresses")
        print("3. Scrape Webpage Title")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_web_title()
        elif choice == '4':
            print("\nThank you for using the Python Automation Toolkit!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")