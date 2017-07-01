from fabric.api import *
# import os
# from django.shortcuts import render, get_object_or_404
# from blog.models import Post
#
env.hosts = ['root@101.200.171.13']
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wind_blog.settings")

def test():
    local('./manage.py test')

def add():
    local('git checkout develop && git add -A')

def commit():
    local('git commit -am "fixed"  ')

def fetch():
    local('git fetch origin develop && git pull origin develop')

def push():
    local('git push -u origin develop')

# def uploadPosts():
#     base_dir = '/server/projects/wind_blog/blog-project/posts/'
#     latest_post_list = Post.objects.order_by('-date').exclude(title='about')
#     for post in latest_post_list:
#         title = post.title
#         content = post.body
#         with open(base_dir + title, 'wb') as f:
#             f.write(content)



def deploy():
    blog_dir = '/server/projects/wind_blog/blog-project'
    # test()
    # fetch()
    # add()
    # commit()
    # push()
    # remote deploy
    with prefix('cd ' + blog_dir + ' && source  ../bin/activate'):
        run('source ../bin/activate')
        run('source /etc/profile')
        run('git checkout develop && git pull origin develop')
        run('./manage.py test --settings wind_blog.production')
        run('pkill gunicorn')
        run('sleep 1')
        run('gunicorn wind_blog.wsgi -c gunicorn_setting.py', pty = False)

