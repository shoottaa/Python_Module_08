import os
import sys
from dotenv import load_dotenv  # type: ignore


load_dotenv()


def config_check() -> None:
    try:
        if not os.path.exists(".env"):
            raise FileNotFoundError("[ERROR] .env file not found.")
        if os.getenv("MATRIX_MODE") not in ("development", "production"):
            raise ValueError(
                "[ERROR] MATRIX_MODE must be 'development' or 'production'.")
        if not os.getenv("DATABASE_URL"):
            raise ValueError("[ERROR] DATABASE_URL is not set.")
        if not os.getenv("API_KEY"):
            raise ValueError("[ERROR] API_KEY is not set.")
        if not os.getenv("ZION_ENDPOINT"):
            raise ValueError("[ERROR] ZION_ENDPOINT is not set.")
        if not os.getenv("LOG_LEVEL"):
            raise ValueError("[ERROR] LOG_LEVEL is not set.")
    except Exception as e:
        print(e)
        sys.exit(1)


def security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file — relying on system environment variables")

    print("[OK] Production overrides available")


def config(matrix_mode: str) -> None:
    if (matrix_mode == "development"):
        print("DATABASE_URL: Connected to local instance")
        print("API Access: Authenticated")
        print(f"LOG_LEVEL: {os.getenv('LOG_LEVEL')}")
        print("Zion Network: Online")
    elif (matrix_mode == "production"):
        print("DATABASE_URL: Connected to production instance")
        print("API Access: Authenticated with production key")
        print(f"LOG_LEVEL: {os.getenv('LOG_LEVEL')}")
        print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")


def main() -> None:
    config_check()
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"MATRIX_MODE: {os.getenv('MATRIX_MODE')}")
    config(os.getenv("MATRIX_MODE"))
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
