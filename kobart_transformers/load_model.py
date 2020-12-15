from transformers import BartModel, PreTrainedTokenizerFast


def get_kobart_model():
    return BartModel.from_pretrained("hyunwoongko/kobart")


def get_kobart_tokenizer():
    return PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")
