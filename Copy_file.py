# 使用 python 复制档案

import shutil
# - copyfile
# 只复制文件内容
# 不复制权限、修改时间等资料
# destination 必须是完整的文件名称
# - copy
# 复制文件内容
# 会复制文件权限（Permission）
# destination 可以是文件，也可以是资料夹
# - copy2
# 功能最完整
# 会复制：
# - 文件内容
# - 文件权限（Permission）
# - 修改时间（Modified Time）
# - 存取时间（Access Time）
# - 其他 Metadata（依作业系统而定）
# 适合用来备份档案

path_file = r"C:\Users\user\Desktop\workshop"
ori_file = f"{path_file}/source.txt"
move_file = f"{path_file}/next.txt"
shutil.copyfile(ori_file,move_file)
