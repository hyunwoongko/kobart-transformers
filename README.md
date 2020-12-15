## KoBart-Transformers
- SKT에서 공개한 KoBart를 편하게 사용할 수 있게 transformers로 포팅하였습니다.
<br><br>

### Install
- pip를 이용해 설치할 수 있습니다.
```consol
pip install kobart-transformers
```
<br>

### Tokenizer
- `PretrainedTokenizerFast`를 이용하여 구현되었습니다.
- `PretrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")`와 동일합니다.
```python
>>> from kobart_transformers import get_kobart_tokenizer
>>> kobart_tokenizer = get_kobart_tokenizer()
>>> kobart_tokenizer.tokenize("안녕하세요. 한국어 BART 입니다.🤣:)l^o")
['▁안녕하', '세요.', '▁한국어', '▁B', 'A', 'R', 'T', '▁입', '니다.', '🤣', ':)', 'l^o']
```
<br>

### Model
- `BartModel`을 이용하여 구현되었습니다.
- `BartModel.from_pretrained("hyunwoongko/kobart")와 동일합니다.`
```python
>>> from kobart import get_kobart_model, get_kobart_tokenizer
>>> kobart_tokenizer = get_kobart_tokenizer()
>>> model = get_kobart_model()
>>> inputs = kobart_tokenizer(['안녕하세요.'], return_tensors='pt')
>>> model(inputs['input_ids'])
Seq2SeqModelOutput(last_hidden_state=tensor([[[-0.4488, -4.3651,  3.2349,  ...,  5.8916,  4.0497,  3.5468],
         [-0.4096, -4.6106,  2.7189,  ...,  6.1745,  2.9832,  3.0930]]],
       grad_fn=<TransposeBackward0>), past_key_values=None, decoder_hidden_states=None, decoder_attentions=None, cross_attentions=None, encoder_last_hidden_state=tensor([[[ 0.4624, -0.2475,  0.0902,  ...,  0.1127,  0.6529,  0.2203],
         [ 0.4538, -0.2948,  0.2556,  ..., -0.0442,  0.6858,  0.4372]]],
       grad_fn=<TransposeBackward0>), encoder_hidden_states=None, encoder_attentions=None)
```
<br>

### Reference
- [SKT KoBart](https://github.com/SKT-AI/KoBART)
- [Huggingface Transformers](https://github.com/huggingface/transformers)
