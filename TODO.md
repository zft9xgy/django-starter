## ready to do

## nexts

- estandarizar lenguaje: inglés only.

### feat

- feat: una manera de añadir de forma automatica las pages que se crean en menu de footer o del header
- feat: sección de comentarios opcional en cada nota, posiblemente con api de github
- feat: añadir readtime and words count en metadata de notas
- feat: página web multilingüe
- feat: canonical on seometa settings

### bugs

- bug: seosettings must be applie to robots.txt file

## maybes and ideas

- link shorter for notes share
- corrector ortográfico, realmente lo necesito
- crear mi propio compresor de PDF online, es muy util y no me gusta subir documentacion a otros sitios.
- implement slugify to slug field -
- sitemaps 2.0 - splits the sitemaps into differents files like: notes_sitemap.xml , pages_sitemap.xml
- build a redirections modules to create redirections
- refactor the whole project to create a super 'webcontent' object

## done

- editor backend de textos md (finalmente se uso un preprocesador de markdown)
- estructura completa: Projects, Tags, Notes, Pages
- sitemap.xml (https://docs.djangoproject.com/en/5.0/ref/contrib/sitemaps/) / (https://christophergs.com/blog/django-sitemap-tutorial-for-humans)
- control sobre el robots
- control that only published notes can be accesibles, draft ones not
- change title tag on every page (https://www.forgepackages.com/guides/page-titles/)
- control sobre el seo metatitle and description og:titles etc https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag?hl=es
- cambiar los favicons
- gestion de media (django-filer)

## references

- https://docs.djangoproject.com/en/5.0/ref/urlresolvers/
- https://christophergs.com/
- learn about 'django.contrib.sites' and why this need it for sitemaps
- https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#date
- Project organization and structrure: https://stackoverflow.com/questions/40914554/django-views-in-project-directory
