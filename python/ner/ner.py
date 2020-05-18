import os
import requests
import json


# endpoint to query - you can get this on the market place of dploy.ai
dploy_url = "https://api.dev.dinosl1ke1cecream.dploy.ai/v1/predictions/810c94ff-dd58-48c7-8cd3-1082d6dce49d"

if __name__ == '__main__':
    # set your environment variables for storing the api key and user id token. 
    # alternatively, replace these lines with the actual values
    api_key = os.environ['apikey']
    user_id = os.environ['userid']
    text = "Lisp (historically LISP) is a family of programming languages with a long history and a distinctive, fully parenthesized prefix notation.[3] Originally specified in 1958, Lisp is the second-oldest high-level programming language in widespread use today. Only Fortran is older, by one year.[4][5] Lisp has changed since its early days, and many dialects have existed over its history. Today, the best-known general-purpose Lisp dialects are Racket, Common Lisp, Scheme and Clojure. "
    # these headers need to be present to authorize requests
    headers = {
            'content-type': 'application/json',
            'x-api-key': api_key,
            'x-api-user': user_id,
            # client and client-version can be any string for now 
            'client-version': 'v1.0.0',
            'client': 'script'
            }
    r = requests.post(url = dploy_url, json={"text": text}, headers = headers)
    data = json.loads(r.text)
    print(data["annotated_text"])