from typing import Union, List

class Request:

    def __init__(self,
        prompt:Union[str, List[str]], 
        max_new_tokens:int=1,
        get_answers:bool=False,
        top_k:int=1,
        generate_greedy:bool=True,
        layers:Union[str, List[str]]=None) -> None:

        if isinstance(prompt, str): prompt = [prompt]

        self.prompt = prompt
        self.max_new_tokens = max_new_tokens
        self.get_answers = get_answers
        self.top_k = top_k
        self.generate_greedy = generate_greedy
        self.layers = layers or []

    def _to_json(self):

        return {
            "prompt": self.prompt,
            "max_new_tokens": self.max_new_tokens,
            "get_answers": self.get_answers,
            "top_k": self.top_k,
            "generate_greedy": self.generate_greedy,
            "activation_requests": {
                "final_output": True,
                "layers": self.layers,
                "intervention": None
            }
        }