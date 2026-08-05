import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "CohereLabs/tiny-aya-global"

print("Loading Tiny Aya...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    dtype=torch.float32,
)

print("Tiny Aya loaded.")

def generate(prompt):

    messages = [
        {"role": "user", "content": prompt}
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        return_tensors="pt",
        return_dict=True,
        add_generation_prompt=True,
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
    )

    new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    return tokenizer.decode(
        new_tokens,
        skip_special_tokens=True,
    )