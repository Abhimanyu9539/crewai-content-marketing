#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
import agentops
from content_marketing.crew import ContentMarketingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load dotenv
import dotenv
dotenv.load_dotenv()

agentops.init()

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    inputs = {
        'topic': 'AI in Digital Marketing',
        'target_audience': 'Marketing professionals and business owners',
        'brand_tone': 'Professional yet approachable',
        'key_messages': [
            'AI makes marketing more efficient and effective',
            'Automation saves time while improving results',
            'Modern marketing tools are accessible to businesses of all sizes',
            'Data-driven decisions lead to better marketing outcomes'
        ],
        'call_to_action': 'Schedule a free consultation to discover how AI can transform your marketing strategy',
        'current_date': datetime.now().strftime("%B %d, %Y")
    }
    
    try:
        ContentMarketingCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()