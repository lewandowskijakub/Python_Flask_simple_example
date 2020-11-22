
HEADERS = ["Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status"]


def get_headers():
    return HEADERS


def get_user_stories():
    return [{HEADERS[0]: 1, "Story Title": "Some title", "User Story": "After click button is everything okay",
             "Acceptance Criteria": "Login button works", "Business Value": 100, "Estimation": 2,
             "Status": "pending"},
            {HEADERS[0]: 2, "Story Title": "Some title2", "User Story": "After login is logon",
             "Acceptance Criteria": "User can login", "Business Value": 92, "Estimation": 1,
             "Status": "done"},
            {HEADERS[0]: 3, "Story Title": "Some title3", "User Story": "33333333333333333333333",
             "Acceptance Criteria": "works", "Business Value": 87, "Estimation": 10,
             "Status": "in-progress"}
            ]


def get_user_story(id):
    stories = get_user_stories()
    for story in stories:
        if story[HEADERS[0]] == int(id):
            return story

    return {}
