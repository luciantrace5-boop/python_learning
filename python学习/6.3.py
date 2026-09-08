github_terms = {
    'repository': '仓库，用于存储项目代码',
    'branch': '分支，用于独立开发或实验',
    'commit': '提交，保存更改并记录历史',
    'push': '推送，将本地提交上传到远程仓库',
    'pull': '拉取，从远程仓库下载最新更改',
    'fork': '复刻，将他人仓库复制到自己的账号下',
    'clone': '克隆，将远程仓库完整复制到本地',
    'merge': '合并，将一个分支的更改集成到另一个分支',
    'issue': '议题，用于报告 bug 或提出功能请求',
    'pull request': '拉取请求，请求合并分支更改到主仓库',
    'remote': '远程仓库别名（如 origin）',
    'origin': '默认远程仓库的别名',
    'main': '现代默认主分支名称',
    'master': '传统默认主分支名称'
}
for term, meaning in github_terms.items():
    print(term)
    print(f'\t{meaning}\n')