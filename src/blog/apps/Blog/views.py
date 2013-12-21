from uliweb import expose, functions
from forms import BlogsForm

@expose('/')
def test():
    blogs = functions.get_model('blogs')
    blog = blogs.all().order_by(blogs.c.id.desc())
    return {'blog': blog}


@expose('/reader/<id>')
def detail(id):
    blogs = functions.get_model('blogs')
    blog = blogs.all()

    if request.method == 'GET':
        p = blogs.get(blogs.c.id == id)
        p.content

        if p:
            return {'blog': blog, 'p': p}
        else:
            return redirect('/')

