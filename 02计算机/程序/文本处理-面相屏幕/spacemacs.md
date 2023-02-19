## layer

### eww

配置
eww-search-prefix
若输入給eww的字符串不像是URL或主机名,则会使用eww-search-prefix作为搜索引擎.

eww-download-directory
配置eww的下载目录

shr-external-browser
该变量指定了eww使用的外部浏览器

eww-use-external-browser-for-content-type
当打开指定类型的content时,自动使用外部浏览器打开.

eww-header-line-format
该变量指示了eww buffer的head line以什么格式来显示
它是一个格式字符串,其中%t表示website的标题,%u表示访问的URL

shr-max-image-proportion
该值为一个不超过1的浮点数,表示当显示图片时,图片的大小不能超过整个eww window的shr-max-imag-proportion倍

shr-blocked-images
该变量为一个正则表达式,若图片的URL匹配该表达式,则该图片被屏蔽.