def my_xml(tag_name, content='', **kwargs):
    attr = "".join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tag_name}{attr}>{content}</{tag_name}>'


print(my_xml('foo'))
print(my_xml('foo', 'bar'))
print(my_xml('foo', 'bar', a=1, b=2, c=3))
