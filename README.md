# git_text_and_img_from_url
爬取指定网页，输出网页的所有图片何文本；
>注意：本项目调试环境是mac，其它系统请依据步骤做出适当调整。

# 1、环境部署

### 安装 Selenium：

```
pip3 install selenium
```

### ChromeDriver的安装
```
brew cask install chromedriver
```

### 解析库BeautifulSoup的安装

```
pip3 install beautifulsoup4
```

# 运行爬取

```
python3 app.py
```

# 运行结果说明：
* imgs文件夹下是下载的图片，根据网址来名文父文件夹名称
* texts文件下是下载的网页内容

# 可以优化方向

* 现在只是简单爬取单个url，没有进行整个网站跳转，但下载逻辑不变，只不过把爬取深度控制一下
* 页面加载现在是等待指定秒来解决重定向或者js请求，可以优化成判断页面关键元素是否存在来优化时间
* 下载可以改成多线程下载
* 数据库存储可以优化
* 数据过滤
* 网络异常处理
* iframe多个嵌套问题可以优化

