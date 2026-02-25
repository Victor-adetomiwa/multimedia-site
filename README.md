# Multimedia Website — Django Assignment

A basic Django web app for uploading and viewing images, videos, and audio files.

## Features
- Upload images, videos, and audio files
- View all media on the homepage
- Play/view media on a detail page
- Delete your own uploads
- User login/logout (Django built-in auth)
- Admin panel

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Create a superuser (for admin + login)
```bash
python manage.py createsuperuser
```

### 4. Run the development server
```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Project Structure

```
multimedia_site/
├── manage.py
├── requirements.txt
├── media/                  ← uploaded files go here (auto-created)
├── mysite/
│   ├── settings.py
│   └── urls.py
└── media_app/
    ├── models.py           ← MediaItem model
    ├── views.py            ← home, detail, upload, delete
    ├── forms.py            ← upload form
    ├── urls.py             ← app URL routes
    ├── admin.py            ← admin registration
    └── templates/
        ├── media_app/
        │   ├── base.html
        │   ├── home.html
        │   ├── detail.html
        │   ├── upload.html
        │   └── confirm_delete.html
        └── registration/
            └── login.html
```

## URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage — list all media |
| `/upload/` | Upload a file (login required) |
| `/media/<id>/` | View/play a media item |
| `/media/<id>/delete/` | Delete a media item |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/admin/` | Django admin panel |
