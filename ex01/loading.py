"""
Exercise 01 - Loading Programs
"""

import sys
import importlib.metadata
from typing import Optional


def get_version(package: str) -> Optional[str]:
    """Return installed version of a package or None."""
    try:
        return importlib.metadata.version(package)
    except Exception:
        return None


def check_dependencies() -> bool:
    """Check required packages and print their status."""
    packages = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    all_ok = True

    print("Checking dependencies:")
    for pkg, description in packages.items():
        version = get_version(pkg)
        if version:
            print(f"[OK] {pkg} ({version}) - {description}")
        else:
            print(f"[MISSING] {pkg} - not installed")
            print("  Install with: pip install -r requirements.txt")
            print("  Or with:      poetry install")
            all_ok = False

    return all_ok


def analyze_data():
    """Generate 1000 Matrix data points."""
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore

    rng = np.random.default_rng(42)
    data = {
        "agent_id": [f"A{i:04d}" for i in range(1000)],
        "threat_level": rng.integers(1, 100, 1000),
        "system_load": rng.uniform(0, 1, 1000),
    }
    return pd.DataFrame(data)


def create_chart(df) -> None:
    """Save a simple visualization."""
    import matplotlib  # type: ignore
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    plt.figure()
    plt.hist(df["threat_level"], bins=20, color="green")
    plt.title("Matrix Threat Levels")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    """Main program."""
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    df = analyze_data()
    print(f"Processing {len(df)} data points...")

    print("Generating visualization...")
    try:
        create_chart(df)
    except Exception as e:
        print(f"[WARNING] Could not generate chart: {e}")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
