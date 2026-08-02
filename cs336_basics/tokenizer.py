class Tokenizer:
    def __init__(self,
    vocab: dict[int, bytes],
    merges: list[tuple[bytes, bytes]],
    special_tokens = None):
        pass

    # construct from files
    def from_files(cls,
    vocab_filepath,
    merges_filepath,
    special_tokens=None):
        pass

    # encode input text into token ids
    def encode(self, text:str) -> list[int]:
        pass
    
    # given list of strings, return generator that lazily yeild token-ids
    def encode_iterable(self,
    iterable: Iterable[str]) -> Iterator[int]:
        pass

    # decode token IDs into text
    def decode(self,
    ids: list[int]) -> str:
        pass