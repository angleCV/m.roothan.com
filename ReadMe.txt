
    先创建数据库 db_3g; 也可以是其它。
    修改 settings 里面的数据库信息 账户密码

    python3 manage.py migrate
    python3 news/push_data.py
    python3 manage.py createsuperuser

    数据导入结束。可以看到测试版本。
    赋权 ;



  建了个中间件 用 request.META["HTTP_USER_AGENT"] 来区别；
    手机端只能访问手机端的官网链接；
    PC端只能访问PC端的链接。
否则都会重定向到各自的首页。本地测试可行；
    局域网手机 3g.roothan.com;
    局域网 PC  roothan.com ;
   两个虚拟主机服务