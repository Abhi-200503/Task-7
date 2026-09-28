# Task 7 - Natural-Language Telemetry Query Test Results

## Test Objective

The objective of this testing activity is to verify whether the natural-language grid assistant can understand different telemetry-related queries and provide appropriate responses.

## Test Environment

* Application: Natural-Language Grid Assistant
* Framework: Streamlit
* Programming Language: Python
* Data Processing: Pandas
* Dataset: grid_data.csv

---

## Test Case 1 - Predicted Peak Consumption

### Query

What is the predicted peak consumption?

### Expected Result

The system should return the predicted peak consumption value.

### Actual Result

Predicted peak consumption is 699.31 MW.

### Status

**PASS**

---

## Test Case 2 - Predicted Average Consumption

### Query

What is the predicted average consumption?

### Expected Result

The system should return the predicted average consumption value.

### Actual Result

Predicted average consumption is 587.13 MW.

### Status

**PASS**

---

## Test Case 3 - Peak Power Consumption

### Query

What is the peak power consumption?

### Expected Result

The system should return the peak power consumption value.

### Actual Result

Peak power consumption is 818.59 MW.

### Status

**PASS**

---

## Test Summary

| Test Case | Query                         | Result    | Status |
| --------- | ----------------------------- | --------- | ------ |
| TC01      | Predicted peak consumption    | 699.31 MW | PASS   |
| TC02      | Predicted average consumption | 587.13 MW | PASS   |
| TC03      | Peak power consumption        | 818.59 MW | PASS   |

---

## Overall Result

All three tested natural-language telemetry queries were successfully processed by the system.

The assistant correctly returned meaningful results for:

* Predicted peak consumption
* Predicted average consumption
* Peak power consumption

## Conclusion

The testing confirms that the natural-language telemetry query interface can process different user questions and provide understandable power-consumption results.

The system successfully passed all the defined test cases.
