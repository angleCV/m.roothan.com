from .models import Article, Categary, slideImage


def set_cates():
    return Categary.objects.all()


def set_sliders():
    return slideImage.objects.all()


def set_page2(num):
    categary = Categary.objects.filter(num=int(num))[0]
    return Article.objects.filter(categary=categary), categary


def set_sigle_info(num):
    categary = Categary.objects.filter(num=int(num))[0]
    _top_news = Article.objects.filter(categary=categary).filter(toutiao=True)

    top_news = [_top_news[0] if len(_top_news) > 0 else Article.objects.filter(categary=categary)[0]][0]
    other_posts = Article.objects.filter(categary=categary).exclude(id=top_news.id)

    return {
        "top_news": top_news,
        "other_posts": other_posts[:5], ##### limit 5 on the index of everyItem
    }


def set_home_infos():
    return [set_sigle_info(x+1) for x in range(12)]

