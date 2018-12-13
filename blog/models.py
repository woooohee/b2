# 문자열 처리 방식이 상이한 파이썬 버전 2 및 3의 호환성을 위한 임포트
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
# url 패턴을 만들어주는 장고 내장 함수 reverse()를 위한 임포트
from django.core.urlresolvers import reverse
from tagging.fields import TagField


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('작성자',
                            unique=True,
                            allow_unicode=True,
                            help_text='제품 유형')
    description = models.CharField('제품유형',
                                   max_length=100,
                                   blank=True,
                                   help_text='작성자 이름')
    content = models.TextField('내용')
    create_date = models.DateTimeField('등록일',
                                       auto_now_add=True)
    modify_date = models.DateTimeField('최종 수정 일시',
                                       auto_now=True)
    tag = TagField('태그',                          # ch07 추가
                   help_text='게시글에 대한 태그')   # ch07 추가

    class Meta:  # 필드 속성 외에 필요한 파라미터를 Meta 내부 클래스로 정의
        verbose_name = '기사'  # 'post'
        verbose_name_plural = '기사 모음'  # 'posts'
        db_table = 'my_posts'  # DB에 저장할 테이블 이름을 my_posts'라고 지정
                                # 기본값(앱이름_모델클래스이름)은 'blog_post'
        ordering = ('-modify_date',)  # 최종 수정 일시의 내림차순 정렬

    def __str__(self):
        return self.title  # 객체를 출력할 때 제목만 출력

    def get_absolute_url(self):  # 이 메소드가 정의된 객체를 지칭하는 URL을 반환
        # 아래에서 'blog:post_detail'는 blog 앱 이름공간의 post_detail이란 의미
        # # Example: /post/django-example/
        # url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
        return self.get_previous_by_modify_date()

    def get_next_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
        return self.get_next_by_modify_date()
