
# Django Mini App

This is a simple Django application designed to display posts on various topics. Each post contains the following fields:

- **Title**: A brief heading for the post.
- **Date**: The date when the post was created or published.
- **Author**: The name of the post's author.
- **Excerpt**: A short summary or snippet of the post content.
- **Description**: The detailed content displayed when opening a specific post.

## Features

- Displays a list of posts with titles, authors, and excerpts.
- Clicking on a post opens a detailed view showing the full description and associated details.
- Data is stored and managed using an SQLite database.


## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/saadfiaz/django-blogs-application
    cd django-blogs-application
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run database migrations to set up the SQLite database:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the homepage to see a list of posts.
- Click on a post title to view its full details, including the description.

## Database

The app uses SQLite as its default database. You can find the database file (`db.sqlite3`) in the project directory.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
