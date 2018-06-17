from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='cut')
def list_index_from_value(list_, value):
    return list_.index(value)