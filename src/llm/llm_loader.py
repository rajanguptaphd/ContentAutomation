from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class OpenSourceLLM:
    def __init__(
        self,
        model_name: str,
        device: str,
        max_new_tokens: int = 256,
    ):
        self.model_name = model_name
        self.device = device
        self.max_new_tokens = max_new_tokens

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=torch.float16 if device != "cpu" else torch.float32,
        )

        self.model.to(device)
        self.model.eval()
    
    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                eos_token_id=self.tokenizer.eos_token_id,
        )

        return self.tokenizer.decode(output[0], skip_special_tokens=True)