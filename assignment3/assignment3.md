# Assignment 3: How to Django

This week, we're going to make our own mock (mock as in fake, not as in making fun; don't do that or we'll eat you) online newspaper using Django! 

![django](https://raw.githubusercontent.com/harvard-crimson/comp/master/assignment3/django.gif)
> Not this kind of Django. We don't condone aggression.

We'll walk you through step-by-step (via an abridged version of the full [Django tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial01/)). Fair warning: there is quite a bit to read! However, what you actually have to do is not too nebulous. If you're ever confused, don't be afraid to ask Tiffany (haotian.wu@thecrimson.com) or Kyle (kyle.kwong@thecrimson.com) for help!

## Setting up
1. Create the virtual environment for your project. If you want to call it `crimson_comp`, try running

        $ mkvirtualenv crimson_comp
2. Make sure you're in your virtual environment:

        $ workon crimson_comp
3. Install the latest version (1.8) of Django!
        
        (crimson_comp)$ pip install Django
        
## Create your project
Now it's time to set up the basic file structure for your django project!

First `cd` into a folder in your terminal, then run

    django-admin startproject newspaper

This will create a `newspaper` direcotry in your current directory. If it didn't work, try [troubleshooting here](https://docs.djangoproject.com/en/1.8/faq/troubleshooting/).

Let's see what was created!

```
newspaper/
├── manage.py
└── newspaper
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
Take note of the following files:

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/1.8/ref/django-admin/).
- `newspaper/settings.py`: Settings and configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/1.8/topics/settings/) will tell you more about how this file works.
- `newspaper/urls.py`: This file tells your Django app what pages correspond to what urls. Consider it your site's "table of contents". Read more about it [here](https://docs.djangoproject.com/en/1.8/topics/http/urls/).

That's literally it.

## Did it work? Let's check! (development server)

`cd` into the outer `newspaper` directory. In the terminal, run

    python manage.py runserver

You should see the following output:

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

September 29, 2015 - 05:32:53
Django version 1.8.4, using settings 'newspaper.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

You’ve started the Django development server, a lightweight Web server written purely in Python so you don't have to mess with fancy stuff like Apache.

It totally works, too! [Don't believe me? Just watch](https://www.youtube.com/watch?v=OPf0YbXqDm0&feature=youtu.be&t=65): you can navigate to [c](http://localhost:8000/) via your favorite web browser. You should now see a spiffy message!

Now to set up the database...

## Database Setup
We're going to use SQLite (the default) as our backend, but note that the crimson uses MySQL behind the scenes. Thankfully, Django abstracts away all the direct interaction with the database, so it looks all the same from your point of view!

### Tell Django you're using SQLite3
Django 1.8 uses SQLite3 by default, which is the easiest database to get started with. If you look at the contents of your `newspaper` directory, you'll see a new file `db.sqlite3` that was created when you ran the development server; this file contains the contents of your (initially emtpy) database. If you're curious about why it's there and called what it's called, check out the `DATABASES` variable in `settings.py`.

### Create tables inside the database
Django comes with a bunch of useful preinstalled apps (check out the `INSTALLED_APPS` variable in `settings.py`), and some of those apps require tables in your (currently empty) database. To create those tables, run

    $ python manage.py migrate
    
You should see some output that looks like

```
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
```

This runs a bunch of Python called **migrations** which create the necessary tables in your database. These particular migrations came packaged Django, but we'll be making our own soon enough.

## Creating models
Now that your environment – a “project” – is set up, you’re set to start doing work.
Each application ("app") you write in Django consists of a Python package, somewhere on your [Python path](https://docs.python.org/2/tutorial/modules.html#the-module-search-path), that follows a certain convention. Django made a nifty little command to create these directories for you!

Let's create an app called `content` to encapsulate the objects/database stuff that goes into an online newspaper. Navigate to the same folder as `manage.py` and run:

    python manage.py startapp content

That’ll create a directory `content`, which is laid out like this:

```
content/
├── __init__.py
├── admin.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

The first step in writing a database Web app in Django is to define your models – essentially, your database layout, with additional metadata.

In our content app, we'll create 4 models: **Content**, **Article**, **Image**, and **Contributor**. Article and Image should extend Content.

Sound familiar? You basically had the same type of structure in the last assignment! Except this time, instead of extending object, **Content** should extend **models.Model**, the base model for Django projects.

***TODO:*** Update `content/models.py` to look like this:

```
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    pass


class Image(Content):
    pass


class Contributor(models.Model):
    pass

```

As you can see, attributes of objects map to "fields" in Django, each of which is represented by an instance of a [Field](https://docs.djangoproject.com/en/1.8/howto/custom-model-fields/#django.db.models.Field) class – e.g., [CharField](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.CharField) for shorter strings and [DateTimeField](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.DateTimeField) for datetimes. This tells Django what type of data each field holds.

See [this link](https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types) for a list of all the built-in field types. **Sidenote:** the Django tutorial/documentation is nebulous and sometimes hard to navigate. If you're stuck, please don't be afraid to reach out to Tiffany or Kyle for help!

Finally, note a relationship is defined, using a ManyToManyField. That tells Django each Content is related to (possibly many) . Django supports all the common database relationships: many-to-ones, many-to-manys and one-to-ones.

***TODO:*** Now, let's fill in the blanks! Create the Article, Image, and Contributor classes.

### The Article model should (additionally) have:
**Attributes:**

- `text`: contains the text of an article. This might not fit into a `CharField`; see if you can find a Django field suitable for storing larger amounts of text.

**Methods:**

- `show()` (optional): Return a nicely formatted string with information about the Article. 

### The Image model should (additionally) have:

**Attributes:**

- `path`: contains the relative file path to the image file

**Methods:**

- `info()`: return a nicely formatted string with the title, the caption (subtitle), and other information you think is relevant

### The Contributor model should have:
**Attributes:**

- `first_name` 
- `last_name`
- `content`: a collection of Content objects that this contributor has made.

**Methods:**

- `die`: You're dead to us now; remove yourself from the database.

## Get your models in the database!

That small bit of model code gives Django a lot of information. With it, Django is able to:

- Create a database schema (`CREATE TABLE` statements) for this app.
- Create a Python database-access API for accessing Contributor and Content objects.

However, Django can't do any of this unless we tell our project that our `content` app exists. To do this, we'll need to modify the `INSTALLED_APPS` tuple in `settings.py`.

***TODO***: Add the string `'content'` to the `INSTALLED_APPS` tuple in `settings.py`.

Now we have all these awesome Python models, but we haven't actually created corresponding tables in the database yet (which was, like, the whole point of models, right?). To create these tables, we need to update our database. Remember those migrations we ran earlier? Let's make one of our own.

First, let's ask Django to create our migration for us. Run

    python manage.py makemigrations content

You should see some output telling you that it made a migration called called `0001_initial.py`. You'll also see some output giving you a summary of what that migration will do, but that's not good enough for us. Let's take a look at the actual migration!

If you look inside the `content/migrations/` directory, you should see a newly created file `0001_initial.py`. Take a peek inside! At this point there's no need to understand exactly what's going on in there, but get a feel for what these migration files look like.

Finally, to actually create the the tables in our database, we need to run this new migration. As with the first round of migrations, just run

    python manage.py migrate
    
See that bit of output? Yeah, that's the one. `Applying content.0001_initial... OK`. It freaking worked! We have our tables! :D

## Last checks
- Does `python manage.py runserver` work as expected?
- Try experimenting with your models in the Python shell by running `python manage.py shell`
  - Can you create new instances of your model in the Python shell?
    - You'll first have to import your models (`from content.models import Contributor, ...`)
    - Create them with syntax like `c = Contributor(last_name="Ever", first_name="Greatest")`
  - If you create a Contributor `c` and call `c.save()`, does it exist in the database?
    - After doing this, exit the shell, reenter the shell, then run `Contributor.objects.all()`. Is your contributor in that list?

## Feedback
You're done! Congrats! Just email us the zipped folder, and you can wipe your hands of the whole thing (until next week!).

Also please fill out [this Google Form](https://docs.google.com/forms/d/1t2mpjKZ5GiS_21527SdFzqmS3O7YEDeKkay9_i43Evw/viewform)! We'll be using these responses to improve the comp in the future, yadda yadda yadda, you know the drill. Thanks!
