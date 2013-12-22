#coding=utf-8
from uliweb import expose, functions
from forms import AddForm, AddCForm


@expose('/')
class Blog(object):

    @expose('')
    def test(self):
        blogs = functions.get_model('blogs')
        blog = blogs.all().order_by(blogs.c.id.desc())
        return {'blog': blog}


    @expose('/reader/<id>')
    def detail(self,id):
        blogs = functions.get_model('blogs')
        blog = blogs.all()

        if request.method == 'GET':
            p = blogs.get(blogs.c.id == id)
            p.content

            if p:
                return {'blog': blog, 'p': p}
            else:
                return redirect('/')

@expose('/god')
class BlogAdminView(object):
    def __init__(self):
        from uliweb import settings
        #import all needed model
        self.blogs = []
        for k in settings.ADMIN_MODELS.models:
            self.blogs.append(k)

    @expose('')
    def view(self):
        objects = self.blogs.all()

        return {'objects':objects}

    def add(self):

        error = {}
        form = AddForm()
        if request.method == 'GET':
            return {'form':form,'error':error}
        elif request.method == 'POST':
            #对数据进行保存
            #debug
            if not request.POST.get('title'):
                error['title'] = '不允许为空'
            if error:
                return {'form':form,'error':error}
            else:
                #save data
                print request.GET
                print request.POST
                d = {}
                d['title'] = request.POST['title']
                d['content'] = request.POST['content']
                d['category'] = request.POST['category']
                obj = self.blogs(**d)
                obj.save()
                return {'form':form}
           # return redirect(url_for(self.__class__.view))
    def addC(self):
        form = AddCForm()
        return {'form':form}
