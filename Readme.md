# Research Portal

A simple full-stack web app for posting and managing research opportunities.
Faculty can create, view, update, and delete research opportunities, and
mark them as Open or Closed. Built with a Flask REST API backend, SQLite
database, and a plain HTML/CSS/JavaScript frontend.

## Technologies used

- Backend: Python, Flask, Flask-SQLAlchemy
- Database: SQLite (`research.db`)
- Frontend: HTML, CSS, JavaScript (no framework, communicates with the
  backend using `fetch`)
- API testing: Postman

## Project Structure

research-portal/
├── app.py                                     # Flask app: routes,model,DB config
├── requirements.txt                           # Python dependencies
├── templates/
│   └── index.html                             # Frontend (served by Flask)
├── postman/
│   └── Research_Portal_API.postman_collection.json
├── api-env/                                   # Virtual environment
└── instance/
    └── research.db                            # SQLite database


## Setup

1.Clone or download the project  , then open it in your editor.

2.Create and activate a virtual environment

   Windows:
   python -m venv api-env
   api-env\Scripts\activate

   macOS/Linux:
   python3 -m venv api-env
   source api-env/bin/activate

3.Install dependencies

   pip install -r requirements.txt

4.Run the app

   python app.py

   The database file `research.db` is created automatically on first run.

5.Open the app

   Go to [http://localhost:5000/](http://localhost:5000/) in your browser.

## API Endpoints

Base URL: `http://localhost:5000`

| Method | Endpoint                     | Description                          |
|--------|-------------------------------|--------------------------------------|
| GET    | `/api/researchtitles`         | Get all research opportunities       |
| GET    | `/api/researchtitles/<id>`    | Get one research opportunity by id   |
| POST   | `/api/researchtitles`         | Create a new research opportunity    |
| PUT    | `/api/researchtitles/<id>`    | Update a research opportunity        |
| DELETE | `/api/researchtitles/<id>`    | Delete a research opportunity        |

### Research opportunity fields

| Field                   | Type    | Required |
|--------------------------|---------|----------|
| `Research_title`         | string  | Yes      |
| `Research_description`   | string  | Yes      |
| `Research_area`           | string  | Yes      |
| `Faculty_name`            | string  | Yes      |
| `Departement`             | string  | Yes      |
| `Required_skills`         | string  | Yes      |
| `Avaliable_positions`     | integer | Yes      |
| `Application_deadline`    | string (date) | Yes |
| `status`                  | string (`Open` or `Closed`) | Yes |

### Example request body (POST / PUT)

json
{
  "Research_title": "AI in Healthcare",
  "Research_description": "Using machine learning to detect diseases",
  "Research_area": "Artificial Intelligence",
  "Faculty_name": "Dr. Ahmed",
  "Departement": "Computer Science",
  "Required_skills": "Python, ML",
  "Avaliable_positions": 2,
  "Application_deadline": "2026-12-01",
  "status": "Open"
}

## Frontend Features

The frontend (`templates/index.html`) is served by Flask at `/` and talks
only to the REST API above — no data is hard-coded.

- View all research opportunities in a table
- View the full details of a selected opportunity
- Add a new research opportunity through a form
- Edit an existing opportunity
- Change an opportunity's status between Open and Closed
- Delete an opportunity, with a confirmation prompt
- Success and error messages for every action
- Required-field and basic input validation before submitting the form

## Testing with Postman

A ready-made collection is included at
`postman/Research_Portal_API.postman_collection.json`.

1. Open Postman and click Import.
2. Select the collection file above.
3. Make sure the backend is running (`python app.py`).
4. Run Create research first to add sample data, then try the other
   requests. The `baseUrl` variable is already set to
   `http://localhost:5000`.

## Notes

- The database resets only if `research.db` is deleted; otherwise data
  persists between runs.
- CORS is not required because the frontend is served by the same Flask
  app that hosts the API.