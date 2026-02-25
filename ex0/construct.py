import sys


if __name__ == "__main__":
    try:
        if sys.prefix != sys.base_prefix:
            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.version}")
            print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
            print(f"Environment Path: {sys.prefix}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting the gobal system.\n")
            print("Package installation path:")
            prefix = sys.prefix
            version_maj = sys.version_info.major
            version_min = sys.version_info.minor
            print(f"{prefix}/lib/python{version_maj}.{version_min}/site-packages")
        else:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.version}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows\n")
            print("Then run this program again.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
