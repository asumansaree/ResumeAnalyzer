from transformers import AutoModelForTokenClassification, AutoTokenizer, Trainer, TrainingArguments
import torch

idx2tag = {0: 'B-NAME',
 1: 'I-DEG',
 2: 'L-EDUCATION',
 3: 'L-DESC',
 4: 'X',
 5: 'L-LOC',
 6: 'L-GRADYEAR',
 7: 'B-DESIG',
 8: 'U-LOC',
 9: 'U-GRADYEAR',
 10: 'U-EMAIL',
 11: 'L-DEG',
 12: 'I-COMPANY',
 13: '[SEP]',
 14: 'U-LINK',
 15: 'B-DEG',
 16: 'I-LOC',
 17: 'U-COMPANY',
 18: 'B-CLG',
 19: 'B-GRADYEAR',
 20: 'L-CLG',
 21: 'I-YOE',
 22: 'U-SKILLS',
 23: 'I-DESIG',
 24: 'B-COMPANY',
 25: 'U-DESIG',
 26: 'I-EDUCATION',
 27: 'I-NAME',
 28: 'B-EDUCATION',
 29: 'L-DESIG',
 30: 'L-SKILLS',
 31: 'I-GRADYEAR',
 32: 'B-LOC',
 33: 'O',
 34: 'I-DESC',
 35: 'L-COMPANY',
 36: 'U-DEG',
 37: 'I-SKILLS',
 38: 'B-SKILLS',
 39: 'B-YOE',
 40: 'I-CLG',
 41: 'L-YOE',
 42: 'B-DESC',
 43: '[CLS]',
 44: 'L-NAME'}

# Load fine-tuned model
model_path = 'custom_model'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForTokenClassification.from_pretrained(model_path)

# Example unseen text
file_path = "TextExtraction/collectedCVs/test/AsumanSareERGUT.txt"
with open(file_path, "r", encoding="utf-8") as file:
    unseen_text = file.read()

# Tokenize the text using encode_plus
encoding = tokenizer.encode_plus(
    unseen_text,
    add_special_tokens=True,
    return_tensors='pt',  # Returns PyTorch tensors
    max_length=512,  # Set max length to 512
    truncation=True,  # Truncate if longer than max_length
)

# Obtain model predictions
with torch.no_grad():
    outputs = model(**encoding)

# Get predicted labels
predictions = torch.argmax(outputs.logits, dim=2).numpy()[0]

# Mapping from label indices to NER tags is in idx2tag
# Map predicted labels to NER tags
predicted_tags = [idx2tag[label] for label in predictions]

# Tokenize the text for printing
tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'][0])

# Print the tokenized text and predicted tags
current_sentence_tokens = []
current_sentence_tags = []

# Iterate through tokens and predicted tags
for token, tag in zip(tokens, predicted_tags):
    # Check for special tokens
    if token == '[CLS]' or token == '[SEP]':
        if current_sentence_tokens:
            print(" ".join(current_sentence_tokens))
            print(" ".join(current_sentence_tags))
            print()
            current_sentence_tokens = []
            current_sentence_tags = []
    else:
        current_sentence_tokens.append(token)
        current_sentence_tags.append(tag)

# Print the last sentence if any
if current_sentence_tokens:
    print(" ".join(current_sentence_tokens))
    print(" ".join(current_sentence_tags))
