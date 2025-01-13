def extract_calibration_value(line):
    """Extract first and last digit from a line and combine them into a two-digit number."""
    # Find all digits in the line
    digits = [char for char in line if char.isdigit()]
    
    if not digits:
        return 0
        
    # Combine first and last digit
    return int(digits[0] + digits[-1])

def calculate_total_calibration(input_text):
    """Calculate sum of calibration values for all lines."""
    # Split input into lines
    lines = input_text.strip().split('\n')
    
    # Calculate sum of calibration values
    total = sum(extract_calibration_value(line) for line in lines)
    
    return total

# Example
example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet8"""

print(f"Example sum: {calculate_total_calibration(example_input)}")  # Should output 142