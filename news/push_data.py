import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()


def write_to_post():
    from news.models import Categary
    enums = "安全热点、管理政策、南方安全视角、安全法治、人才培养、前沿技术、趣味科普、主题活动、热点专题、网络安全法、公民个人信息保护、NSA武器库".split("、")
    to_en = ["safeHot", "ManagementPolicy", "SouthernSecurityPerspective",
             "SafeLaw", "TalentDevolopment", "AdvancedTechnology", "FunScience",
             "ThemeActivity", "HotTopics", "NetSafeLaw", "PersonInfoProtect",
             "NSAarsenal"]
    for i in range(len(enums)):
        Categary.objects.create(categary=enums[i], url="/news/" + to_en[i] +"/", num = i+1)

    print("写入分类完成")


def write_sliders():
    from news.models import slideImage
    for i in range(4):
        slideImage.objects.create(title="第 " + str(i+1) + " 个图片")
    print("写入图片完成")


def push_data_article():
    contents = '''<p>
    <br/>
</p>
<p style="line-height: 2em; text-indent: 2em;">
    <span style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; font-size: 18px;">5月27日上午，根据中央网络安全和信息化领导小组办公室的统一部署，湖南省委网络安全和信息化领导小组办公室在长沙召开全省关键信息基础设施网络安全检查工作部署会议。湖南省委常委、省委宣传部部长、省委网信领导小组副组长蔡振红出席会议并讲话。</span>
</p>
<p style="text-align:center">
    <span style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; font-size: 18px;"><img src="http://gzqinglang.com/media/uploads/images/blob_20170602111113.png" title="" alt="blob.png"/></span>
</p>
<p style="line-height: 2em; text-indent: 2em;">
    <span style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; font-size: 18px;">蔡振红指出，开展关键信息基础设施网络安全检查，是迎接党的十九大胜利召开的重大政治任务，是保障网络运行安全的重要举措，是推动湖南省信息化快速健康发展的现实需要。要通过专项检查，进一步提升网络安全防范意识，加快构建关键信息基础设施安全保障体系。</span>
</p>
<p style="line-height: 2em; text-indent: 2em;">
    <span style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; font-size: 18px;">蔡振红强调，要深入查找薄弱环节，迅速开展督促整改，强化安全防护措施，加强监测预警和应急处置。要加强关键部位监测和防护，加强重点网站安全管理，加强核心数据防护，为党的十九大胜利召开营造安全有序的网络环境。</span>
</p>
<p style="line-height: 2em; text-indent: 2em;">
    <span style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; font-size: 18px;">此次检查工作将于6月初开始，8月底结束。湖南省委网信办负责人就有关事项作了具体部署。会议要求，各市州、各部门要根据全省统一部署，抓紧研究制定本地区、本单位的网络安全检查工作方案，确保按时按质完成检查工作。（记者 李国斌）</span>
</p>
<p>
    <br/>
</p>'''
    num = 120
    from numpy.random import randint
    from news.models import Categary, Article
    from django.utils import timezone

    for i in range(num):
        r = randint(12) + 1
        cate = Categary.objects.get(num=r)
        Article.objects.create(
            categary = cate,
            title= str(i) + "==" + str(cate)+"==测试用例==",
            content="内容测试" +"===="+str(i) +"===="+ str(cate) + contents,
            pub_date=timezone.now(),
        )
    print("导入文章结束")


if __name__ == "__main__":
    write_to_post()## 切记不要重复导入
    write_sliders()
    push_data_article()


'''
insert into db_3g.news_article (categary_id, pic, title, content, pub_date, author, sourcefrom) select c.categary_id, c.pic, c.title, c.content, c.pub_date, c.author,c.sourcefrom  from(

select a.toutiao, b.id as categary_id, a.pic, a.title, a.abstract, a.content, a.published, a.pub_date, a.author, a.sourcefrom, a.slug_url from
 (
    select *,1 as num from pages.news_focusarticle
    union all
    select *,2 from pages.news_policyarticle
     union all
    select *,4 from pages.news_lawarticle
     union all
     select *,5 from pages.news_talentsarticle
     union all
    select *,6 from pages.news_techarticle
    union all
    select *,7 from pages.news_popularscience
) as a

left join(
    select * from db_3g.news_categary
) as b
on a.num = b.num
)as c;
'''
