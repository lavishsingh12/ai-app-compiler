from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema
from pipeline.runtime_simulator import simulate_execution

import json


user_prompt = """
Build a CRM with login,
contacts,
dashboard,
payments
"""


# Stage 1 - Intent Extraction
intent = extract_intent(user_prompt)

print("\n" + "=" * 50)
print("STAGE 1 : INTENT EXTRACTION")
print("=" * 50)

print(json.dumps(intent, indent=4))


# Stage 2 - System Design
design = design_system(intent)

print("\n" + "=" * 50)
print("STAGE 2 : SYSTEM DESIGN")
print("=" * 50)

print(json.dumps(design, indent=4))


# Stage 3 - Schema Generation
schema = generate_schema(design)

print("\n" + "=" * 50)
print("STAGE 3 : SCHEMA GENERATION")
print("=" * 50)

print(json.dumps(schema, indent=4))


# Uncomment this to test Repair Engine

# schema["api_schema"]["endpoints"].remove("/contacts")


# Stage 4 - Validation
errors = validate_schema(schema)

print("\n" + "=" * 50)
print("STAGE 4 : VALIDATION")
print("=" * 50)

if len(errors) == 0:
    print("No validation errors found.")
else:
    print(errors)


# Stage 5 - Repair
repaired_schema, repairs = repair_schema(
    schema,
    errors
)

print("\n" + "=" * 50)
print("STAGE 5 : REPAIR ENGINE")
print("=" * 50)

if len(repairs) == 0:
    print("No repairs needed.")
else:
    print(repairs)

#runtime simulation
runtime_result = simulate_execution(
    repaired_schema
)

print("\n" + "=" * 50)
print("STAGE 6 : RUNTIME SIMULATION")
print("=" * 50)

print(
    json.dumps(
        runtime_result,
        indent=4
    )
)

# Final Output

print("\n" + "=" * 50)
print("FINAL OUTPUT")
print("=" * 50)

print(
    json.dumps(
        repaired_schema,
        indent=4
    )
)
