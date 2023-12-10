import requests, json
from bs4 import BeautifulSoup
from tools import write_to_file

# URL = "https://www.linkedin.com/posts/zemoso-technologies_predicting-onset-of-diabetes-with-a-healthtech-activity-7128043464457396225-Ik2X?utm_source=share&utm_medium=member_desktop"
URL = "https://www.linkedin.com/posts/gowebknot_switch-to-hybrid-with-webknot-activity-7127606813268594688-ZRFR?utm_source=share&utm_medium=member_desktop"


def extract_scripts(element):
    for script in element.find_all("script"):
        if script.has_attr("type") and "application/ld+json" in script.attrs["type"]:
            script_text = script.get_text(strip=True).strip()
            return script_text
    return ""


def extract_divs(element):
    divs = {}
    classes = []
    for div in element.find_all("div"):
        div_text = div.get_text(strip=True).strip()
        if div.has_attr("class"):
            classes.append(",".join(div.attrs["class"]))
            div_id = ",".join(div.attrs["class"])
            if div_text:
                divs[div_id] = div_text
            if div.find_all("div"):
                nested_divs = extract_divs(div)
                if len(nested_divs):
                    divs[div_id] = nested_divs
    s = "\n".join(classes)
    write_to_file("classes.txt", s)
    return divs


def create_soup(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None


def scrape_linkedin_post(linkedin_post_url):
    soup = create_soup(linkedin_post_url)
    if soup:
        scriptcontent = extract_scripts(soup)
        obj = json.loads(scriptcontent)
        pretty_divs = json.dumps(obj, indent=4)
        write_to_file("scrapped_response.json", pretty_divs)


scrape_linkedin_post(URL)
