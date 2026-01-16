print("Starting script")

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("Imports done")

model_id = "Qwen/Qwen2.5-1.5B-Instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    device_map="cpu",
    low_cpu_mem_usage=True
)

print("Model loaded")

prompt = "Explain transformers in simple terms."
inputs = tokenizer(prompt, return_tensors="pt")

print("Running generation...")
with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=False
    )

print("Generation done")
print(tokenizer.decode(output[0], skip_special_tokens=True))
