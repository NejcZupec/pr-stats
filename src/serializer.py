import json


def stringify_time(d):
    return d.isoformat().replace('T', ' ').split('.')[0] if d else ''


def to_json(pull_requests, filename='github_data.json'):
    """Dump pull request data to JSON file"""
    data = dict()

    # TODO: slow! fetches assignees and users for every PR instead of in batch!

    for pr in pull_requests:
        data[pr.id] = {
            'id': pr.id,
            'title': pr.title,
            'url': pr.url,
            'owner': pr.user.name or pr.user.email,
            'assignees': [
                person.name or person.email for person in pr.assignees
            ],
            'state': pr.state,
            'created_at': stringify_time(pr.created_at),
            'merged_at': stringify_time(pr.merged_at),
        }

    with open(filename, 'w') as f:
        json_data = json.dumps(data, indent=4)
        f.write(json_data)
