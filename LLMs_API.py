class LLMsApi:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": {"IMAGE"}}}

    RETURN_NAMES = "Text"
    RETURN_TYPES = "STRING"

    FUNCTION = "run"

    CATEGORY = "EakLLMs"

    def run(self):
        return "test"


NODE_CLASS_MAPPINGS = {"X_LLMsAPI": LLMsApi}

NODE_DISPLAY_NAME_MAPPINGS = {"X_LLMsAPI": "LLMs API"}
