#coding=utf-8
from uliweb import expose, functions
from forms import AddForm, AddCForm
from uliweb.orm import get_model

@expose('/')
class Blog(object):
    def __init__(self):
        self.model = get_model('blogs')

    @expose('')
    def test(self):
        from uliweb.utils.generic import ListView
        print functions
        #页面编号
        pageno = int(request.GET.get('page', 1)) - 1
        #每页文章数量,5为每页显示的文章
        rows_per_page = int(request.GET.get('rows', 8))
        print int(request.GET.get('rows', 1))
        #后面的参数为请求网址，所有记录数， 总页数, 每页文章数


        def modified_date(value, obj):
            return self._get_date(obj.modified_date)

        #fields_convert_map = {'modified_date': modified_date}

        #view = ListView(self.model, order_by=self.model.c.modified_time.desc(), pageno=pageno, rows_per_page=rows_per_page, fields_convert_map=fields_convert_map)
        view = ListView(self.model, order_by=self.model.c.modified_time.desc(), pageno=pageno, rows_per_page=rows_per_page)
        view.query()
        pagination = functions.create_pagination(request.url, view.total, pageno+1, rows_per_page)
        return {'objects': view.objects(),'pagination': pagination}


    @expose('/reader/<id>')
    def detail(self,id):
        #page for detail
        if request.method == 'GET':
            p = self.model.get(self.model.c.id == id)
            if p:
                #if p exist,pass the p to template detail.html
                print p
                return {'p': p}
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
                                                                                                                                                                       