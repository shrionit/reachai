from constants import API_BASE, AD_ACCOUNT_ID, ACCESS_TOKEN
import requests, json


def create_custom_audience(email_list):
    custom_audience_payload = {
        "name": "Custom Audience Name",
        "subtype": "CUSTOM",
        "customer_file_source": "USER_PROVIDED_ONLY",
        "data_source": "USER_PROVIDED_ONLY",
        "description": "Custom audience description",
        "is_value_based": False,
        # "origin_audience_id": "", # Optional
        "content": {"schema": ["EMAIL"], "data": email_list},
    }

    response = requests.post(
        f"{API_BASE}/act_{AD_ACCOUNT_ID}/customaudiences",
        params={"access_token": ACCESS_TOKEN},
        data=json.dumps(custom_audience_payload),
        headers={"Content-Type": "application/json"},
    )

    print(response.content)

    custom_audience_id = response.json().get("id")
    return custom_audience_id


if __name__ == "__main__":
    output = create_custom_audience(["sptiwari46289@gmail.com"])
    print({output})
