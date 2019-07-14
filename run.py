import requests
import requests_cache
import json
import click

requests_cache.install_cache(cache_name='github_cache', backend='sqlite', expire_after=180)

@click.command()
@click.option("--org", prompt="Enter organization name",
              help="Name of organization to search repositories for (Required)")
@click.option("--sort_by",
              help="Options: stargazers_count, forks_count, contributors_count")
def organization_repos(org, sort_by):
    org_request = requests.get(f'https://api.github.com/orgs/{org}')

    if not org_request.ok:
        org_request.raise_for_status()

    org_info = json.loads(org_request.content or org_request.text)
    repos_request = requests.get(org_info.get('repos_url'))

    if not repos_request:
        repos_request.raise_for_status()

    repos_info = json.loads(repos_request.content or repos_request.text)
    
    if sort_by and sort_by in ['stargazers_count', 'forks_count', 'contributors_count']:
        if sort_by == "contributors_count":
            for i, repo in enumerate(repos_info):
                contributors_request = requests.get(repo.get('contributors_url'))
                        
                if not contributors_request:
                    contributors_request.raise_for_status()

                contributors_info =  json.loads(contributors_request.content or contributors_request.text)
                repos_info[i]['contributors_count'] = len(contributors_info)
        
        sorted(repos_info, key=lambda x: x.get(sort_by))
    print(repos_info)
    return repos_info

if __name__ == '__main__':
    organization_repos()