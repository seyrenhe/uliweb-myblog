from uliweb import expose, functions
from forms import BlogsForm

@expose('/')
def test():
    blogs = functions.get_model('blogs')
    blog = blogs.all().order_by(blogs.c.id.desc())
    form = BlogsForm()
    if request.method == 'POST':
        flag = form.validate(request.params)
        if flag:
            n = blogs(**form.data)
            n.username = request.user.username
            n.save()
    return {'blog': blog, 'form': form}



@expose('/delete/<id>')
def delete(id):
        functions.require_login()

        blogs = functions.get_model('blogs')
        n = blogs.get(blogs.c.id == id)
        if n:
                n.delete()
        return redirect('/')


@expose('/edit/<id>')
def edit(id):
        blogs = functions.get_model('blogs')
        if functions.require_login():
                return redirect(url_for(login))
        if request.method == 'GET':
                p = blogs.get(blogs.c.id==id)
                form = BlogsForm(data={'title':p.title,'content':p.content})
                return {'form':form}
        elif request.method == 'POST':
                form = BlogsForm()
                flag = form.validate(request.params)
                n = blogs.get(blogs.c.id == id)
                if n:
                        n.username = request.user.username
                        n.title    = form.data.title
                        n.content  = form.data.content
                        n.save()
                return redirect('/')


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


@expose('/admin')
 class AdminView(object):
#     def __begin__(self):
#         functions.require_login()
#         if not request.user.is_superuser:
#             error('you have no permisstion to visit the page')


    @expose('')
    def index(self):
        return {}