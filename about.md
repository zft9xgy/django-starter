## Un poco de contexto

Con la construcción de esta web como proyecto de aprendizaje, me gustaría compartir todo el proceso desde los requisitos iniciales, la toma de decisiones y algunas partes de la implementación.

Esta página tiene el objetivo de ser un portfolio, un lugar donde expresarme, donde compartir conocimientos, donde aprender haciendo, donde desarrolar ideas y mucho más.

Hace aglún tiempo ya que descubrí Django, y desde entonces siempre he tenido una atracción por su manera de hacer las cosas.

En ocasiones me he visto embaucado por el "sindrome de lo brillante" o "shiny syndrome", es decir, de sentirme atraido por la novedad y las nuevas técnologias. Y es que surgen nuevas técnologias cada día, como si de mala hierba se tratara.

Librerías de JS, Framworks y UI kits de CSS, frameworks de backend, nueva técnologia en servidores, despliegue de aplicaciones, etc etc.

Cada vez que descubro algo que no sabia, surgen mil cosas más y similar número de alternativas.

En el ecosistema de Django y la manera de hacer las cosas de Django, en contra, todo parece estar mucho más calmado, no hay grandes tendencias en Youtube queriendote vender cursos, no hay hype, todo es estable y va avanzando.

Y por otro lado esta Python, en lenguaje intutivo, rico, rápido, capaz, y con una comunidad y paquetes para todo.

Por suerte, estoy de vuelva en el camino, voy a centrarme en esta página web, y dedicarle tiempo, en implementar cosas, en aprender. Y si además, puede servirte de ayudar a ti, mucho mejor.

## Requisitos iniciales de esta web

Los requisitos de esta web son muy sencillos, al menos en la primera versión.

- Un area admin para poder gestionar el contenido, que ya la trae Django por defecto. (Nice)
- Un sistema de entradas clasificadas en etiquetas y que serán el core de la web.
- Un area de proyectos, donde poder publicar los proyectos.
- Un sistema de páginas, donde publicar contenido más estatico como página de about, ideas, now, aviso legal, cookies, etc.
- Capacidad para controlar el SEO de los contenidos, indexación, como se muestra en Google. Además de poder controlar el robots.txt y generación de un sitemap.xml.
- Un sistema de gestión de media, principalmente imágenes para poder usar en el contenido.

Y eso son los requisitos principales básicos para la primera versión.

## Arquitectura inicial de la web

Tened en cuenta que las decisiones que vaya tomando pueden no ser la más acertadas o más optimizar po multiples motivos:

- Porque sencillamanete quiero aprender y he decidido hacerlo de esa forma
- Por falta de conocimientos técnicos
- Por sencillez en el mantenimiento
- Por preferencia personal

En algunos proyectos, he sufrido mucho por paralisis por análisis y no quiero que esto me detenga mucho más. Todo se puede cambiar el en futuro si es necesario, lo importante es establecer una ruta y andarla.

Y ahora ya si, vamos con la arquitectura.

### Modelos

(poner aquí imagen de los modelos para cuando se pueda subir media a la web)

django-project: personalweb
django-apps: notes, tags, projects, pages

Aunque en primer lugar pensé en crear las etiquetas, dentro de notes, he decidido dejarla fuera para poder usarla en otros modelos como projects, pages o cualquier modelo futuro.

#### notes

El core principal de la web. Equivalente a entrada, post, articulo, etc. Yo he decidio llamarlo notes porque es algo más informal y que puede ser realmente cualquier cosa. He añadido la relación con author:User porque me parece coherente aunque no es realmente necesaria.

**Note:**

- id = models.UUIDField
- title = models.CharField
- excerpt = models.TextFiel
- slug = models.SlugField
- featured_image = models.ImageField
- author = models.ForeignKey(User)
- content = SanitizedProseEditorField # django-prose-editor
- created_date = models.DateTimeField
- updated_date = models.DateTimeField
- status = models.CharField(choices={'draft','published})
- tags = models.ManyToManyField(Tag)

#### tags

**Note:**

- id = models.UUIDField
- name = models.CharField
- slug = models.SlugField

#### projects

Se mostran en forma de tarjetas de una manera simple, con un titulo, una descripción y enlaces a source, demo y nota hablando del proyecto.

**Project:**

- id = models.UUIDField
- title = models.CharField
- short_description = models.TextField
- featured_image = models.ImageField
- demo_link = models.CharField
- source_link = models.CharField
- note_link = models.CharField
- created_date = models.DateTimeField
- updated_date = models.DateTimeField

#### pages

Se usará para páginas genéricas, sin usar etiquetas ni autor.

**Page:**

- id = models.UUIDField
- title = models.CharField
- excerpt = models.TextField
- slug = models.SlugField
- content = SanitizedProseEditorField # django-prose-editor
- created_date = models.DateTimeField
- updated_date = models.DateTimeField

## Deploy y production
