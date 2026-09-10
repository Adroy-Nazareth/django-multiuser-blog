import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post,Tag
class Command(BaseCommand):
    help='Seed reviewer account and 10 sample posts.'
    def handle(self,*args,**kwargs):
        username=os.getenv('REVIEWER_USERNAME','reviewer'); password=os.getenv('REVIEWER_PASSWORD','change-me-reviewer'); email=os.getenv('REVIEWER_EMAIL','reviewer@example.com')
        user,_=User.objects.get_or_create(username=username,defaults={'email':email})
        user.email=email;user.is_staff=True;user.is_superuser=True;user.set_password(password);user.save()
        samples=[('Building Reliable Django APIs','backend,django','Practical lessons for validation, persistence, and clear API boundaries.'),('PostgreSQL for Python Backends','postgres,python','Why relational persistence remains a strong default for production applications.'),('Writing Better Automated Tests','testing,python','A small testing strategy that catches regressions without slowing development.'),('Django Authentication Basics','django,auth','Using Django sessions and built-in authentication instead of reinventing security.'),('Designing Useful Search','search,ux','Simple text search patterns that keep a small blog pleasant to use.'),('Pagination Without Pain','django,performance','How paginated querysets keep list pages fast and focused.'),('Moderating Community Comments','django,moderation','A lightweight approval workflow for safer community discussion.'),('RSS Feeds for Your Blog','rss,web','Give readers a simple way to follow new posts with RSS.'),('Deploying Django on Render','deployment,render','A practical checklist for static files, environment variables, and Postgres.'),('What I Learned Building This Blog','reflection,python','A short reflection on backend reliability, documentation, and deployment.')]
        for title,tags,excerpt in samples:
            p,_=Post.objects.update_or_create(slug=title.lower().replace(' ','-'),defaults={'author':user,'title':title,'excerpt':excerpt,'content':excerpt+'\n\nThis sample article demonstrates the multi-user blog workflow. It is intentionally small, documented, and ready for extension.','published':True})
            p.tags.clear()
            for name in tags.split(','):p.tags.add(Tag.objects.get_or_create(name=name)[0])
        self.stdout.write(self.style.SUCCESS('Seeded 10 posts and reviewer account. Set REVIEWER_PASSWORD in the deployment environment.'))
