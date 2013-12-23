#coding=utf-8
from uliweb import expose, functions
from forms import AddForm, AddCForm


@expose('/')
class Blog(object):

    @expose('')
    def test(self):
        blogs = functions.get_model('blogs')
        print functions
        blog = blogs.all().order_by(blogs.c.id.desc())
        #页面编号
        #pageno = int(request.GET.get('page', 1)) - 1
        #每页文章数量
        print int(request.GET.get('page', 1))
        #后面的参数为请求网址，所有记录数， 总页数 每页记录数
        print blog
        pagination = functions.create_pagination(request.url, 10, 3, 4)


        return {'blog': blog,'pagination': pagination}


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
        #定义一个空列表，然后把settings里的ADMIN_MODELS配置里的model取出来,放到这个list里
        self.blogs = []
        for k in settings.ADMIN_MODELS.models:
            self.blogs.append(k)

    @expose('')
    def view(self):
        #objects = self.blogs.all()
        model = functions.get_model('blogs').all()
        print self.blogs
        print model
        return {'objects':model}

    def add(self):

        error = {}
        form = AddForm()
        model = functions.get_model('blogs')
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
                #d['category'] = request.POST['category']
                obj = model(**d)
                obj.save()
                return {'form':form}
           # return redirect(url_for(self.__class__.view))
    def addC(self):
        form = AddCForm()
        return {'form':form}
