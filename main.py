import math
import openai, re
from tools import write_to_file
from constants import OPENAI_KEY, OPENAI_ORG_CODE, URL
from summerize import scrape_webpage

api_key = OPENAI_KEY

openai.api_key = api_key

adcontext = scrape_webpage(URL)


def split_and_limit(input_string, n):
    words = input_string.split()
    result = []
    for i in range(0, len(words), n):
        result.append(" ".join(words[i : i + n]))
    return result


context_data = split_and_limit(adcontext, 250)


def context_builder(txts):
    context = [
        {
            "role": "system",
            "content": """You are a strict assistant that generates compelling Facebook ads following strict rules.
            The user will provide website content in parts, and you need to generate ads for posting using Facebook Ads Manager.
            """,
        }
    ]
    context = []
    for txt in txts:
        context.append({"role": "user", "content": txt})
    return context


CONTEXT = context_builder(context_data)
CONTEXT.append(
    {
        "role": "user",
        "content": """
        Generate a high-converting 120-word Facebook ad targeting bloggers using the Hook, Story, and Offer format. Adhere to the specified limits for each section:
        Don't forget to include the emojis and the ad should be only in this format.
        [Hook] (10 words max)
        [Story] (40 words max, in paragraph format with minimum three lines)
        [Offer] (60 words max, splitted in bullet points, minimum 5 lines)
        [Links]
        
        follow this structure very strictly
        """,
    }
)

DIVIDER = "-------------------------------x----------------------x-------------------------------"


def updateContext(whoSaid, what):
    c = {"role": whoSaid, "content": what}
    CONTEXT.append(c)


def generateAds(times):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=CONTEXT, n=times, presence_penalty=-2.0
    )
    for choice in response.choices:
        print(choice.message.content)
        print(DIVIDER)
        yield choice.message.content


ads = []

for e in generateAds(10):
    ads.append(e)

write_to_file(
    "ads.txt",
    f"\n{DIVIDER}\n".join(ads),
)
