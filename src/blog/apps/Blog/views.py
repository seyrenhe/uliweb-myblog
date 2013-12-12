#coding=utf-8
from uliweb import expose, functions
from forms import BlogsForm

@expose('/')
def index():
    blogs = functions.get_model('blogs')
    blog = blogs.all()
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