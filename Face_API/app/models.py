from app import db
from flask import abort

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
        return json_video