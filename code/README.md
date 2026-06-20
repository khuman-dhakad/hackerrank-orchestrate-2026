# Multi-Modal Damage Claim Verification System

A damage-claim verification system developed for the HackerRank Orchestrate Hackathon.

The system evaluates insurance-style claims using:

* Claim conversations
* Submitted images
* User claim history
* Evidence requirements

It determines whether visual evidence supports, contradicts, or does not provide enough information for a reported claim.

---

## Features

### Claim Understanding

* Extracts claimed damage from conversation history
* Supports:

  * Cars
  * Laptops
  * Packages

### Image Analysis

* Uses Gemini 2.5 Flash for visual inspection
* Detects visible damage categories
* Identifies affected object parts
* Estimates severity

### Risk Assessment

* Reads user history
* Flags suspicious claim patterns
* Supports manual review workflows

### Decision Engine

Produces:

* Evidence sufficiency decision
* Claim status
* Risk flags
* Severity assessment
* Justification

### Fallback Mode

If Gemini is unavailable or quota limits are reached:

* Pipeline continues execution
* Generates valid output.csv
* Prevents runtime failure

---

## Project Structure

```text
.
├── code/
│   ├── main.py
│   ├── image_analyzer.py
│   ├── claim_parser.py
│   ├── decision_engine.py
│   ├── history_checker.py
│   ├── csv_processor.py
│   └── evaluation/
│       ├── main.py
│       └── evaluation_report.md
│
├── dataset/
│   ├── claims.csv
│   ├── sample_claims.csv
│   ├── user_history.csv
│   ├── evidence_requirements.csv
│   └── images/
│
└── output.csv
```

---

## Workflow

```text
Claims CSV
      ↓
Claim Parsing
      ↓
Image Analysis (Gemini)
      ↓
Risk Assessment
      ↓
Decision Engine
      ↓
Output CSV
```

---

## Output Fields

The generated output contains:

* user_id
* image_paths
* user_claim
* claim_object
* evidence_standard_met
* evidence_standard_met_reason
* risk_flags
* issue_type
* object_part
* claim_status
* claim_status_justification
* supporting_image_ids
* valid_image
* severity

---

## Technologies

* Python
* Pandas
* Pillow
* Gemini 2.5 Flash API
* Git & GitHub

---

## Evaluation

Evaluation artifacts are available under:

```text
code/evaluation/
```

The evaluation report includes:

* Operational analysis
* Runtime considerations
* Cost estimates
* Rate-limit considerations
* Model usage assumptions

---

## Author

Khuman Dhakad

MCA Student | Software Developer | AI & Automation Enthusiast

Built for HackerRank Orchestrate 2026 Hackathon.
