### Step 1: Create the file

In VS Code, inside your Week17 folder:

* Click New File.

* Name it exactly test_cases.md.

* Copy and paste the content below.

# Test Cases – Simulated Device Monitoring and Alert System

## 1. Purpose
This document records the test cases used to verify the functionality of the Simulated Device Monitoring and Alert System.

## 2. Test Cases
Test Case 1: View Readings

- Input: 1
- Expected Result: Displays the five initial temperature readings.

Test Case 2: Add Valid Reading

- Input: 32
- Expected Result: Displays "Reading added successfully."

Test Case 3: Empty Input

- Input: Blank
- Expected Result: Displays an empty input error message.

Test Case 4: Invalid Input

- Input: abc
- Expected Result: Displays a whole-number validation error.

Test Case 5: Negative Reading

- Input: -5
- Expected Result: Rejects the input as invalid.

Test Case 6: Out-of-Range Reading

- Input: 101
- Expected Result: Displays a range validation error.

Test Case 7: Normal Classification

- Input: 28
- Expected Result: Classifies the temperature as NORMAL.

Test Case 8: Warning Classification

- Input: 31
- Expected Result: Classifies the temperature as WARNING.

Test Case 9: Critical Classification

- Input: 37
- Expected Result: Classifies the temperature as CRITICAL.

Test Case 10: Generate Summary

- Input: 4
- Expected Result: Displays the total, average, minimum, maximum, and classification percentages.

Test Case 11: Invalid Menu Choice

- Input: 9
- Expected Result: Displays an invalid menu choice message.

Test Case 12: Exit Program

- Input: 5
- Expected Result: Displays a thank-you message and exits the program.


## 3. Testing Notes
- Run each test case using the Python program.
- Record the observed output in the Actual Result column.
- Change the Status column to *Pass* if the actual result matches the expected result.
- Change the Status column to *Fail* if the actual result does not match the expected result.
- Do not mark a test as Pass until it has actually been performed.

## 4. Conclusion
The test cases are designed to check the program's menu, reading management, classification rules, input validation, summary calculations, and exit function. The results will be completed after the program has been implemented and tested.

### Step 2: Save the file

Press Ctrl + S.
