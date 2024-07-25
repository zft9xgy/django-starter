import os
import django
import random
from datetime import datetime, timedelta
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalweb.settings')
django.setup()

from django.contrib.auth.models import User
from notes.models import Note
from tags.models import Tag
from projects.models import Project
from pages.models import Page


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def create_pages():

    pages_data = [
        {
            'title': 'About',
            'slug': 'about',
            'excerpt': 'This page is about me.',
            'content': '....'
        },
        {
            'title': 'Ideas',
            'slug': 'ideas',
            'excerpt': 'This page is about the ideas i got and want to share with others.',
            'content': '....'
        },
        {
            'title': 'Now',
            'slug': 'now',
            'excerpt': 'This page is about what im doing now.',
            'content': '....'
        }
    ]

    for page in pages_data:
        p, created = Page.objects.get_or_create(
            title=page['title'],
            slug=page['slug'],
            excerpt=page['excerpt'],
            content=page['content'],
        )

def create_projects():

    projects_data = [
        {
            'title': 'rafaelcosquiere.com',
            'short_description': 'This website in Django',
            'demo_link': 'http://127.0.0.1:8000/',
            'source_link': '',
            'note_link': '',
        },
        {
            'title': 'Django Simple CMS',
            'short_description': 'A really simple Django blog inspired by WordPress',
            'demo_link': 'https://dev.rafaelcosquiere.com/',
            'source_link': 'https://github.com/zft9xgy/django-simple-blog',
            'note_link': '',
        },
        {
            'title': 'Cloudflare DNS Updater w/Docker',
            'short_description': 'Automatic container that updates the public IP in CloudFlare every 5 minutes using the CloudFlare API.',
            'demo_link': '',
            'source_link': 'https://github.com/zft9xgy/cloudflare-ddns-docker',
            'note_link': '',
        }
    ]

    for project in projects_data:
        p, created = Project.objects.get_or_create(
            title=project['title'],
            short_description=project['short_description'],
            demo_link=project['demo_link'],
            source_link=project['source_link'],
            note_link=project['note_link']
        )



def create_tags():
    tags = ['django', 'python', 'webdevelopment', 'backend', 'api']
    for tag in tags:
        Tag.objects.get_or_create(name=tag, slug=tag.replace(' ', '-'))

def create_notes():
    tags = Tag.objects.all()

   
    notes_data = [
        {
            'title': 'Getting Started with Django',
            'slug': 'getting-started-with-django',
            'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.',
        },
        {
            'title': 'Building APIs with Django REST Framework',
            'slug': 'building-apis-with-django-rest-framework',
            'content': 'Django REST framework is a powerful and flexible toolkit for building Web APIs.',
        },
        {
            'title': 'Understanding Django ORM',
            'slug': 'understanding-django-orm',
            'content': 'The Django ORM is the interface used by Django to provide database access.',
        },
        {
            'title': 'Advanced Django Querying',
            'slug': 'advanced-django-querying',
            'content': 'Explore advanced querying techniques in Django to efficiently retrieve data from your database.',
        },
        {
            'title': 'Django Admin Customization',
            'slug': 'django-admin-customization',
            'content': 'Learn how to customize the Django admin interface to better suit your project’s needs.',
        },
        {
            'title': 'Testing in Django',
            'slug': 'testing-in-django',
            'content': 'A guide to writing tests in Django to ensure your application works as expected.',
        },
        {
            'title': 'Deploying Django Applications',
            'slug': 'deploying-django-applications',
            'content': 'Best practices for deploying Django applications to production environments.',
        },
        {
            'title': 'Securing Django Applications',
            'slug': 'securing-django-applications',
            'content': 'Learn how to secure your Django applications against common security threats.',
        },
        {
            'title': 'Using Celery with Django',
            'slug': 'using-celery-with-django',
            'content': 'An introduction to using Celery for background task processing in Django projects.',
        },
        {
            'title': 'Integrating Django with React',
            'slug': 'integrating-django-with-react',
            'content': 'How to integrate Django with React to build modern web applications.',
        },
        {
            'title': 'Building RESTful APIs with Django',
            'slug': 'building-restful-apis-with-django',
            'content': 'Learn how to build RESTful APIs using Django and Django REST Framework.',
        },
        {
            'title': 'Django Performance Optimization',
            'slug': 'django-performance-optimization',
            'content': 'Tips and techniques for optimizing the performance of your Django applications.',
        },
        {
            'title': 'Working with Django Signals',
            'slug': 'working-with-django-signals',
            'content': 'An overview of using signals in Django to handle events and trigger actions.',
        },
        {
            'title': 'Django Middleware Explained',
            'slug': 'django-middleware-explained',
            'content': 'Understanding middleware in Django and how to create custom middleware for your projects.',
        },
        {
            'title': 'Internationalization in Django',
            'slug': 'internationalization-in-django',
            'content': 'How to internationalize and localize your Django applications for multiple languages.',
        },
        {
            'title': 'Using Django Channels',
            'slug': 'using-django-channels',
            'content': 'Learn how to use Django Channels to add WebSocket support to your Django applications.',
        },
        {
            'title': 'Working with Django Forms',
            'slug': 'working-with-django-forms',
            'content': 'A comprehensive guide to creating and handling forms in Django.',
        },
        {
            'title': 'Django Templating Engine',
            'slug': 'django-templating-engine',
            'content': 'An introduction to the Django templating engine and how to use it effectively.',
        },
        {
            'title': 'Building E-commerce Sites with Django',
            'slug': 'building-e-commerce-sites-with-django',
            'content': 'Steps to create a fully functional e-commerce site using Django.',
        },
        {
            'title': 'Django Authentication and Authorization',
            'slug': 'django-authentication-and-authorization',
            'content': 'Implementing authentication and authorization in Django applications.',
        }
    ]


    # madrid_tz = pytz.timezone('Europe/Madrid')
    # start_date = madrid_tz.localize(datetime(2022, 1, 1))
    # end_date = madrid_tz.localize(datetime.now())

    for note in notes_data:
        author = User.objects.get(username='jade')
        #published_date = random_date(start_date, end_date)

        p, created = Note.objects.get_or_create(
            title=note['title'],
            slug=note['slug'],
            defaults={
                'content': note['content'],
                'status': random.choice(['draft', 'published']),
            }
        )
        if created:
            # Assign random tags to the note
            p.tags.set(random.sample(list(tags), k=random.randint(1, len(tags))))
            p.save()

            # p.published_date = published_date
            # p.save()

def main():
    create_tags()
    create_notes()
    create_projects()
    create_pages()
    print("Data population complete.")

if __name__ == '__main__':
    main()