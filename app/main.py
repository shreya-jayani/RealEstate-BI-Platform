from app.generators.generate_date import generate_date
from app.generators.generate_location import generate_location
from app.generators.generate_building_type import generate_building_type


def main():

    print("=" * 60)
    print("Property Benchmark Intelligence Platform")
    print("=" * 60)

    print("\nGenerating Dimensions...\n")

    generate_date()
    generate_location()
    generate_building_type()

    print("\nSprint 1 - Milestone 3 completed successfully!")


if __name__ == "__main__":
    main()