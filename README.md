## 项目说明

这是一个使用 Python 语言编写的小工具，用于管理和展示读书的摘录。

支持如下的读书摘录：

- Kindle 的 My Clippings.txt
- Moon+ Reader Pro(静读天下)
- 微信读书 (WeRead)

最早一版是在 [muzi502](https://github.com/muzi502/kindle) 的启发之下，将 Kindle 的 My Clippings.txt 文件直接转成 [HTML](https://kindle.einverne.info)，这样就可以静态文件直接交给 GitHub 托管了。

后来发现如果转成 markdown，然后借用静态网站生成器自动渲染成 HTML 就更加方便进行修改了，而不用使用模板或者手动拼装的方式组装 HTML 了。所以借用了 VuePress 项目，首先将书摘转变成 markdown，存放在 `docs/` 下，然后使用 VuePress 通知渲染，成果见：

- <https://clip.einverne.info> 

## 使用说明

### Kindle
1. 从 kindle 中拷贝出 My Clippings.txt 标注文件，附加到 source.txt 文件。

        cat /Volumes/Kindle/documents/My\ Clippings.txt >> source.txt

2. 在 Python3 环境下执行 `python kindle_convert.py`，生成的 markdown 文件会按照书名，依次存放到 `docs/kindle` 目录下。

### Moon+ Reader Pro
和 Kindle 摘录类似，从 Moon+ Reader Pro 中导出 `.mrexpt` 格式的文件。放到 `moonreader` 目录中。然后执行：

    python moonreader.py

执行后，markdown 文件会保存到 `docs/moonreader` 目录下。

### WeRead
微信读书可以导出纯文本的书摘，然后保存到 `weread` 文件夹中，然后执行：

    python weread.py

执行后，markdown 文件会保存到 `docs/weread` 目录中。


## Inspired by

- <https://github.com/cyang812/kindleNote>
- <https://github.com/muzi502/kindle>
- [书伴网 Clippings Fere 工具](https://bookfere.com/tools#ClippingsFere)
