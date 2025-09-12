class FileOperation:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def open_file_read_mode(self):
        try:
            self.file = open(self.filename, 'r')
            print(f"File {self.filename} opened in read mode.")
        except FileNotFoundError:
            print(f"File {self.filename} not found.")

    def open_file_write_mode(self):
        try:
            self.file = open(self.filename, 'w')
            print(f"File {self.filename} opened in write mode.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def current_position(self):
        if self.file:
            print(f"Current position of the file pointer: {self.file.tell()}")
        else:
            print("File is not opened.")

    def reposition_pointer(self):
        if self.file:
            self.file.seek(0)
            print(f"File pointer repositioned at the beginning.")
        else:
            print("File is not opened.")

    def exit(self):
        if self.file:
            self.file.close()
            print(f"File {self.filename} closed.")
        print("Exiting the program.")
        return "exit"

def main():
    filename = input("Enter the filename: ")
    file_operation = FileOperation(filename)

    while True:
        print("\nFile Operations Menu:")
        print("1. Open file in read mode")
        print("2. Open file in write mode")
        print("3. Current position of the file pointer")
        print("4. Reposition the pointer at the beginning")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_operation.open_file_read_mode()
        elif choice == "2":
            file_operation.open_file_write_mode()
        elif choice == "3":
            file_operation.current_position()
        elif choice == "4":
            file_operation.reposition_pointer()
        elif choice == "5":
            if file_operation.exit() == "exit":
                break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()