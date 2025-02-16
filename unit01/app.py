from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool, tool
import datetime
import requests
import pytz
import yaml
from smolagents.default_tools import FinalAnswerTool

import requests

from Gradio_UI import GradioUI


@tool
def visit_webpage(url: str) -> str:
    """Fetches the content of a webpage.

    Args:
        url: A URL.

    Returns:
        Success if url was successfully resolved, Failed - otherwise.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"


@tool
def check_valid_url(url: str) -> str:
    """Resolving url.

    Args:
        url: A URL.

    Returns:
        Success if url was successfully resolved, Failed - otherwise.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        return "Success"
    except requests.RequestException as e:
        s = f"Failed to fetch image from {url}: {e}"
        return s


# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def square(number: int) -> str:  # it's import to specify the return type
    # Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that squares given number
    Args:
        number: a number to square
    """
    return number ** 2


@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()

search_tool = DuckDuckGoSearchTool(max_results=20, verify=False, timeout=60)

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
model_id = 'https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud'

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id=model_id,  # 'Qwen/Qwen2.5-Coder-32B-Instruct',  # it is possible that this model may be overloaded
    custom_role_conversions=None,
)

# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[check_valid_url, visit_webpage, search_tool, get_current_time_in_timezone, square, final_answer],
    ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)

GradioUI(agent).launch()
