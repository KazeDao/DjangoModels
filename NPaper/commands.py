# переходим в директорию с manage.py
cd NPaper

# запускаем shell
python manage.py shell

# импортируем необходимые для работы модули
from NewsPortal.models import *
from django.contrib.auth.models import User
from django.db.models import Sum

# создаём юзеров
User.objects.create_user('User1')
User.objects.create_user('User2')

# создаём авторов, связанных с юзерами
Author.objects.create(user_id=1)
Author.objects.create(user_id=2)

# создаём категории
Category.objects.create(category_name='politics')
Category.objects.create(category_name='sport')
Category.objects.create(category_name='economics')
Category.objects.create(category_name='education')

# создаём посты
Post.objects.create(post_author_id=1, post_type='article')
Post.objects.create(post_author_id=2, post_type='article')
Post.objects.create(post_author_id=2)

# создаём укороченный запрос для категорий для дальнейшей имплантации в посты
c1 = Category.objects.get(id=1)
c2 = Category.objects.get(id=2)
c3 = Category.objects.get(id=3)
c4 = Category.objects.get(id=4)

# создаём укороченный запрос для постов
p1 = Post.objects.get(id=1)
p2 = Post.objects.get(id=2)
p3 = Post.objects.get(id=3)

# добавляем категории к постам
p1.post_categories.add(c2)
p1.post_categories.add(c3)
p2.post_categories.add(c4)
p3.post_categories.add(c2)

# создаём комментарии
Comment.objects.create(parent_post_id=1, comm_author_id=1)
Comment.objects.create(parent_post_id=1, comm_author_id=2)
Comment.objects.create(parent_post_id=1, comm_author_id=1)
Comment.objects.create(parent_post_id=2, comm_author_id=2)
Comment.objects.create(parent_post_id=1, comm_author_id=3)

# раздаём комментариям лайки и дизлайки. Так как в задании чёткое количество прописано не было привожу общую форму использования метода
Comment.objects.get(id=n).like_comm()
Comment.objects.get(id=n).dislike_comm()
# n - id выбранного комментария

# раздаём постам лайки и дизлайки. Так как в задании чёткое количество прописано не было привожу общую форму использования метода
Post.objects.get(id=m).like_post()
Post.objects.get(id=m).dislike_post()
#m - id выбранного поста

# обновляем рейтинг авторов/пользователей
Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

# выводим юзернейм и рейтинг самого "популярного пользователя"
Author.objects.order_by('-rating').values('user', 'rating').first()
# ответ на запрос
{'user': 1, 'rating': 14}

# выводим дату добавления, username автора, рейтинг и заголовок лучшего поста, основываясь на лайках/дислайках к этому посту.
# Сразу вывожу id для дальнейшего вызова превью, тк использовать метод совместно с values не представляется возможным
Post.objects.order_by('-post_rating').values('post_time', 'post_author', 'post_rating', 'post_title', 'id').first()
# получаем ответ на запрос
{'post_time': datetime.datetime(2022, 9, 15, 12, 5, 30, 202845, tzinfo=datetime.timezone.utc), 'post_author': 1,
 'post_rating': 4, 'post_title': '', 'id': 1}
# используем метод preview к популярнейшему посту
Post.objects.get(id=1).preview()
# и получаем ответ
'...'
# или сокращаем форму запроса
top_post = Post.objects.get(id=1)
# и снова применяем метод
top_post.preview()
# а в ответ
'...'

# выводим все комментарии с датой, пользователем, рейтингом и текстом к посту с топ рейтингом
Comment.objects.filter(parent_post_id=top_post.id).values('comm_time', 'comm_author', 'comm_rating', 'comm_text')
# и получаем ответ на запрос
< QuerySet[{'comm_time': datetime.datetime(2022, 9, 15, 12, 21, 32, 575972, tzinfo=datetime.timezone.utc), 'comm_author': 1,
'comm_rating': 0.0, 'comm_text': ''}, {'comm_time': datetime.datetime(2022, 9, 15, 12, 21, 41, 167191, tzinfo=datetime.timezone.utc),
'comm_author': 2, 'comm_rating': 1.0, 'comm_text': ''}, {'comm_time': datetime.datetime(2022, 9, 15, 12, 21, 56, 992301, tzinfo=datetime.timezone.utc),
'comm_author': 1,'comm_rating': 1.0, 'comm_text': ''}]>

