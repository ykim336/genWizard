from database_manager import DatabaseManager
from generator import Generator
from expander import Expander

class Comparator:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.expander = Expander()
        self.generator = Generator()

    def base_evaluation_function(self, prompt, filename):
        file_content = self.db_manager.read(2, filename)
        expanded_prompt = self.expander.base_expansion([prompt, file_content])
        score_string = self.generator.base_generation(expanded_prompt)
        return float(score_string)

    def evaluate_reliability_function(self, prompt):
        return self.base_evaluation_function(prompt, "evaluate_reliability_prompt.txt")

    def evaluate_validity_function(self, prompt):
        return self.base_evaluation_function(prompt, "evaluate_validity_prompt.txt")

    def base_comparator_function(self, num=5):
        comparator_prompt_content = self.db_manager.read(2, "base_comparator_prompt.txt")
        prototype_outputs = self.db_manager.get_latest_file(self.db_manager.path_mapping[3], num)

        modified_prototype_outputs = []
        for output in prototype_outputs:
            reliability_score = str(self.evaluate_reliability_function(output))
            validity_score = str(self.evaluate_validity_function(output))
            modified_output = self.expander.base_expansion([
                output,
                "Reliability Score: " + reliability_score, 
                "Validity Score: " + validity_score,
                "-------------------------------------------------------------------"])
            modified_prototype_outputs.append(modified_output)

        final_input = self.expander.base_expansion([comparator_prompt_content] + modified_prototype_outputs)
        return self.generator.base_generation(final_input)
