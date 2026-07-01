"""
=========================================================
Real Estate Business Intelligence Platform
Author : Shreya Jayani

Main entry point for synthetic data generation.
=========================================================
"""

from generators.generate_dimensions import generate_dimensions
from generators.generate_facts import generate_facts


def main():
    print("=" * 60)
    print("Real Estate BI Platform")
    print("=" * 60)

    print("\nGenerating Dimension Tables...")
    generate_dimensions()

    print("\nGenerating Fact Tables...")
    generate_facts()

    print("\nData generation completed successfully!")


if __name__ == "__main__":
    main()
