# 姓名：郭宏亮
# 时间：2023/5/24 20:40
import os.path


def get_project():
    return os.path.dirname(os.path.dirname(__file__))


print(os.path.join(get_project(), "bin"))
