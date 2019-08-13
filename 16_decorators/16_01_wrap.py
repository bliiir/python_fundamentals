'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

def tagger(tag):
    def deco(func):
        def wrapper(text):
            raw = func(text)
            html = f'<{tag}>{raw}</{tag}>'
            return html
        return wrapper

@tagger('div')
def make_html(text):
    return text

print(make_html('Some text'))


# def tagger(func):

#     def wrapper(text):
#         raw = func(text)
#         html = f'<div>{raw}</div>'
#         return html
#     return wrapper

# @tagger('div')
# def make_html(text):
#     return text

# print(make_html('Some text'))



# def tag_decorate(func):
#    def func_wrapper(name):
#        return "<p>{0}</p>".format(func(name))
#    return func_wrapper

# @p_decorate
# def make_html(name):
#    return "lorem ipsum, {0} dolor sit amet".format(name)

# print(get_text("John"))

# Outputs <p>lorem ipsum, John dolor sit amet</p>