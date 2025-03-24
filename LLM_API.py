class LLMApi:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": {"IMAGE"}}}

    RETURN_NAMES = "text"
    RETURN_TYPES = "STRING"

    def run(self):
        return "test"
