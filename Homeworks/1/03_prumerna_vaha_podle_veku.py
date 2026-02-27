# 03_prumerna_vaha_podle_veku.py reseni
# autor reseni: Jan Hruza
# datum: 2026-02-20

def calculate_average_weight_in_age_range(file_path: str, min_age: int, max_age: int) -> float | None:
    """
    Calculates the average weight of people in a specified age range from a CSV file.

    Args:
        file_path: Path to the CSV file.
        min_age: Minimum age (inclusive).
        max_age: Maximum age (inclusive).

    Returns:
        Average weight as float, or None if calculation cannot be performed.
    """
    total_weight = 0.0
    person_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        try:
                            age = int(parts[4])
                            if min_age <= age <= max_age:
                                total_weight += float(parts[2])
                                person_count += 1
                        except ValueError:
                            continue

    except FileNotFoundError:
        return None

    # Prevent division by zero and return result
    if person_count > 0:
        return total_weight / person_count
    else:
        return None


def main():
    # Example 1: Calculate average weight for age 20-30 years
    avg_weight_20_30 = calculate_average_weight_in_age_range("data.csv", 20, 30)
    if avg_weight_20_30 is not None:
        print(f"Average weight of people aged 20-30 years is: {avg_weight_20_30:.2f} kg")
    else:
        print("No people found in the age range 20-30 years.")

    # Example 2: Age range where no one exists
    avg_weight_40_50 = calculate_average_weight_in_age_range("data.csv", 40, 50)
    if avg_weight_40_50 is not None:
        print(f"Average weight of people aged 40-50 years is: {avg_weight_40_50:.2f} kg")
    else:
        print("No people found in the age range 40-50 years.")

    # Example 3: Non-existent file
    result_nonexistent = calculate_average_weight_in_age_range("nonexistent.csv", 20, 30)
    if result_nonexistent is None:
        print("File 'nonexistent.csv' was not found.")


if __name__ == '__main__':
    main()