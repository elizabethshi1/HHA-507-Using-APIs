# -*- coding: utf-8 -*-
"""

@author: Elizabeth Shi
"""
# The API that I am connecting to is from Healthcare.gov. 
# This API that I used was the glossary from Healthcare.gov's content collection.
# The content collection is a group of posts by type of content.
# The API looks like a dictionary full of URLs. 
conda install requests
import requests
import pandas as pd

response =requests.get(' https://www.healthcare.gov/api/glossary.json')
response.status_code

json_response = response.json()
json_response

response_glossary = json_response['glossary']
response_glossary_df = pd.DataFrame(response_glossary)
