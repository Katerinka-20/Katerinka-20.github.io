def main():
    file_name = input("File name: ")
    if file_name.lower().endswith(".gif"):
        print("image/gif")
    elif file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.lower().endswith(".png"):
        print("image/png")
    elif file_name.lower().endswith(".pdf"):
        print("application/pdf")
    elif file_name.lower().endswith(".txt"):
        print("text/plain")
    elif file_name.lower().endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
