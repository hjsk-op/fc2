from app import db
from flask import abort, json
from fileinput import filename

class User(db.Model):
    """
    用户名 UserName
    """
    __tablename__="users"
    #主键
    uid=db.Column(db.Integer,primary_key=True)
    #用户名
    username=db.Column(db.String(50))
    #密码
    password=db.Column(db.String(50))
    #人脸/此处存储人脸图片的链接
    face=db.Column(db.String(500))
    def to_json(self):
        json_blog={
            'id':self.uid,
            'username':self.username,
            'faceURL':self.face
        }
        return json.dumps(json_blog)


ALLOWED_EXTENSIONS=set(['png','jpg','JPG','PNG','bmp'])
def allowed_file(filename):
    return '.' in filename and filename.replit('.',1)[1] in ALLOWED_EXTENSIONS


class Video(db.Model):
    """
    视频 Model
    """
    __tablename__ = 'videos'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 视频id
    vid = db.Column(db.String(50))
    # 封面图片
    coverUrl = db.Column(db.Text)
    # 详情描述
    desc = db.Column(db.Text)
    # 概要
    synopsis = db.Column(db.Text)
    # 标题
    title = db.Column(db.String(100))
    # 发布时间
    updateTime = db.Column(db.Integer)
    # 主题
    theme = db.Column(db.String(10))
    # 是否已删除？（逻辑）
    isDelete = db.Column(db.Boolean, default=False)

    def to_json(self):
        """
        完成Video数据模型到JSON格式化的序列化字典转换
        """
        json_blog = {
            'id': self.vid,
            'coverUrl': self.coverUrl,
            'desc': self.desc,
            'synopsis': self.synopsis,
            'title': self.title,
            'updateTime': self.updateTime
        }
        return json_blog


def getHomepageData():

    result = {}
    # 获取banner
    banners = Video.query.filter_by(theme='banner')
    result['banner'] = [banner.to_json() for banner in banners]
    # 获取homepage
    first = Video.query.filter_by(theme='hot').all()
    second = Video.query.filter_by(theme='dramatic').all()
    third = Video.query.filter_by(theme='idol').all()
    if len(first) and len(second) and len(third):
        homepage = [{'Hot Broadcast': [item.to_json() for item in first]},
                    {'Dramatic Theater': [item.to_json() for item in second]},
                    {'Idol Theatre': [item.to_json() for item in third]}]
        result['homepage'] = homepage
        return result
    else:
        abort(404)