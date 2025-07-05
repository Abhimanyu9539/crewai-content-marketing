# Load dotenv
import dotenv
import agentops
dotenv.load_dotenv()

agentops.init()

#!/usr/bin/env python
import os
import sys
import warnings
from datetime import datetime

# Disable AgentOps telemetry to avoid circular import warnings
os.environ['AGENTOPS_ENABLED'] = 'false'

from crewai_content_marketing.crew import ContentMarketingFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file runs the two-crew content marketing flow:#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from content_marketing_crew.crew import ContentMarketingFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# flow locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the content marketing flow.
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
        # Initialize and run the flow
        flow = ContentMarketingFlow()
        result = flow.kickoff(inputs=inputs)
        
        print("\n" + "=" * 60)
        print("✅ Content Marketing Flow completed successfully!")
        print("📁 Check the output directory for generated content files:")
        print("   • instagram_post.md")
        print("   • linkedin_post.md") 
        print("   • twitter_tweet.md")
        print("   • facebook_post.md")
        print("   • blog_post.md")
        
        return result
        
    except Exception as e:
        raise Exception(f"An error occurred while running the flow: {e}")


if __name__ == "__main__":
    run()