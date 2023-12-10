from constants import *
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.customaudience import CustomAudience

# Set your Facebook API credentials
app_id = APP_ID
app_secret = APP_SECRET
access_token = ACCESS_TOKEN
FacebookAdsApi.init(app_id, app_secret, access_token)

# Define the parameters for your custom audience
audience_name = "Your Custom Audience Name"
description = "Description for your custom audience"
customer_file_source = CustomAudience.CustomerFileSource.user_provided_only

# Create the custom audience
audience = CustomAudience(parent_id=AD_ACCOUNT_ID)
audience[CustomAudience.Field.name] = audience_name
audience[CustomAudience.Field.subtype] = CustomAudience.Subtype.custom
audience[CustomAudience.Field.description] = description
audience[CustomAudience.Field.customer_file_source] = customer_file_source

# Save the custom audience
audience.remote_create()

# Print the ID of the newly created custom audience
print(f"Custom Audience ID: {audience.get_id()}")

# Now that the audience is created, you can add users to it
# Upload a list of user data to the audience (in this example, a list of email addresses)
user_data = [
    "sptiwari46289@gmail.com",
    # Add more user data here
]

# Add the user data to the custom audience
audience.add_users(CustomAudience.Schema.email_hash, user_data)

# Save the custom audience after adding users
audience.remote_update()

# Print the ID of the updated custom audience
print(f"Custom Audience ID (after adding users): {audience.get_id()}")
