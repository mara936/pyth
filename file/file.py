try:
    input_filename = input("Enter filename to be read: ")

    with open(input_filename, "r") as infile:
        content = infile.read()
        modified_content = content.upper()

        output_filename = input ("Enter the new file to be saved: ")
    
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

        print(F"File saved as '{output_filename}' with uppercase content")

except FileNotFoundError:
    print("Error: File Not Found")
except Exception as e:
    print(f" Error{e}")