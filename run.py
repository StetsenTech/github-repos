"""Script that allows users to search an organizaton's repo"""

import requests
import requests_cache
import json
import click

# Sets up caching for requests, so that repeated requires don't trigger GitHub limit
requests_cache.install_cache(cache_name='github_cache', backend='sqlite', expire_after=180)

@click.command()
@click.option("--org", prompt="Enter organization name",
              help="Name of organization to search repositories for (Required)")
@click.option("--sort_by",
              help="Options: stargazers_count, forks_count, contributors_count")
@click.option('--output_file', '-o', default="repos.out",
              type=click.Path(exists=False),
              help="Path to output file")
def organization_repos(org:str, sort_by:str,output_file:str) -> list:
    """Given an organization, searches through
    
    Arguments:
        org {str} -- Name of organization
        sort_by {str} -- Optional parameter to sort repositories by
        output_file {str} -- File to put output
    
    Returns:
        list -- List of all repositories for an organization
    """

    # Get organization information
    org_request = requests.get(f'https://api.github.com/orgs/{org}')

    if not org_request.ok:
        org_request.raise_for_status()

    org_info = json.loads(org_request.content or org_request.text)

    # Follow URL provided for repos located in the response
    repos_request = requests.get(org_info.get('repos_url'))

    if not repos_request:
        repos_request.raise_for_status()

    repos_info = json.loads(repos_request.content or repos_request.text)
    
    # If a sort is specified, sort the list of repositories by key
    if sort_by and sort_by in ['stargazers_count', 'forks_count', 'contributors_count']:
        if sort_by == "contributors_count": 
            # Since contributor count isn't provided, have to manually calculate it
            # Only do so if specified because it is an additional request
            for i, repo in enumerate(repos_info):
                # Follow URL for contributors located in response
                contributors_request = requests.get(repo.get('contributors_url'))
                        
                if not contributors_request:
                    contributors_request.raise_for_status()

                contributors_info =  json.loads(contributors_request.content or contributors_request.text)
                
                # Append the contributors count to repository information
                repos_info[i]['contributors_count'] = len(contributors_info)
        
        sorted(repos_info, key=lambda x: x.get(sort_by))

    with open(output_file, 'w+') as result_out:
        print("Writing output to", output_file)
        json.dump(repos_info, result_out)

    return repos_info

if __name__ == '__main__':
    organization_repos()