import pyAesCrypt
import os

def decrypt(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[+]Encrypted")

    os.remove(file)


def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decrypt(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


pasword = input("Enter password: ")
walking_by_dirs("C:\\Users\\koty1\\OneDrive\\Рабочий стол\\etest", pasword)