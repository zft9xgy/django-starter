from django.conf import settings


def global_variables(request):
    """
    Variables globales que serán lanzadas en todas las templates.
    """

    domain = settings.DOMAIN
    seo_index = settings.SEO_INDEX
    seo_follow = settings.SEO_FOLLOW
    
    context = {
        'domain' : domain,
        'seo_index':seo_index,
        'seo_follow':seo_follow,
    }
    return {'global': context}