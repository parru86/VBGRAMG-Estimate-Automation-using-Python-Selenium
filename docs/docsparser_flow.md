# VBGRAMG Parser Flow

## Project

VBGRAMG Estimate Automation

---

# Objective

Convert VBGRAMG Detailed Estimate PDF into Estimate Object.

```
PDF

↓

Estimate Object

↓

Selenium Automation

↓

VBGRAMG Portal
```

---

# Parser Pipeline

```
PDFReader

↓

TextNormalizer

↓

LineClassifier

↓

EstimateParser

↓

EstimateBuilder

↓

Estimate
```

---

# Parser State Machine

```
START

↓

HEADING

↓

SPECIFICATION

↓

MEASUREMENT_HEADER

↓

HEAD_DESCRIPTION

↓

MEASUREMENTS

↓

DEDUCTION

↓

LIST

↓

MATERIAL_ANALYSIS

↓

TOTAL

↓

NEXT_SPECIFICATION

↓

FINISHED
```

---

# State Description

## START

Read PDF.

Normalize all text.

Move to first Heading.

---

## HEADING

Example

```
Heading / Description:
Construction of Food grain storage building
```

Action

- Save Appendix Name

Next

SPECIFICATION

---

## SPECIFICATION

Example

```
79.03.07b -- Earth work in excavation...
```

Action

- Create Specification
- Reset Measurement Counter
- Reset Deduction Counter

Next

MEASUREMENT_HEADER

---

## MEASUREMENT_HEADER

Example

```
Sl No Description No L B D CF Quantity Remark
```

Ignore Header

Next

HEAD_DESCRIPTION

---

## HEAD_DESCRIPTION

Example

```
Earth Work

Brick Work

False Work
```

Optional

Save as

Specification.head_description

Next

MEASUREMENTS

---

## MEASUREMENTS

Example

```
1 COLUMN ...

2 LW ...

3 .
```

Action

RowBuffer

↓

RowParser

↓

MeasurementRow

Repeat until

```
deduction
```

or

```
LIST
```

---

## DEDUCTION

Optional

Example

```
deduction

10 COLUMN ...
```

Action

Parse exactly like Measurement

Store into

Specification.deductions

Repeat until

LIST

---

## LIST

Example

```
LIST
```

Ignore complete Material Analysis.

Next

MATERIAL_ANALYSIS

---

## MATERIAL_ANALYSIS

Ignore

Everything until

```
Total Quantity
```

---

## TOTAL

Ignore

```
Total Quantity

Total Deducted Quantity

Net Total Quantity

Say

Unskilled wage

Unskilled Person-days
```

Next

Next Heading

or

Next Specification

---

# Supported Features

✓ Multiple Headings

✓ Multiple Specifications

✓ Measurement

✓ Deduction

✓ Formula Length

✓ Dot Description

✓ Wrapped Description

✓ Negative Quantity

✓ Optional Head Description

---

# Unsupported

Structural Drawing

Image Pages

Scan PDFs

OCR PDFs

---

# Output

Estimate

```
Estimate

↓

Specification

↓

MeasurementRow

↓

DeductionRow
```

---

# Version

Parser Flow

Version 1.0