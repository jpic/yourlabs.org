from django import template

register = template.Library()

def get_comment_reply_skeleton(comment):
    skeleton = []
    skeleton.append('%s wrote:' % comment.user)
    skeleton.append('> ')
    for line in comment.comment.split("\n"):
        skeleton.append('> ' + line)
    skeleton.append('> ')
    return u"\n".join(skeleton)
register.filter('get_comment_reply_skeleton', get_comment_reply_skeleton)
