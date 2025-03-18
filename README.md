# aviateassignment
### Description
   create a table called "Candidate" with columns: [Name, Age, Gender, Email, Phone number]
   - You have to create api endpoints to: create, update and delete a candidate. Also create an api endpoint to Search candidates.
     
## Features

- **CRUD Operations:** Perform create, read, update, and delete operations on candidate records.
- **Search Functionality:** Filter candidates based on search terms in their names as per the relevancy.
-  **added swagger**: Better visualisation of apis on browser integrated swagger as well

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rathorharish07/aviateassignment.git
   cd aviateassignment/
   
2. **Set Up a Virtual Environment**
   ```bash
   create virtualenv and activate
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Run the Development Server**
   ```bash
   python manage.py runserver
6. **open browser and run**
    ```bash
    like if you are running locally and on port 8000 then go to
     http://localhost:8000/doc/
7. **test apis**
   ```bash
   for create:        *POST*    api/candidate/
   
   for update:
      partial update: *PATCH*   api/candidate/{id}/
      update:         *PUT*     api/candidate/{id}/
   
   for delete:        *DELETE*  api/candidate/{id}/
   
   for search:        *GET*     api/candidate/?name=<YOUR SEARCH STRING>
   
