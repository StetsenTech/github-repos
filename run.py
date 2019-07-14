import requests
import requests_cache
import json

requests_cache.install_cache(cache_name='github_cache', backend='sqlite', expire_after=180)
org_request = requests.get('https://api.github.com/orgs/github')

if not org_request.ok:
    raise Exception

org_info = json.loads(org_request.content or org_request.text)
repos_request = requests.get(org_info.get('repos_url'))

if not repos_request:
    raise Exception

repos_info = json.loads(repos_request.content or repos_request.text)

for i, repo in enumerate(repos_info):
    contributors_request = requests.get(repo.get('contributors_url'))
            
    if not contributors_request:
        raise Exception

    contributors_info =  json.loads(contributors_request.content or contributors_request.text)
    repos_info[i]['contributors_count'] = len(contributors_info)


for s in ['stargazers_count', 'forks_count', 'contributors_count']:
    print(s)
    a = sorted(repos_info, key=lambda x: x.get(s))
        
    for repo in a:
        print(repo.get(s))

