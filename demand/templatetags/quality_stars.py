from django import template
register = template.Library()

@register.filter
def quality_stars(n_stars):
    star = '<i class="fas fa-star" style="color:#ffd700"></i>'
    no_star = '<i class="far fa-star" style="color:#cccccc"></i>'

    html = ''
    for i in range(0, n_stars):
        html += star

    for i in range(0, 8-n_stars):
        html += no_star

    return html
