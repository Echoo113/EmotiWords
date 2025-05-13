from typing import Dict, List, Optional
from openai import OpenAI
from dataclasses import dataclass
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class WordExplanation:
    word: str
    definition: str
    mnemonic: str
    example: str
    native_language: str
    learning_style: str

class WordExplainer:
    def __init__(self, api_key: str = None):
        """Initialize the WordExplainer with OpenAI API key."""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in .env file or pass it directly.")
        self.client = OpenAI(api_key=self.api_key)

    def generate_explanation(
        self,
        word: str,
        native_language: str = "English",
        learning_style: str = "standard"
    ) -> WordExplanation:
        """
        Generate a personalized explanation for a word.
        
        Args:
            word: The word to explain
            native_language: User's native language (e.g., "Chinese", "Spanish")
            learning_style: Preferred learning style (e.g., "analogy", "story", "standard")
            
        Returns:
            WordExplanation object containing the generated explanation
        """
        prompt = self._create_prompt(word, native_language, learning_style)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful vocabulary learning assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            
            # Parse the response and create WordExplanation object
            explanation = self._parse_response(response.choices[0].message.content)
            return WordExplanation(
                word=word,
                definition=explanation["definition"],
                mnemonic=explanation["mnemonic"],
                example=explanation["example"],
                native_language=native_language,
                learning_style=learning_style
            )
            
        except Exception as e:
            raise Exception(f"Error generating word explanation: {str(e)}")

    def _create_prompt(
        self,
        word: str,
        native_language: str,
        learning_style: str
    ) -> str:
        """Create a prompt for the GPT model based on user preferences."""
        return f"""
        Please provide a comprehensive explanation for the word '{word}'.
        
        Requirements:
        1. Provide a clear definition in {native_language}
        2. Create a memorable mnemonic device using {learning_style} approach
        3. Include a practical example sentence
        
        Format the response as:
        Definition: [definition]
        Mnemonic: [mnemonic]
        Example: [example]
        """

    def _parse_response(self, response: str) -> Dict[str, str]:
        """Parse the GPT response into structured data."""
        lines = response.strip().split('\n')
        explanation = {
            "definition": "",
            "mnemonic": "",
            "example": ""
        }
        
        current_section = None
        for line in lines:
            line = line.strip()
            if line.startswith("Definition:"):
                current_section = "definition"
                explanation["definition"] = line.replace("Definition:", "").strip()
            elif line.startswith("Mnemonic:"):
                current_section = "mnemonic"
                explanation["mnemonic"] = line.replace("Mnemonic:", "").strip()
            elif line.startswith("Example:"):
                current_section = "example"
                explanation["example"] = line.replace("Example:", "").strip()
            elif current_section and line:
                explanation[current_section] += " " + line
                
        return explanation

# Example usage
if __name__ == "__main__":
    try:
        explainer = WordExplainer()  # Will use API key from .env file
        explanation = explainer.generate_explanation(
            word="ameliorate",
            native_language="Chinese",
            learning_style="analogy"
        )
        print(f"Word: {explanation.word}")
        print(f"Definition: {explanation.definition}")
        print(f"Mnemonic: {explanation.mnemonic}")
        print(f"Example: {explanation.example}")
    except Exception as e:
        print(f"Error: {str(e)}") 