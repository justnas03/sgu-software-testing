# Quadratic Equation Solver

This repository contains a Python script that solves quadratic equations of the form ax² + bx + c = 0.

## Features

- Handles all cases of quadratic equations:
  - When a ≠ 0 (standard quadratic equation)
  - When a = 0 (linear equation)
  - Special cases (no solution, infinite solutions)
- Provides solutions with 4 decimal places of precision
- Accepts input coefficients from the user

## Usage

1. Run the `ptb2.py` script:
   ```
   python ptb2.py
   ```

2. Enter the coefficients a, b, and c when prompted, separated by spaces:
   ```
   1 -5 6
   ```

3. The program will output the solution(s) to the equation.

## Input Format

The input should be three numbers (a, b, and c) separated by spaces. For example:
- `-1 6 8` represents the equation -x² + 6x + 8 = 0
- `0 0 0` represents the equation 0 = 0

## Output

The program will print one of the following:
- "Phương trình vô số nghiệm" (Infinite solutions)
- "Phương trình vô nghiệm" (No solution)
- "Phương trình có nghiệm x = [value]" (One solution)
- "Phương trình có nghiệm kép x = [value]" (Double root)
- "Phương trình có 2 nghiệm phân biệt x1 = [value1] và x2 = [value2]" (Two distinct solutions)

## Test Cases

The repository includes several test input files (e.g., `ptb2_test.in1`, `ptb2_test.in4`) that can be used to verify the program's functionality.

## Note

This program is written in Vietnamese. Future updates may include internationalization support.
