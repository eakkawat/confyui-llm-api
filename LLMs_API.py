class LLMsApi:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": {"IMAGE"}}}

    RETURN_NAMES = "text"
    RETURN_TYPES = "STRING"

    FUNCTION = "run"

    CATEGORY = "LLMs/api"

    def run(self):
        return "test"


NODE_CLASS_MAPPINGS = {"X_LLMsAPI": LLMsApi}
