from pinax.apps.blog import feeds

class BlogFeedAll(feeds.BlogFeedAll):
    def feed_title(self):
        return "YourLabs local blog post feed"

class BlogFeedUser(feeds.BlogFeedUser):
    pass
