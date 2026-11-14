import os

def create_file(file_name):
    try:
        with open(file_name,"x") as f:
            print(f"file name {file_name}: created successfully!!")

    except FileExistsError:
        print(f"file name {file_name} already exists!!")

    except Exception as e:
        print("An error occurred : ")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("file in direct!")
        for file in files:
            print(files)
        

def delete_file(file_name):
    try:
       os.remove(file_name)
       print(f"{file_name} has been delete successfully!!")

    except FileExistsError:
        print("file not found")

    except Exception as e:
        print("An error occurred : ")

def read_file(file_name):
    try:
        with open("practice.txt","r") as f:
            contact = f.read()
            print(contact)

    except FileExistsError:
        print(f"{file_name} doesn't exist!!!")

    except Exception as e:
        print("An error occurred : ")

def update_file(file_name):
    try:
       with open("practice.txt","a") as f:
        contact = input("Enter data to add in file = ")
        f.write(contact + "\n") 
        print("Content added to {file_name} successfully!!!")
        
    except FileExistsError:
        print(f"{file_name} doesn't exist!!!")

    except Exception as e:
        print("An error occurred : ")

def main():
    while True:
        print("File Management aap!!")
        print("1: Create file")
        print("2: View file")
        print("3: delete file")
        print("4: read file")
        print("5: update file")
        print("6: Exit ")

        choice = input("Enter your choice(1-6) = ")

        if choice == '1':
            file_name = input("Enter the filename to create = ")
            create_file(file_name)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            file_name = input("Enter the filename to delete = ")
            delete_file(file_name)

        elif choice == '4':
            file_name = input("Enter the filename to read = ")
            read_file(file_name)

        elif choice == '5':
            file_name = input("Enter the filename to update = ")
            update_file(file_name)

        elif choice == '6':
            print("Closing the app.....")
            break
        
        else:
            print("Invslid syntax ")

if __name__ == "__main__":
    main()