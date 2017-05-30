from fabric.api import local



def test():
    local('./manage.py test')

def add():
    local('git add -A')

def commit():
    local('git commit -am "fixed" ')

def fetch():
    local('git fetch origin develop && git pull origin develop')

def push():
    local('git push -u origin develop')

def deploy():
    test()
    add()
    commit()
    push()