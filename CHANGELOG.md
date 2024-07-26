# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.3.3]

- [85b5967](https://github.com/zft9xgy/rafaelcosquiere.com/commit/85b59677335eb269470d4074d80b99cb013038f6) Refactor tags. Move tags into notes and unset Tags app
- [c6b5b4c](https://github.com/zft9xgy/rafaelcosquiere.com/commit/c6b5b4c8e11485f9088c813c0ce9dc1e7468efd0) Add: get_tags return a list with tags that got notes only
- [87b8447](https://github.com/zft9xgy/rafaelcosquiere.com/commit/87b8447a5ad48aa83a2dc50c1fa1d62402f25960) Fix: show only note published in tags view
- [c535731](https://github.com/zft9xgy/rafaelcosquiere.com/commit/c5357312d88b4a56321cfc06f820f8629e16dcf9) Fix: show only note published in single tag view

## [0.1.1]

### Change

- [90d3ebe](https://github.com/zft9xgy/rafaelcosquiere.com/commit/90d3ebeae66a63424505e48d34f705447c3f076e) Change created_date on models Note, Project and Page to be editable.
- [0872024](https://github.com/zft9xgy/rafaelcosquiere.com/commit/0872024fc51e92e182b90813e7b274887218da51) When a new Tag is created slug will be autopopulate based on Tag name.

## [0.0.0] - 2024-07-25

Fist release, still in beta status.

### Added

- Models Notes, Pages, Tags, Projects
- general management of meta robots index/noindex and follow/nofollow from settings.py
- sitemap.xml management
- robots.txt, humants.txt and security.txt management
- text edition from admin panel as MD or html
- draft and published status for Notes
- dynamic \<title\> tag on pages
- dynamic seo meta title, meta description, meta robots index, and meta robots follow on Notes and Pages.
- creation of favicon
- files and images upload from third-party package (django-filer)[https://github.com/django-cms/django-filer]
