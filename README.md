# Portfolio Website

A professional portfolio website built with Django showcasing data science, machine learning, and analytics projects.

## Features

- **Home Page**: Professional introduction and contact information
- **Projects**: Showcase of technical projects with detailed descriptions
- **Education**: Academic background and achievements
- **Experience**: Professional experience and skills
- **Contact**: Contact form for inquiries and opportunities

## Technologies Used

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (local), PostgreSQL (production)
- **Deployment**: Render.com

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Visit**: http://localhost:8000

## Deployment on Render

1. **Push to GitHub**: Ensure your code is in a GitHub repository
2. **Connect to Render**: Sign up at [render.com](https://render.com)
3. **Create Web Service**: Connect your GitHub repo
4. **Configure**:
   - **Name**: `portfolio`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn Portfolio.wsgi:application`
   - **Plan**: `Free`

## Environment Variables

No environment variables required for basic deployment.

## Project Structure

```
Portfolio/
├── Portfolio/          # Django project settings
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── build.sh          # Build script for Render
├── requirements.txt  # Python dependencies
└── manage.py         # Django management script
```

## Contact

For questions or support, please use the contact form on the website.

## License

This project is open source and available under the MIT License.
