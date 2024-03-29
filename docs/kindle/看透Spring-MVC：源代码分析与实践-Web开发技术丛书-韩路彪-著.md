# 看透Spring-MVC：源代码分析与实践-(Web开发技术丛书)-(韩路彪-著)

---

> 数据量大这个问题最直接的解决方案就是使用缓存，缓存就是将从数据库中获取的结果暂时保存起来，在下次使用的时候无需重新到数据库中获取，这样可以大大降低数据库的压力。

您在位置 #265-267的标注 添加于 2016年11月29日星期二 下午7:24:09

---

> 程序直接操作主要是使用Map，尤其是ConcurrentHashMap，而常用的缓存框架有Ehcache、Memcache和Redis等。

您在位置 #268-269的标注 添加于 2016年11月29日星期二 下午7:25:27

---

> 缓存可以在第一次获取的时候创建也可以在程序启动和缓存失效之后立即创建，缓存的失效可以定期失效，也可以在数据发生变化的时候失效，如果按数据发生变化让缓存失效，还可以分粗粒度失效和细粒度失效。

您在位置 #270-271的标注 添加于 2016年11月29日星期二 下午7:25:46

---

> 跟缓存相似的另外一种技术叫页面静态化，它在原理上跟缓存非常相似，缓存是将从数据库中获取到的数据（当然也可以是别的任何可以序列化的东西）保存起来，而页面静态化是将程序最后生成的页面保存起来，使用页面静态化后就不需要每次调用都重新生成页面了，这样不但不需要查询数据库，而且连应用程序处理都省了，所以页面静态化同时对数据量大和并发量高两大问题都有好处。

您在位置 #282-286的标注 添加于 2016年11月29日星期二 下午7:27:05

---

> 页面静态化可以在程序中使用模板技术生成，如常用的Freemarker和Velocity都可以根据模板生成静态页面，另外也可以使用缓存服务器在应用服务器的上一层缓存生成的页面，如可以使用Squid，另外Nginx也提供了相应的功能。

您在位置 #286-288的标注 添加于 2016年11月29日星期二 下午7:27:24

---

> 其实在常用的数据库中可以不分表而达到跟分表类似的效果，那就是分区。

您在位置 #304-304的标注 添加于 2016年11月29日星期二 下午7:28:41

---

> ·1XX：信息性状态码。 ·2XX：成功状态码，如200表示成功。 ·3XX：重定向状态码，如301表示重定向。 ·4XX：客户端错误状态码，如404表示没找到请求的资源。 ·5XX：服务端错误状态码，如500表示内部错误。

您在位置 #567-570的标注 添加于 2016年11月29日星期二 下午8:06:40

---

> A记录是将域名解析到IP（一个域名可以有多条A记录），CNAME记录是将域名解析到另一个域名（也就是作为另一个域名的别名），查

您在位置 #601-602的标注 添加于 2016年11月29日星期二 下午8:08:25

---

> Container一共有4个子接口Engine、Host、Context、Wrapper和一个默认实现类ContainerBase，每个子接口都是一个容器，

您在位置 #1316-1317的标注 添加于 2016年11月30日星期三 下午5:25:21

---

> ·Engine：引擎，用来管理多个站点，一个Service最多只能有一个Engine。 ·Host：代表一个站点，也可以叫虚拟主机，通过配置Host就可以添加站点。 ·Context：代表一个应用程序，对应着平时开发的一套程序，或者一个WEB-INF目录以及下面的web.xml文件。 ·Wrapper：每个Wrapper封装着一个Servlet。

您在位置 #1326-1330的标注 添加于 2016年11月30日星期三 下午5:26:22

---

> 需要注意的是，同一个Service下的所有站点由于是共享Connector，

您在位置 #1373-1373的标注 添加于 2016年11月30日星期三 下午5:29:36

---

> Spring MVC的本质其实就是一个Servlet，

您在位置 #1766-1766的标注 添加于 2016年11月30日星期三 下午5:43:03

---

> 学习完一样东西之后及时地总结可以在很短的时间内获得很大的收获，这不仅适用于开源框架的学习，同时也适用于其他内容的学习。这么做首先可以加深对所学内容的印象，更重要的是可以站在更高的层次来综合思考，这样就可以将所学的内容整合到一个整体结构中，并且这时候很容易想明白原来没理解的疑点，也就是所谓的将书“先看厚再看薄”中看薄的过程。

您在位置 #5612-5615的标注 添加于 2016年12月1日星期四 下午3:26:07

---

> HTTP协议是单向的，只能客户端自己拉不能服务器主动推，Servlet对异步请求的支持并没有修改HTTP协议，而是对Http的巧妙利用。

您在位置 #5821-5823的标注 添加于 2016年12月1日星期四 下午3:36:51

---

> HTTP协议是单向的，只能客户端自己拉不能服务器主动推，Servlet对异步请求的支持并没有修改HTTP协议，而是对Http的巧妙利用。异步请求的核心原理主要分为两大类，一类是轮询，另一类是长连接。轮询就是定时自动发起请求检查有没有需要返回的数据，这种方式对资源的浪费是比较大的；长连接的原理是在客户端发起请求，服务端处理并返回后并不结束连接，这样就可以在后面再次返回给客户端数据。Servlet对异步请求的支持其实采用的是长连接的方式，也就是说，异步请求中在原始的请求返回的时候并没有关闭连接，关闭的只是处理请求的那个线程（一般是回收的线程池里了），只有在异步请求全部处理完之后才会关闭连接。

您在位置 #5821-5827的标注 添加于 2016年12月1日星期四 下午3:37:51

---

