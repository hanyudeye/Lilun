---
layout: default
toc: false
title: github actions 用法      
date:  2023-06-03T15:06:46+08:00
categories: ['github']
---

对博客文档 使用工具 (hexo,hugo,vuePress)进行 静态化生成。

现在，我们一步一步来。

首先在仓库 1 的根目录下，创建 .github/workflows/main.yml 文件，这就是 GitHub Actions 功能的配置文件，用于告诉 GitHub 要做哪些事情，写入以下内容

```
name: Deploy GitHub Pages

# 触发条件：在 push 到 master 分支后
on:
  push:
    branches:
      - master

# 任务
jobs:
  build-and-deploy:
    # 服务器环境：最新版 Ubuntu
    runs-on: ubuntu-latest
    steps:
      # 拉取代码
      - name: Checkout
        uses: actions/checkout@v2
        with:
          persist-credentials: false

      # 1、生成静态文件
      - name: Build
        run: npm install && npm run build

      # 2、部署到 GitHub Pages
      - name: Deploy
        uses: JamesIves/github-pages-deploy-action@releases/v3
        with:
          ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
          REPOSITORY_NAME: somenzz/somenzz.github.io
          BRANCH: master
          FOLDER: public
          #注意这里的 public 是仓库根目录下的 public，也就是 npm run build 生成静态资源的路径，比如有的人是 `docs/.vuepress/dist`

      # 3、同步到 gitee 的仓库
      - name: Sync to Gitee
        uses: wearerequired/git-mirror-action@master
        env:
          # 注意在 Settings->Secrets 配置 GITEE_RSA_PRIVATE_KEY
          SSH_PRIVATE_KEY: ${{ secrets.GITEE_RSA_PRIVATE_KEY }}
        with:
          # 注意替换为你的 GitHub 源仓库地址
          source-repo: git@github.com:somenzz/somenzz.github.io.git
          # 注意替换为你的 Gitee 目标仓库地址
          destination-repo: git@gitee.com:somenzz/somenzz.git

      # 4、部署到 Gitee Pages
      - name: Build Gitee Pages
        uses: yanglbme/gitee-pages-action@main
        with:
          # 注意替换为你的 Gitee 用户名
          gitee-username: somenzz
          # 注意在 Settings->Secrets 配置 GITEE_PASSWORD
          gitee-password: ${{ secrets.GITEE_PASSWORD }}
          # 注意替换为你的 Gitee 仓库，仓库名严格区分大小写，请准确填写，否则会出错
          gitee-repo: somenzz/somenzz
          # 要部署的分支，默认是 master，若是其他分支，则需要指定（指定的分支必须存在）
          branch: master

      # 5、部署到 somenzz.cn 服务器
      - name: rsync deployments
        uses: burnett01/rsync-deployments@4.1
        with:
          # 这里是 rsync 的参数 switches: -avzh --delete --exclude="" --include="" --filter=""
          switches: -avzh
          path: public/
          remote_path: /home/ubuntu/public/
          remote_host: somenzz.cn
          remote_port: 22
          remote_user: ubuntu
          remote_key: ${{ secrets.MY_UBUNTU_RSA_PRIVATE_KEY }}

          ```


# hugo githubaction

## 创建您的工作流程

创建 .github/workflows/gh-pages.yml，第一次部署，要使用 
GITHUB_TOKEN

