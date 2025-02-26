from pypdf import PdfReader, PdfWriter, PdfMerger
import os

def validate_files(files):

    valid_files = []

    for file in files:
        print(f"Sprawdzam plik: {file}") #la
        if not os.path.isfile(file):
            print(f"File {file} does not exist")
        continue
    valid_files.append(file)

    if valid_files:
        print(f"Znaleziono poprawne pliki: {valid_files}")  
    else:
        print("Brak poprawnych plików do scalenia.")
    return valid_files

    
def merge_pdfs(files):
    valid_files = validate_files(files)
    if not valid_files:
        print("Brak poprawnych plików do scalenia.")  
        return

    merger = PdfWriter()
    print("Rozpoczynam scalanie plików...")  

    for file in valid_files:
        print(f"Dodaję plik do scalenia: {file}")  
        merger.append(file)
    
    output_folder = input("Enter path, where your file will be saved.")

    if not os.path.exists(output_folder):
        print(f"The {output_folder} directory doesn't exist")
        return

    output_filename = os.path.join(output_folder, "merged_output.pdf")
    print(f"Zapisuję plik do: {output_filename}")  
    merger.write(output_filename)
    print(f"File has been successfully saved in {output_folder}, as {output_filename}")

def main():
    files = input("Enter the paths to the PDF files you want toi merge, seperated by commas: ").split(",")
    files = [file.strip() for file in files]
    print(f"Pliki do scalania: {files}")  #

    merge_pdfs(files)

main()