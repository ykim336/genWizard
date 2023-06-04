from database_manager import DatabaseManager
from generator import Generator
from expander import Expander
from comparator import Comparator

class Combinations:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.expander = Expander()
        self.generator = Generator()
        self.comparator = Comparator()
        
    def chat_bot(self, filename=None):
        print("\nType '/exit' to end the conversation.")
        if filename != None:
            preprompt = self.db_manager.read(2, filename)
        while True:
            self.db_manager.write(1, input("\nUser: "))
            user_prompt = self.db_manager.read(1)
            self.db_manager.delete(1)
            if user_prompt == "/exit":
                break
            if filename != None:
                user_prompt = self.expander.base_expansion([preprompt, user_prompt])
            response = self.generator.base_generation(user_prompt, memory=True)
            print(f"Bot: {response}")
        self.generator.conversation_log.clear()
        
    def basic_io_bot(self, filename=None, expand=False):
        initial_prompt = ""
        if filename != None:
            intial_prompts = []
            for file in filename:
                intial_prompts.append(self.db_manager.read(2, file))
            initial_prompt = self.expander.base_expansion(intial_prompts)
        self.db_manager.write(1, input("\nUser: "))
        user_prompt = self.db_manager.read(1) 
        self.db_manager.delete(1)
        expansion_prompts = []
        if expand:
            expansion_prompts = self.expander.expansion_generator(user_prompt)
            if expansion_prompts[0] == "NOT APPLICABLE":
                expansion_prompts.pop(0)
        user_prompt = "USER PROMPT: " + user_prompt
        final_prompt = self.expander.base_expansion([initial_prompt] + expansion_prompts + [user_prompt])
        print(final_prompt)
        response = self.generator.base_generation(final_prompt)
        self.db_manager.write(3, response)
        print(f"Bot: {response}")
        
