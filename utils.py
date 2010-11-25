import string,random

def ranpwd(minlength=7,maxlength=17):
  length=random.randint(minlength,maxlength)
  letters=string.ascii_letters+string.digits # alphanumeric, upper and lowercase
  return ''.join([random.choice(letters) for _ in range(length)])
