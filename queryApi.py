from datetime import datetime
import requests
import json


def querygithub(searchterm):
    payload = {'q': searchterm}
    r = requests.get('https://api.github.com/search/repositories', params=payload)
    if r.ok:   # write an else clause for error handling if program starts to crash
        repoItem = json.loads(r.text or r.content)
    items = repoItem['items']
    # the following line sorts the items. The API does not offer sorting by 'created_at' so do it here.
    sortedItems = sorted(items, key=lambda item: datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)
    # Get newest give. Could add the paging thing to only fetch five, as per comment below
    # Although API seems to not have an obvious way of returning 5 rather than a minumum 30 so this tiny inefficiency remains.
    fivenewestRepos = sortedItems[:5]    
    
    # this following parameters for the request save network data and processing time by only pulling latest commit not many more
    # sorting does not seem to be necessary - the API is already sorting the commits from newest to oldest
    payload2 = {'page':'1', 'per_page':'1'} 

    fivenewest = []
    for repo in fivenewestRepos:
        repodict = {}
        repodict.update({'searchterm':searchterm})
        repodict.update({'repositoryName': repo['name']})
        repodict.update({'createdAt': repo['created_at']})
        repodict.update({'avatarLink': repo['owner']['avatar_url']})
        repodict.update({'ownerLogin': repo['owner']['login']})
        requesturl = 'https://api.github.com/repos/' + repo['full_name'] + '/commits'
        r2 = requests.get(requesturl, params=payload2)
        if r2.ok:                                                                 
            c = json.loads(r2.text or r2.content)  
        repodict.update({'shaString': c[0]['sha']})  # list of length 1 but still need to pull out 1st element.
        repodict.update({'commitMessage': c[0]['commit']['message']})
        repodict.update({'commitAuthorName': c[0]['commit']['author']['name']})
        fivenewest.append(repodict)

    # add the number to each dictionary
    counter = 1
    for rp in fivenewest:
        rp.update({'counter':counter})    
        counter += 1
    return fivenewest

