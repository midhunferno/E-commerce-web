from django import template
register=template.Library()

@register.filter(name='chunks')
def spliter(list,size):
    row=[]
    i=0
    for data in list:
        row.append(data)
        i=i+1
        if i==size:
            yield row
            i=0
            row=[]
    yield row        