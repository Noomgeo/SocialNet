# Finding a profile
def find_profile(username):
    user_profile = {}
    for profile in profiles:
        if profile['username'] == username:
            user_profile = profile

    return user_profile


# Profile list
profiles = [
  {
    'id': 1,
    'username': 'frank_s',
    'first_name': 'Frank',
    'last_name': 'Sinatra',
    'picture': 'https://www.billboard.com/files/styles/article_main_image/public/media/frank-sinatra-1963-billboard-650.jpg',
    'friends': [2, 5, 9],
  },
  {
    'id': 2,
    'username': 'miles_d',
    'first_name': 'Miles',
    'last_name': 'Davis',
    'picture': 'https://after5detroit.com/wp-content/uploads/2018/01/Miles-Davis-1.jpg',
    'friends': [1, 5, 9],
  },
  {
    'id': 5,
    'username': 'louis_a',
    'first_name': 'Louis',
    'last_name': 'Armstrong',
    'picture': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Louis_Armstrong_restored.jpg',
    'friends': [1, 2, 9],
  },
  {
    'id': 9,
    'username': 'thelonious_m',
    'first_name': 'Thelonious',
    'last_name': 'Monk',
    'picture': 'https://m.media-amazon.com/images/M/MV5BOWQzMGM5NDYtYmJmNi00MmY1LThmNTItOGMxMjEzY2M0MzMyXkEyXkFqcGdeQXVyMjE5MzM3MjA@._V1_SY1000_CR0,0,692,1000_AL_.jpg',
    'friends': [2, 5, 1],
  },
]
