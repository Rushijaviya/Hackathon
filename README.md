Assignment for a back-end development internship
========

This is Test Assignment submission for Back End Internship with AI Planet

Task
--------

- Create a submissions app where one can submit their hackathon submissions & see the list. 
- The hackathon can be posted by anyone and they will be authorized before they are allowed to post hackathons. Users should be able to come and submit some code or files as hackathon submissions. 
- Create different APIs for various task.
- Unit Tests

## How to run
```bash
# Fetch the repo using git
$ git clone https://github.com/Rushijaviya/Hackathon.git

# Go to the directory
$ cd Hackathon

# Install a compatible version
$ pip install -r requirements.txt

# Database Migrations
$ python manage.py makemigrations
$ python manage.py migrate

# To run server
$ python manage.py runserver

# For Testing
$ python manage.py test
```

## API Details:
<details><summary>1. Create Hackathon</summary>

    - URL: api/v1/create-hackathon/
    - Request Type: POST
    - Request Body: title, created_by, submission_type, start_date, end_date, reward_prize, background_image, hackathon_image, description
</details>

<details><summary>2. List Hackathon</summary>

    - URL: api/v1/get-hackathon-list/
    - Request Type: GET
    - Optional: live/past/future
</details>

<details><summary>3. Register to Hackathon</summary>

    - URL: api/v1/register-to-hackathon/
    - Request Type: PATCH
    - Parameter: hackathon_id, user_id
</details>

<details><summary>4. Make Submission</summary>

    - URL: api/v1/create-user-submission/
    - Request Type: POST
    - Request Body: name, Summary, submission_image, submission_file, submission_link, submitted_by, hackathon
</details>

<details><summary>5. User list Hackathon</summary>

    - URL: api/v1/get-user-hackathon-list/
    - Request Type: GET
    - Parameter: username
    - Optional: live/past/future
</details>

<details><summary>6. User view Submission</summary>

    - URL: api/v1/view-user-submission/
    - Request Type: GET
    - Parameter: user_id
    - Optional: hackathon_id
</details>

Note:
--------
- No Front-end is made as goal is to develop APIs. 
- You can use postman for API Testing. 