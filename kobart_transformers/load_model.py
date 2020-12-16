from transformers import BartModel, PreTrainedTokenizerFast, BartForConditionalGeneration


def get_kobart_model():
    return BartModel.from_pretrained("hyunwoongko/kobart")


def get_kobart_for_conditional_generation():
    return BartForConditionalGeneration.from_pretrained("hyunwoongko/kobart")


def get_kobart_tokenizer():
    tokenizer = PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")

    tokenizer.pad_token = "<pad>"
    tokenizer.bos_token = "<s>"
    tokenizer.eos_token = "</s>"
    tokenizer.unk_token = "<unk>"
    tokenizer.mask_token = "<mask>"

    return tokenizer
