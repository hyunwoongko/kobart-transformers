## KoBART-Transformers
- SKT에서 공개한 KoBART를 편리하게 사용할 수 있게 transformers로 포팅하였습니다.
<br><br>

### Install (Optional)
- `BartModel`과 `PreTrainedTokenizerFast`를 이용하면 설치하실 필요 없습니다.
```console
pip install kobart-transformers
```
<br>

### Tokenizer
- `PreTrainedTokenizerFast`를 이용하여 구현되었습니다.
- `PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")`와 동일합니다.
```python
>>> from kobart_transformers import get_kobart_tokenizer
>>> # from transformers import PreTrainedTokenizerFast

>>> kobart_tokenizer = get_kobart_tokenizer()
>>> # kobart_tokenizer = PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")

>>> kobart_tokenizer.tokenize("안녕하세요. 한국어 BART 입니다.🤣:)l^o")
['▁안녕하', '세요.', '▁한국어', '▁B', 'A', 'R', 'T', '▁입', '니다.', '🤣', ':)', 'l^o']
```
<br>

### Model
- `BartModel`을 이용하여 구현되었습니다.
- `BartModel.from_pretrained("hyunwoongko/kobart")`와 동일합니다.
```python
>>> from kobart_transformers import get_kobart_model, get_kobart_tokenizer
>>> # from transformers import BartModel

>>> kobart_tokenizer = get_kobart_tokenizer()
>>> model = get_kobart_model()
>>> # model = BartModel.from_pretrained("hyunwoongko/kobart")

>>> inputs = kobart_tokenizer(['안녕하세요.'], return_tensors='pt')
>>> model(inputs['input_ids'])
Seq2SeqModelOutput(last_hidden_state=tensor([[[-0.4488, -4.3651,  3.2349,  ...,  5.8916,  4.0497,  3.5468],
         [-0.4096, -4.6106,  2.7189,  ...,  6.1745,  2.9832,  3.0930]]],
       grad_fn=<TransposeBackward0>), past_key_values=None, decoder_hidden_states=None, decoder_attentions=None, cross_attentions=None, encoder_last_hidden_state=tensor([[[ 0.4624, -0.2475,  0.0902,  ...,  0.1127,  0.6529,  0.2203],
         [ 0.4538, -0.2948,  0.2556,  ..., -0.0442,  0.6858,  0.4372]]],
       grad_fn=<TransposeBackward0>), encoder_hidden_states=None, encoder_attentions=None)
```
<br>

### For Seq2Seq Training
- seq2seq 학습시에는 아래와 같이 `get_kobart_for_conditional_generation()`을 이용합니다.
- `BartForConditionalGeneration.from_pretrained("hyunwoongko/kobart")`와 동일합니다.
```python
>>> from kobart_transformers import get_kobart_for_conditional_generation
>>> # from transformers import BartForConditionalGeneration

>>> model = get_kobart_for_conditional_generation()
>>> # model = BartForConditionalGeneration.from_pretrained("hyunwoongko/kobart")
```
<br>

### Updates Notes
#### version 0.1
- `pad` 토큰이 설정되지 않은 에러를 해결하였습니다.
```python
from kobart import get_kobart_tokenizer
kobart_tokenizer = get_kobart_tokenizer()
kobart_tokenizer(["한국어", "BART 모델을", "소개합니다."], truncation=True, padding=True)
{
'input_ids': [[28324, 3, 3, 3, 3], [15085, 264, 281, 283, 24224], [15630, 20357, 3, 3, 3]], 
'token_type_ids': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 
'attention_mask': [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 0, 0, 0]]
}
```
#### version 0.1.3
- `get_kobart_for_conditional_generation()`를 `__init__.py`에 등록하였습니다.

#### version 0.1.4
- 누락되었던 `special_tokens_map.json`을 추가하였습니다.
- 이제 `pip install` 없이 KoBART를 이용할 수 있습니다.
<br>

### Reference
- [SKT KoBART](https://github.com/SKT-AI/KoBART)
- [Huggingface Transformers](https://github.com/huggingface/transformers)
