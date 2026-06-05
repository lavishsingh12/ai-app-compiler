import gradio as gr
import json

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema
from pipeline.runtime_simulator import simulate_execution


def run_pipeline(user_prompt):

    intent = extract_intent(user_prompt)

    design = design_system(intent)

    schema = generate_schema(design)

    errors = validate_schema(schema)

    repaired_schema, repairs = repair_schema(
        schema,
        errors
    )

    runtime = simulate_execution(
        repaired_schema
    )

    result = {
        "intent": intent,
        "design": design,
        "schema": repaired_schema,
        "validation_errors": errors,
        "repairs": repairs,
        "runtime": runtime
    }

    return json.dumps(
        result,
        indent=4
    )


demo = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Textbox(
        lines=6,
        label="Describe your application"
    ),
    outputs=gr.Textbox(
        lines=30,
        label="Generated Output"
    ),
    title="AI App Compiler",
    description="Natural Language → Architecture → Schema → Validation → Runtime"
)

demo.launch()
