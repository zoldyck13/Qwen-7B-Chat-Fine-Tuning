# Fine-tuning Qwen-7B-Chat with LoRA and 4-bit Quantization
This  [jupyter notebook](Qwen-7B-Chat_Clean.ipynb) demostrates how to fine-tune the Qwen-7B-Chat model using Hugging Face Transformers with LoRA(Low-Rank Adaptation) for efficient traning, combined with 4 bit Quantization to reduce memory usage.
---

## Features

- Load Qwen-7B-Chat model with 4-bit quantization (`bitsandbytes`)
- Apply LoRA for parameter-efficient fine-tuning (`peft` library)
- Custom data preprocessing for multi-turn chat conversations
- Training using Hugging Face's Trainer with gradient accumulation and mixed precision (fp16)

---

## Installation

Make sure to install the necessary dependencies:

```bash
pip install transformers datasets peft bitsandbytes accelerate torch
```


## Usage
1. Prepare your dataset in JOSNL format with mulit-turn messages. Example format:
```bash
   {
    "messages": [
      {"role": "user", "content": "Hello!"},
      {"role": "assistant", "content": "Hi, how can I help you?"}
    ]
  }
```
2. Run the training script to fine-tune the model.
3. After training completes, load the model with the fine-tuned weights from the output directory (e.g, ./qwen-lora-finetuned) to evaluate the improved preformance.

___
## Troublshooting
If you face issues loading the model with 4-bit quantization:
- Ensure bitsandbytes is installed:
  ```bash
    pip install bitsandbytes
  ```
- Check your GPU compatibility and CUDA installation.
- Update transformers to the latest version.
- Try changing the device map to "auto" in the model loading code.
- If problems persist, consider switching to 8-bit quantization by replacing load_in_4bit=True with load_in_8bit=True.


---

## Notes
- accelerate is installed because it helps manage device placement and training optimizations automatically, especially when using Trainer.
- Using LoRA allows training only a small subset of model parameters, making fine-tuning feasible on limited hardware.
- 4-bit quantization drastically reduces memory usage but requires compatible hardware and software setup.


  ---
  ### Author
  [Ali Saad]
