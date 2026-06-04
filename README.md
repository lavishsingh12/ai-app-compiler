## AI App Compiler

## Overview

AI App Compiler is a multi-stage AI system that converts natural language application requirements into structured application configurations.

The system follows a compiler-inspired architecture:

Natural Language → Intent Extraction → System Design → Schema Generation → Validation → Repair → Runtime Simulation

---

## Problem Statement

Users describe applications in natural language.

Example:

Build a CRM with login, contacts, dashboard, payments and role-based access.

The system converts this description into:

* UI Schema
* API Schema
* Database Schema
* Authentication Schema

while ensuring consistency and execution readiness.

---

## Architecture

User Prompt
↓
Intent Extractor
↓
System Designer
↓
Schema Generator
↓
Validator
↓
Repair Engine
↓
Runtime Simulator

---

## Pipeline Stages

### 1. Intent Extraction

Extracts:

* Application Type
* Features

Example:

```json
{
  "app_type": "CRM",
  "features": [
    "login",
    "contacts",
    "dashboard",
    "payments"
  ]
}
```

### 2. System Design

Generates:

* Entities
* Roles
* Modules

Example:

```json
{
  "entities": ["User", "Contact", "Payment"],
  "roles": ["User", "Admin"],
  "modules": [
    "Authentication",
    "ContactManagement",
    "Dashboard",
    "PaymentProcessing"
  ]
}
```

### 3. Schema Generation

Generates:

* UI Schema
* API Schema
* Database Schema
* Auth Schema

### 4. Validation

Performs:

* Missing component detection
* Cross-layer consistency checks

### 5. Repair Engine

Automatically repairs detected issues.

Example:

* Missing Contacts API
* Missing Payments API

### 6. Runtime Simulation

Validates execution readiness.

Outputs:

* Number of pages
* Number of APIs
* Number of tables
* Number of roles

---

## Technologies Used

* Python
* Google Gemini API
* Gradio
* JSON
* Rule-based Validation

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python ui.py
```

---

## Future Improvements

* Advanced semantic validation
* Conflict detection
* Rule-based optimization to reduce API calls
* Direct code generation
* Runtime deployment support

---

## Author

Lavish Singh Rajawat
