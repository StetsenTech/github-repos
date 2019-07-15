# GitHub Organization Sortable Dashboard

Simple application that provides a summary dashboard for GitHub

## Documentation

* [Getting Started](GETTING_STARTED.md) - Steps on how to set up project

## Using the CLI

Running the application's CLI will produce a JSON file that can be used for making an visual interface

### Available commands

```bash
$ python run.py --help
Usage: run.py [OPTIONS]

  Given an organization, searches through

  Arguments:     org {str} -- Name of organization     sort_by {str} --
  Optional parameter to sort repositories by     output_file {str} -- File
  to put output

  Returns:     list -- List of all repositories for an organization

Options:
  --org TEXT              Name of organization to search repositories for
                          (Required)
  --sort_by TEXT          Options: stargazers_count, forks_count,
                          contributors_count
  -o, --output_file PATH  Path to output file
  --help                  Show this message and exit.
```

### Default

```bash
$ python run.py
Enter organization name: github
Writing output to repos.out
```

### Sort by a Count
```bash
$ python run.py --sort_by=contributors_count
Enter organization name: github
Sorting by: contributors_count
Writing output to repos.out
```

### Specifying Output File

```bash
$ python run.py -o different_file.out
Enter organization name: github
Writing output to different_file.out
```

## TO-DO List
- [ ] Create RESTful API using Flask to serve JSON
- [ ] Make a simple UI to demostrate sorting
- [ ] Add header for API token to avoid Github Limits
