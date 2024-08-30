from invoke import task

@task
def setup(c):
    """Set up the project environment"""
    c.run("python -m venv venv")
    with c.prefix("source venv/bin/activate"):
        c.run("pip install -r requirements.txt")