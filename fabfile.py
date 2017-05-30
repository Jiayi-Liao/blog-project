from fabric.api import *

env.hosts = ['root@101.200.171.13']

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


def deploy():
    blog_dir = '/server/projects/wind_blog/blog-project'
    test()
    add()
    commit()
    push()
    # remote deploy
    with prefix('cd ' + blog_dir + ' && source  ../bin/activate'):
        run('source ../bin/activate')
        run('source /etc/profile')
        run('git checkout develop && git pull origin develop')
        run('./manage.py test --settings wind_blog.production')
        run('pkill gunicorn')
        run('sleep 1')
        run('gunicorn wind_blog.wsgi -c gunicorn_setting.py', pty = False)

