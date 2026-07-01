from app.generators.generate_date import generate_date


def main():
    print("=" * 60)
    print("Property Benchmark Intelligence Platform")
    print("=" * 60)

    print("\nGenerating Date Dimension...")
    generate_date()

    print("\nSprint 1 completed successfully!")


if __name__ == "__main__":
    main()