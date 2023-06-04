
import openai
from database_manager import DatabaseManager

# to change the settings of generator class, 
# generator = Generator("gpt-3.5-turbo", "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")

class Generator:
    def __init__(self, engine="gpt-3.5-turbo", api_key="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"):
        self.engine = engine
        self.api_key = api_key
        openai.api_key = api_key
        self.conversation_log = []
        self.db_manager = DatabaseManager()
    
    def base_generation(self, prompt, memory=False, token=300, temperature=0.5):
        self.conversation_log.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=self.conversation_log,
            max_tokens=token,
            temperature=temperature,
        )
        response_content = response.choices[0].message.content.strip()
        if memory:
            self.conversation_log.append({"role": "system", "content": response_content})
        else:
            self.conversation_log.pop()
        return response_content

    def multi_generation(self, prompt, number=1, memory=False):
        responses = [self.base_generation(prompt, memory) for _ in range(number)]
        return responses
