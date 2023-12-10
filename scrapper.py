import requests, json
from bs4 import BeautifulSoup

URL = "https://www.dfyplrbundles.com"
response = requests.get(URL)


def purge_id(id: str) -> str:
    return id[: id.rindex("-")] if id.count("-") > 0 else id


def extract_divs(element):
    divs = {}
    for div in element.find_all("div"):
        div_text = div.get_text(strip=True).strip()
        if div.has_attr("class"):
            div_id = div.attrs["class"]
            if div_text:
                divs[div_id] = div_text
            if div.find_all("div"):
                nested_divs = extract_divs(div)
                if len(nested_divs):
                    divs[div_id] = nested_divs
    return divs


def process_response(response: any):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        div_data = extract_divs(soup)
        pretty_divs = json.dumps(div_data, indent=4)
        print(pretty_divs)
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")


process_response(response)
