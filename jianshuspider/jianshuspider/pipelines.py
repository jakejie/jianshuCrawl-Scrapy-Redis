# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from sqlalchemy import Column, String, create_engine, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Item
try:
    from items import JianshuArticleItem, JianshuUserItem
except:
    from jianshuspider.items import JianshuArticleItem, JianshuUserItem
# 数据库连接信息
db_host = '59.110.230.99'
db_user = 'root'
db_pawd = 'roottoor'
db_name = 'jianbook'
db_port = 3306
# 创建对象的基类:
Base = declarative_base()


# 用户数据
class JianUserInfo(Base):
    __tablename__ = "userinfo"
    # 表结构
    id = Column(Integer, unique=True, primary_key=True)
    # name = Column(String(1024))
    # 用户名
    name = Column(String(256))
    # 作者标志
    article_s = Column(String(32))
    # 主页链接地址
    users_url = Column(String(64))
    # 关注量
    attention = Column(Integer)
    # 粉丝数
    fans = Column(Integer)
    # 文章数
    article = Column(Integer)
    # 字数
    words_num = Column(Integer)
    # 收获喜欢
    gain_like = Column(Integer)
    # 自我简介
    intro = Column(Text)
    # 添加时间
    add_time = Column(DateTime, default=datetime.now)


# 文章数据
class JianshuArticleInfo(Base):
    __tablename__ = "article"
    # 表结构
    id = Column(Integer, unique=True, primary_key=True)
    # name = Column(String(1024))
    # 文章标题
    article_title = Column(Text)
    # 作者
    article_autho = Column(String(256))
    # 图像
    image = Column(String(512))
    # 作者标志
    article_s = Column(String(32))
    # 最后编辑时间
    article_edit_time = Column(String(32))
    # 字数
    article_num = Column(Integer)
    # 阅读数
    article_read = Column(Integer)
    # 评论数
    article_comment = Column(Integer)
    # 喜欢数
    article_like = Column(Integer)
    # 赞赏数
    article_admire = Column(Integer)
    # 作者信息：写了 **** 字，被 **** 人关注，获得了 **** 个喜欢
    # article_autho_info = Column(String(1024))
    # 作者签名信息
    article_autho_intro = Column(Text)
    # 正文——文本——信息
    article_txt = Column(Text)
    # 文章页面链接
    article_url = Column(String(64))
    # 微博长图链接
    weibo_image = Column(String(512))
    # 添加时间
    add_time = Column(DateTime, default=datetime.now)


class JianshuspiderPipeline(object):
    def __init__(self):
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def process_item(self, item, spider):
        if isinstance(item, JianshuUserItem):
            userinfo = JianUserInfo(
                # 用户名
                name=item["name"],
                # 作者标志
                article_s=item["article_s"],
                # 主页链接地址
                users_url=item["users_url"],
                # 关注量
                attention=item["attention"],
                # 粉丝数
                fans=item["fans"],
                # 文章数
                article=item["article"],
                # 字数
                words_num=item["words_num"],
                # 收获喜欢
                gain_like=item["gain_like"],
                # 自我简介
                intro=item["intro"],
            )
            try:
                self.session.add(userinfo)
                self.session.commit()
            except Exception as e:
                print("[UUU] JianUserInfo Error :{}".format(e))
                self.session.rollback()
        elif isinstance(item, JianshuArticleItem):
            article = JianshuArticleInfo(
                # 文章标题
                article_title=item["article_title"],
                # 作者
                article_autho=item["article_autho"],
                # 图像
                image=item["image"],
                # 作者标志
                article_s=item["article_s"],
                # 最后编辑时间
                article_edit_time=item["article_edit_time"],
                # 字数
                article_num=item["article_num"],
                # 阅读数
                article_read=item["article_read"],
                # 评论数
                article_comment=item["article_comment"],
                # 喜欢数
                article_like=item["article_like"],
                # 赞赏数
                article_admire=item["article_admire"],
                # 作者信息：写了 **** 字，被 **** 人关注，获得了 **** 个喜欢
                # article_autho_info = item["article_autho_info"],
                # 作者签名信息
                article_autho_intro=item["article_autho_intro"],
                # 正文——文本——信息
                article_txt=item["article_txt"],
                # 文章页面链接
                article_url=item["article_url"],
                # 微博长图链接
                weibo_image=item["weibo_image"],
            )
            try:
                self.session.add(article)
                self.session.commit()
            except Exception as e:
                print("[AAA] JianshuArticleInfo Error :{}".format(e))
                self.session.rollback()
        else:
            print("[XXX]简述Item Error ===={}".format(item))
        return item


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                           .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    Base.metadata.create_all(engine)
