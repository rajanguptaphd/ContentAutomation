import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from src.llm.base import BaseLLM

class HFBackend(BaseLLM):
    def __init__(self, model_name, device, max_new_tokens):
        self.device = device
        self.max_new_tokens = max_new_tokens

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.model.to(device)
        self.model.eval()

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        input_len = inputs["input_ids"].shape[-1]

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        gen_tokens = output[0][input_len:]
        return self.tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()
